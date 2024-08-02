# Broken Lines Blog

This project is to develop a small blog website for the band Broken Lines, as a micro service to enable bnd followerss to keep informed on what hte band is doing and comment and discuss relevant posts.

From a users perspective, they should be able to view posts made by the band, and, if a registered user, comment on those posts to enage in conversation with other users or the band themselves.

In terms of design, a minimalistic approach has been taken in order to let the vibrance of the blg post images dictate the overal feel of the site. should be a cohesive colour scheme and set of styles across the whole site to reiterate the artist's brand. Site layout should enhance rather than impede the user experience to give a welcoming, intuitive feel.

A responsive site layout enables easy navigation on all devices.

## Desktop
<p><img width="1787" alt="desktop" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/8e46f40e-c449-4b8c-9d83-96bc8c37c05e"></p>

## Tablet
<p><img width="600" alt="tablet" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/4e582bf4-a647-40c3-9400-e3cfed679387"></p>

## Mobile
<p><img width="400" alt="iphone" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/a10153a4-f3cc-46a2-bf59-adda58896b9e"></p>


## UX Design

### Typography

[**Font Awesome**](https://fontawesome.com) icons were used for the site icons. For example, the social media icons in the footer of the pages.

[**Lato**](https://fonts.google.com/specimen/Lato) was used for the primary headers and titles.

[**Roboto**](https://fonts.google.com/specimen/Roboto) was used for all other secondary text.



### Colour Palette ###
![screenshot](docs/images/swatch.png)

A simple colour palette was chosen to compliment the vibrant images of the band, with a plain white page background, blue icons and a dark gray footer and individual blog page  header background. A simple red was chosen for the link hover to blog pages.



### Home Page Wireframe Design
<img width="1043" alt="Home" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/fc1c7075-0936-462b-a62c-97e1c3dc9bf1" style="width:70%;">


### Post Detail Page Wireframe Design
<img width="1034" alt="Post Detail" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/0a25af88-2728-4a80-842d-4e39d2dc3233" style="width:70%;">

### About Page Wireframe Design
<img width="1041" alt="About" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/b642421a-90f5-4ed2-a2f3-ffa69172eac8" style="width:70%;">

### Biog Page Wireframe Design
<img width="1035" alt="Biography" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/b3783363-ed00-49d5-ac2a-bd4886549f3d" style="width:70%;">


## User Stories

**As a site user, I can view a list of posts and click on the post I want to view.**

- A list of posts is displayed on the front page
- Multiple posts are listed and paginated

**As a Site User, I can click on a post so that I can read the full text.**

- When a blog post title is clicked, a detailed view of the individual post is displayed.

**As a Site Admin I can create draft posts so that I can finish writing the content later, prior to publishing.**

- As a logged in Admin, they can save a draft blog post
- As a logged in Admin they can finish the content at a later time

**As a Site User I can view comments on an individual post**

- Given one or more user comments the user can view them.
- Given one or more user comments the admin can view them.

**As a Site User I can leave comments on a post**

- Comments need to be approved by an admin user
- Approved comments are listed on the individual post page

**As a Site User I can modify or delete my comments on a post**

- A logged in user can modify their own comments
- A logged in user can delete their own comments

**As a site admin I can approve/disapprove comments in order to filter out objectionable comments**

- Admin can approve a comment
- Admin can un-approve a comment

**As a Site User, I can click on the About link and read about the site.**

- When the About link is clicked, the about page is displayed.

**As a Site Admin, I can create or update the about page.**

- The About app is visible in the admin panel
- The About app is accessible to Admin users

**As a site user I can fill in a contact /collaboration form so that I can submit a message to the site owner.**

- Contact/collaboration form is submitted and feedback given

**As a Site Admin I can mark contact messages as "read".**

- Admin can mark messages as read

**As a user I can click on the biography menu and read the band biography**

- User clicks biography and band biog page displays
- Admin can add/edit band biographies

**As a Site User I can register an account so that I can comment posts.**

- Given an email a user can register an account and log in.
- When the user is logged in they can comment.

**As a site user/admin I can login so that I can access all of available content.**

- User can login and se the full range of available menus.

**As a site user/admin I can logout so that I can leave the site safely.**

- User/admin can logout successfully

The completed sprint was composed of 15 separate items. Having used the MoSCoW approach to prioritisation, 9 were classified as "Must-Have" making up less than 60% of the tasks as recommended. The rest of the first sprint was made up of "Should-Have" and "Could-Have" items.
There were no remaining backlog items.

<img width="1467" alt="kanban" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/ba4b5b09-7b18-4449-b7ba-399ea99bbf00">



## Features

<br><br>

- **Home Page**

The home page of the site offers the user a grid of blog posts, by the band, that the user can click on to read each individual blog post.

![screenshot](docs/images/homepage.png)


<br><br>

- **About Page**

The about page gives details about the band history and offers the option to make a collaboration request, via a form at the bottom of the page. The collaboration request is stored in the database for later review.

![screenshot](docs/images/aboutpage.png)


<br><br>

- **Biogs Page**

The biogs page gives a biographical history of each band member, detailing past experiences in music and previous bands.

![screenshot](docs/images/biogs.png)



- **Navigation Bar**

<p>Navigation is provided via a bootstrap navbar.</p>
<img width="516" alt="navbar1" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/f6512fcd-f7e8-4aa3-8ddc-bfeb76c998a9" style="width:70%;">

<p>And is fully responsive</p>
<img width="784" alt="navbar2" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/c68630ba-a572-4079-a07e-1b7e56c6a82a">

<br><br>
- **The Footer**

The page footer is a simple arrangement of 3 social media icons.
<img width="738" alt="footer" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/bc205537-b534-4795-9d16-f9ffb589e12e">

<br><br>

- **Sign Up**

The site has a facility to sign up as a user in order to make, edit or delete your own comments on blog posts.

![screenshot](docs/images/signup.png)

<br><br>

- **Sign In**

The site has a facility to sign in, once you have created a user account, in order to make, edit or delete your own comments on blog posts.

![screenshot](docs/images/signin.png)

<br><br>

- **Sign Out**

The site has a facility for a user to sign out of their account.


![screenshot](docs/images/signout.png)

<br><br>

- **Admin**

The site has a facility for designated administrators to sign in, in order to administrate the site via the standard Django admin interface.

![screenshot](docs/images/admin.png)

<br><br>


- **Entity Relationship Diagram**
<p>The following data structure was created for the project.</p>

<img width="1200" alt="erd" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/a36f5174-0876-4d27-b6da-9bca6d88bf37">

## Testing

### Manual Testing
The site was tested on the following browsers for compatibility:

### Chrome ###
|   Test	|  Expected Result 	|  Actual Result	|
|---	|---	|---	|
|   Click Home menu	|  success 	|  success 	|
|   Click About menu	|  success 	|  success 	|
|   Click Biogs menu	|  success 	|  success 	|
|   Click Admin menu	|  success 	|  success 	|
|   Click Login menu	|  success 	|  success 	|
|   Click Logout	|  success 	|  success 	|
|   Click individual blog post	|  success 	|  success 	|
|   Create, edit, delete a personal comment	|  success 	|  success 	|
|   Register new account	|  success 	|  success 	|
|   Create collaboration request	|  success 	|  success 	|
|   Access admin interface	|  success 	|  success 	|
|   Responsivity	|  success 	|  success 	|
|   Open new page from social media links	|  success 	|  success 	|

### Firefox ###
|   Test	|  Expected Result 	|  Actual Result	|
|---	|---	|---	|
|   Click Home menu	|  success 	|  success 	|
|   Click About menu	|  success 	|  success 	|
|   Click Biogs menu	|  success 	|  success 	|
|   Click Admin menu	|  success 	|  success 	|
|   Click Login menu	|  success 	|  success 	|
|   Click Logout	|  success 	|  success 	|
|   Click individual blog post	|  success 	|  success 	|
|   Create, edit, delete a personal comment	|  success 	|  success 	|
|   Register new account	|  success 	|  success 	|
|   Create collaboration request	|  success 	|  success 	|
|   Access admin interface	|  success 	|  success 	|
|   Responsivity	|  success 	|  success 	|
|   Open new page from social media links	|  success 	|  success 	|

### Edge ###
|   Test	|  Expected Result 	|  Actual Result	|
|---	|---	|---	|
|   Click Home menu	|  success 	|  success 	|
|   Click About menu	|  success 	|  success 	|
|   Click Biogs menu	|  success 	|  success 	|
|   Click Admin menu	|  success 	|  success 	|
|   Click Login menu	|  success 	|  success 	|
|   Click Logout	|  success 	|  success 	|
|   Click individual blog post	|  success 	|  success 	|
|   Create, edit, delete a personal comment	|  success 	|  success 	|
|   Register new account	|  success 	|  success 	|
|   Create collaboration request	|  success 	|  success 	|
|   Access admin interface	|  success 	|  success 	|
|   Responsivity	|  success 	|  success 	|
|   Open new page from social media links	|  success 	|  success 	|

### Safari ###
|   Test	|  Expected Result 	|  Actual Result	|
|---	|---	|---	|
|   Click Home menu	|  success 	|  success 	|
|   Click About menu	|  success 	|  success 	|
|   Click Biogs menu	|  success 	|  success 	|
|   Click Admin menu	|  success 	|  success 	|
|   Click Login menu	|  success 	|  success 	|
|   Click Logout	|  success 	|  success 	|
|   Click individual blog post	|  success 	|  success 	|
|   Create, edit, delete a personal comment	|  success 	|  success 	|
|   Register new account	|  success 	|  success 	|
|   Create collaboration request	|  success 	|  success 	|
|   Access admin interface	|  success 	|  success 	|
|   Responsivity	|  success 	|  success 	|
|   Open new page from social media links	|  success 	|  success 	|

### Lighthouse
The site was tested using Lighthouse with the following results:
<img width="995" alt="lighthouse" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/c4684a12-5bff-48de-8608-b22aa490d702" style="width:70%;">


### Responsive Testing

Alongside the built in Bootstrap responsive CSS, Chrome dev tools were used frequently to test the site at standard screen sizes and the site was manually viewed on laptops, tablets and phones.


### Validator Testing

- HTML

  - No errors were returned when passing through the official W3C validator
<img width="1082" alt="w3 validator" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/e6127df3-cc68-4216-b769-bc216c3b68ae" style="width:70%;">


- CSS
  - No errors were found with our own CSS code when passing through the official Jigsaw validator.
<img width="1029" alt="css validator" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/2e0830fc-cd8e-4a40-828d-150126247a0a" style="width:70%;">

- Python

  - All Python code was tested for PEP8 compatibility with the Code Institute Linter.

  **The only code that didn't pass was code that was automatically generated by Django**
  
  which was then edited in order to pass.

  ![screenshot](docs/images/linter.png)

  - Javascript

  - All Javascript code was tested for errors with JSHint. There were no code errors and one error related to imported code, which is outside the domain of the test.
  
  ![screenshot](docs/images/jshint.png)

## Deployment

The site was deployed to Heroku from the main branch of the repository early in the development stage for continuous deployment and checking.

The Heroku app is setup with 3 environment variables, repalcing the environment variables stored in env.py (which doesn't get pushed to github).

In order to create an Heroku app:

1. Click on New in the Heroku dashboard, and Create new app from the menu dropdown.

2. Give your new app a unique name, and choose a region, preferably one that is geographically closest to you.

3. Click "Create app"

4. In your app settings, click on "Reveal Config Vars" and add the environment variables for your app. These are:
- DATABASE_URL - your database connection string
- SECRET_Key - the secret key for your app
- CLOUDINARY_URL - the cloudinary url for your image store

The PostgreSQL database is served from ElephantSQL

Once the app setup is complete, click on the Deploy tab and:

1. connect to the required GitHub account
2. select the repository to deploy from
3. click the Deploy Branch button to start the  deployment.
4. Once deployment finishes the app can be launched.

![screenshot](docs/images/heroku.png)


The live link can be found [_here_](https://broken-lines-blog-d7e7160138f2.herokuapp.com/)


## Credits
- This project is based on the "I Think Therefore I Blog" project from the LMS.
  
### Content

- all content is copyright Broken Lines Publishing Limited 2024.
- The posts were created by various members of the band.

### Media

- For this project, all media was supplied by Broken Lines.
