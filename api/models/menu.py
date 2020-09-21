from django.db import models
from django.contrib.auth import get_user_model


# Create model
class Menu(models.Model):
    # define fields
    date = models.DateField()
    breakfast = models.CharField(max_length=200)
    lunch = models.CharField(max_length=200)
    snack = models.CharField(max_length=200)
    dinner = models.CharField(max_length=200)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    def __str__(self):
        # This must return a string
        return f"The menu for the on {self.date} we have {self.breakfast} for breakfast, {self.lunch} for lunch, {self.snack} for snack and {self.dinner} for dinner."

    def as_dict(self):
        """Returns dictonary version of Menu models"""
        return {
            'id': self.id,
            'date': self.date,
            'breakfast': self.breakfast,
            'lunch': self.lunch,
            'snack':self.snack,
            'dinner': self.dinner
        }
