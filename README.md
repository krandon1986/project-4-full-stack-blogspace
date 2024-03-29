<h1 align="center">Blog Space</h1>

## Description

This is my blog site where I can add a series of post on many different topics. People view them and post comments on each post if they wish. All they need to do is log in post a comment, sign up if they don't have an account on the site.  

The site is live can be access [here](https://blogspace-97bdcd968196.herokuapp.com/)

![Responive Mockup](static/screenshots/website.png)

## Design

- __Color Pallete__
    - The three main colors that is used for this site are Black, Taupe White, and Black Fox.
    - Black color is used for background color for the navigation section.
    - Taupe White is used for the background color for the site.
    - Black Fox is used as the background color for the footer section.


![Main Color](static/screenshots/color-pallete.png)


- __Typography__
    - Merriweather google font will be used throughout the main body of blog site, whereas the Teko google font will be used in the headline text. 
    - If the web browser can't render the Merriweather and Teko google fonts, the fonts will fall back to san serif.

![Google Fonts](static/screenshots/google-font.png)

- __Wireframe__
    - This is the home page of my blog site.

    ![Home Page](static/screenshots/wireframe1.png)

    - This is signup page, where first time user can create an account on the site.

    ![Register](static/screenshots/wireframe2.png)

    - This is the login page, where returning users can log back into the site. 

    ![login](static/screenshots/wireframe3.png)

    - This is post page where the supercar can post articles onto the site. Each post page will have same layout, even when the article are different
    - When login, the user will be able to post comment on the post they are visiting.

    ![post page](static/screenshots/wireframe4.png)

## Database Diagrams
This is the diagram of what database is going to be stored on my blog site. The database will have three tables, post, user and comments. All three of them will be connected to each other via the foreign key. 

![database diagram](static/screenshots/database-diagram.png)


## User Stories
In this section, you will look the user stories that is use to help implement certain feature in the certain part on the site. 

- __Site Pagination__
    -   First stage of putting features on the site is paginated list of post, so that the site user can select any post to view.

    ![User Story 1](static/screenshots/User-Story-Site-Pagination-(1).png)

    - As you can see from the home page, it is populated with several different posts via the admin using superuser account. A visiting user can select any post and read it. 

    ![Site Pagination](static/screenshots/User-Story-Site-Pagination-(2).png)

- __View a Post__
    - With the post created, a visiting user can click on the post to view it. 

    ![User Story 2](static/screenshots/User-Story-View-a-Post-(1).png)

    - Once the user select of the post, they can read one and if they want leave a comment. 

    ![View a Post](static/screenshots/User-Story-View-a-Post-(2).png)

- __View Comments__
    - As with the post, users' comments can be viewed as well. 
    - However, the superuser (admin) can view the posted comments on the Django administation page.

    ![User Story 3](static/screenshots/User-Story-View-Comment-(1).png)

    - As a user, they can view post and scroll down to see a posted comment. 

    ![View Comment 1](static/screenshots/User-Story-View-Comment-(2).png)

    - As an admin, the superuser can view all comment posted on site in Django administration page by clicking comments under 'Blog'.

    ![View Comment 2](static/screenshots/User-Story-View-Comment-(4).png)

- __Account Registration__
    - Any visiting user that isn't logged into the sit won't be able post comments. So they would have to register an account by given their email address.

    ![User Story 4](static/screenshots/User-Story-Account-Pagination.png)

    - While logged in and click on one of the post, text box will visible to the user so that they can post a comment. 

    ![Account Registration](static/screenshots/User-Story-Comment-on-a-Post-(2).png)

- __Comment on a Post__
    - Users can engaged conversation with each on the post.

    ![User Story 5](static/screenshots/User-Story-Comment-on-a-Post-(1).png)

    - Once user has posted his or her comment, it need to be approved admin before it is allowed to be shown in the comment section. 
    - The only people that can see it before it is approved is the user that post it. 

    ![Comment on a Post 1](static/screenshots/User-Story.png)

    - Once the comment is approved, the comment visible to everyone.

    ![Comment on a Post 2](static/screenshots/User-Story(2).png)

- __Manage Posts__
    - As site Admin, it is important for superuser to be able create, read, update and delete to be about manage the content on the blog site.

    ![User Story 6](static/screenshots/User-Story-Manage-Post-(1).png)

    - The superuser can gain access all blogs and comment and is able to read, create, update, and delete it from the Django Admin. 

    ![Manage Post](static/screenshots/User-Story-Manage-Post-(2).png) 

- __Modify or Delete Comments__
    - User can edited or delete their comment they have posted.

    ![User Story 7](static/screenshots/UserStory-Modify-or-Delete-Comments-(1).png)

    - By creating the edit button under user's comment and implement the neccesary javascript code to be able to update the posted comments. 

    ![Modify and Delete 1](static/screenshots/User-Story-Modify-or-Delete-Comments-(2).png)

    - The user can make some adjustment to the comment before reposting it. 

    ![Modify and Delete 2](static/screenshots/User-Story-Modify-or-Delete-Comment-(3).png)

    - After the user updates his comment, message will be displayed at the top of the page, but below the navigation section to inform the user that their comment has bee updated.

    ![Modify and Delete 3](static/screenshots/User-Story-Modify-or-Delete-Comment-(4).png)

    - Now the user's comment has been updated.

    ![Modify and Delete 4](static/screenshots/User-Story-Modify-or-Delete-Comment-(5).png)

    - After creating the delete button, clicking will cause a popup to open to inform the user that they are about to delete their comments. 

    ![Modify and Delete 5](static/screenshots/User-Story-Modify-or-Delete-Comment-(6).png)

    - Like when the user updated his comment, they receive a message telling the user that their comment has successfully being deleted.

    ![Modify and Delete 6](static/screenshots/User-Story-Modify-or-Delete-Comment-(7).png)

- __Create Drafts__
    - As a Site Admin, they create draft on the Django admin and save the contrant finish it later. 

    ![User Story 8](static/screenshots/User-Story-Create-Drafts-(1).png)

    - Logged in as superuser, the Admin can create half finished post and save it as a draft. 

    ![Create Draft](static/screenshots/User-Story-Create-Drafts-(2).png)

- __Approve comment__
    - Everytime user post a comment on the site, it doesn't become visible to the public until the admin approves it.

    ![User Story 9](static/screenshots/User-Story-Approve-Comments-(1).png)

    - Looking at post comment via the admin, the approve boolean is left unchecked. which means it is still invisible to public except the user who posted it. 

    ![Approve Comment](static/screenshots/User-Story-Approve-Comments-(2).png)

## Testing

- HTML Validator
    - [Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblogspace-97bdcd968196.herokuapp.com%2F)

- Accessibility

    - Home Page

        ![Index](static/screenshots/accessibility-(1)-home.png)

    - Post Page

        ![Post](static/screenshots/accessibility_(2)_post_page.png)

    - Sign Out

        ![Signout](static/screenshots/accessibility_(3)_signout.png)

    - Sign Up

        ![SignUp](static/screenshots/accessibility_(4)_signup.png)

- Mobile Responsiveness
    - The lowest to highest maximum screen width for responsive design was done from 338px to 912px.   
    - Mobile responsiveness was limited to the "toggle device" feature in Chrome Developer Tools due to lack of access to more physical devices.

## Bugs

| Bug | Solution |
| --------------- | --------------- |
| 1. I was unable to delete ny posted comment | Spelling error in the code|

## Deployment
This project was deployed in Heroduk using the Code Institute's terminal.
- Step for deployment:
    - Clone the the blogspace repository.
    - Create a new Heroku app.
    - Name the new Heroku app.
    - Go on setting and click the 'Reveal Config Vars' button.
    - Enter 'PORT' as a key and 8000 as value.
    - Set the buildbacks to 'Python' and 'NodeJS' in that order. 
    - Link the Heroku app to the blogspace repository.
    - Click [Deploy Branch](https://blogspace-97bdcd968196.herokuapp.com/)
