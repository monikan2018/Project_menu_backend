from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.menu import Menu
from ..serializers import MenuSerializer, UserSerializer

# Create views.
class Menus(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = MenuSerializer
    def get(self, request):
        """Index request"""
        # Get all the menus:
        # menus = Menu.objects.all()
        # Filter the menu by owner, so you can only see your owned menu
        menus = Menu.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = MenuSerializer(menus, many=True).data
        return Response({ 'menus': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['menu']['owner'] = request.user.id
        # Serialize/create menu
        menu = MenuSerializer(data=request.data['menu'])
        # If the menu data is valid according to our serializer...
        if menu.is_valid():
            # Save the created menu & send a response
            menu.save()
            return Response({ 'menu': menu.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(menu.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the menu to show
        menu = get_object_or_404(Menu, pk=pk)
        # Only want to show owned menus?
        if not request.user.id == menu.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this menu')

        # Run the data through the serializer so it's formatted
        data = MenuSerializer(menu).data
        return Response({ 'menu': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate menu to delete
        menu = get_object_or_404(Menu, pk=pk)
        # Check the menu's owner agains the user making this request
        if not request.user.id == menu.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this menu')
        # Only delete if the user owns the  menu
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['menu'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['menu'].get('owner', False):
            del request.data['menu']['owner']

        # Locate Menu
        # get_object_or_404 returns a object representation of our Menu
        menu = get_object_or_404(Menu, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == menu.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this menu')

        # Add owner to data object now that we know this user owns the resource
        request.data['menu']['owner'] = request.user.id
        # Validate updates with serializer
        data = MenuSerializer(menu, data=request.data['menu'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
