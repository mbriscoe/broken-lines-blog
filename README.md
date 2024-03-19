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

- **Navigation Bar**

<p>Navigation is provided via a bootstrap navbar.</p>
<img width="516" alt="navbar1" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/f6512fcd-f7e8-4aa3-8ddc-bfeb76c998a9" style="width:70%;">

<p>And is fully responsive</p>
<img width="784" alt="navbar2" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/c68630ba-a572-4079-a07e-1b7e56c6a82a">

<br><br>
- **The Footer**

The page footer is a simple arrangement of 3 social media icons.
<img width="738" alt="footer" src="https://github.com/mbriscoe/broken-lines-blog/assets/86828720/bc205537-b534-4795-9d16-f9ffb589e12e">


## Testing

### Manual Testing
The site was tested on the following browsers vfor compatibility:
- Chrome
- Firefox
- Edge
- Opera

### Lighthouse
The site was tested using Lighthouse with the following results:
<img src="https://github.com/mbriscoe/Ethereal-Expressions/assets/86828720/ed031055-ecac-4a09-93e0-d9710011e550" style="width:70%;">


### Responsive Testing

Alongside the built in Bootstrap responsive CSS, Chrome dev tools were used frequently to test the site at standard screen sizes and the site was manually viewed on laptops, tablets and phones.


### Validator Testing

- HTML

  - No errors were returned when passing through the official [_W3C validator_](https://validator.w3.org/nu/?doc=https://mbriscoe.github.io/Ethereal-Expressions)

- CSS
  - No errors were found with our own CSS code when passing through the official Jigsaw validator. However, there were many errors found in the Bootstrap CSS code, which is a normal result.


## Deployment

- The site was deployed to Heroku from the main branch of the repository early in the developemnt stage for continuous deployment and checking.
- The PostgreSQL database was served from ElephantSQL

- The live link can be found [_here_](https://broken-lines-blog-d7e7160138f2.herokuapp.com/)


## Credits

### Content

- all content is copyright Broken Lines Publishing Limited 2024.
- The posts were created by various members of the band.

### Media

- For this project, all media was supplied by Broken Lines.
