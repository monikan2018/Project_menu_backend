
FAMILY MENU

FAMILY MENU is an web application built to plan family meals by making joint family efforts. Family members can access the menu and add meals for the day. They can also look at all the menu enteries and can edit meals or delete the daily entry.

## Important Links

- [Deployed Client]()
- [Client Repo](https://github.com/monikan2018/Project_menu_frontend)
- [Deployed API]()
- [API Repo](https://github.com/monikan2018/Project_menu_backend)

## Planning Story

The first step was to decide on the prompt and prepare schedule to deliver the project ontime. I decided to make the we all struggle with everyday to plan family meals. I initially started with the planning out with Asana but not working in team made me not being actively filling the enteries in Asana. I went back to using paper and pen to plan out. I first desigend the schema for the database and then completed the backend. Next I designed the wireframes for the application and realized the redundant data and also to add date instead of day in order to make improvement in frontend in future iterations.

In this project we had a choice to pick frontend and backend of our choice. Since I wanted to challenge myself and learn Django I picked Django for backend and React for frontend. After completeing the backend and the wireframes, I started working on the frontend. For the first time I used react to manipulate dates and to create a table with the buttons that perform edit and delete operations. I tried different date pickers but was not able to store the date. I decided to use react-datepicker and learned how store changes to Object and run it through axios. I did not want to stop on create as it was day 3 as I was still stuck on add the record. I decided to complete the code for other crud operations.
After fixing the date error, it took a lot of google search to understand how in react you can access the id for rows in the table that you populated data with. Lot of GA's instructors help and google search helped out in completing this project.

### User Stories

- As an unregistered user, I would like to sign up with email and password.
- As a registered user, I would like to sign in with email and password.
- As a signed in user, I would like to change password.
- As a signed in user, I would like to sign out.
- As a signed in user, I would like to add meals to menu.
- As a signed in user, I would like to update meals in menu.
- As a signed in user, I would like to delete any day's menu.
- As a signed in user, I would like to see all days meals.
- As a signed in user, I would like to see the meals that I am updating.
- As a signed in user, I want to be able to update or create inventory without
  having to know what my current inventory levels are.
- If the user wants to update a day , the app should not allow user to change
  date and with PATCH request update the existing menu.

### Technologies Used

- React.js
- Javascript
- HTML/CSS
- Sass
- Bootstrap
- Axios
- Django
- proto(UI design)
- Lucidchart

### Unsolved Problems

In future iterations, we'd like to ...

- Add a suggestion box for famiy members to list their suggestions
- Allow family members to have their own login and does not allow them to edit the menu
- Shoud be able to fo back and look at monthly menu by allowing date range to get records
- To connect the meals with recipes that also updates the grocery list
- Add the grocery list in the qrcode to have the list easily accessible on any device.

## Images

#### Wireframe:
[ERD]https://app.lucidchart.com/documents/view/4817cabd-f8da-4a1f-a70c-2825b4d5f39a/0_0#?folder_id=home&browser=icon
[Home](https://i.imgur.com/zVmPXau.png)
[Sign Up](https://i.imgur.com/tSZEbx2.png)
[Sign In](https://i.imgur.com/PemHvsQ.png)
[CREATE](https://i.imgur.com/NjAAvJf.png)
[SHOW](https://i.imgur.com/z9Fzlo0.png)
[UPDATE](https://i.imgur.com/GN5FlQu.png)
