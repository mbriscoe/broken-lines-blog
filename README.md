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

Navigation is provided via a bootstrap navbar. CSS code has been added to underline menu items on hover and tint the navbar for each page. Font Awesome icons have been added to each menu item to add visual clues.

<img src="https://github.com/mbriscoe/Ethereal-Expressions/assets/86828720/6278e0e9-371f-4190-8527-9988f7a4d5c4" style="width:70%;">

- **The Footer**

The page footer is arranged in 2 rows. The first row contains social media links for the site and the second row contains links to the site team's GitHub pages.
The footer layout was created using CSS flex.  

<img src="https://github.com/mbriscoe/Ethereal-Expressions/assets/86828720/3e936859-663d-4d57-9b4f-38e4c8627a01" style="width:70%;">


### Home Page

The Home page is formed by a carousel built on Bootstrap as the main element, a gradient banner, and two Bootstrap grids, the first one with two images and two pieces of text and the second one with  four images on the same row. The first element, the carousel is built up to catch the users' attention when they first visit the site and inform them about the content to expect through the site. Following the carousel, a banner works as a transitional element between the carousel and the content. 

The gradient style of the banner uses the same colours as the images chosen for the first grid and its borders. Finally, the last point  is the use of representative images of the painter and her creative process taking place, in order to provide relevant visual information about the quality of the artist’s work.

<img src="https://github.com/mbriscoe/Ethereal-Expressions/assets/86828720/aa86ebb5-e68b-4e42-8536-4e605799fa10" style="width:70%;">


### About Page

The About page is compounded by two pictures, followed by two pieces of text. Bootstrap grid has been used to fit them on the page and make them responsive. For smaller devices, the elements collapse one on top of each other, having the images at the top and the bottom, and the text, in the center.  For devices with higher resolution such as tablets, laptops and desk computers, the elements expand evenly in two rows, and each element takes  50 per cent of the space available.

<img src="https://github.com/mbriscoe/Ethereal-Expressions/assets/86828720/0e44e6d5-6efe-49ae-8c16-ed46b25fc010" style="width:70%;">


### Gallery Page

The gallery page contains eight four-piece collections from the artist, displayed in a grid using Bootstrap CSS. The user can click on any of the pieces to see it full-size, and an on-hover shadow effect highlights image as the mouse passes over them.

<img src="https://github.com/mbriscoe/Ethereal-Expressions/assets/86828720/5dea4234-8c38-4fd1-8e0c-2e863001c600" style="width:70%;">


### Contact Page

The contact page is comprised of two parts. First, there is a contact form for users to get in touch with the artist. This give options to submit either a general enquiry, a purchase enquiry or to contact about a commission. 

The second part of the page deals with contact details for the artist giving a portrait photo, contact details and an embedded map showing her location.

This page was structured using bootstrap.

<img src="https://github.com/mbriscoe/Ethereal-Expressions/assets/86828720/35aa091f-62d6-4557-a52a-05a543820609" style="width:70%;">


## Testing

### Manual Testing
<img src="https://github.com/mbriscoe/Ethereal-Expressions/assets/86828720/c0e89b6c-78a8-42a2-8b48-bc6b39ac513e" style="width:100%;">

### Lighthouse
The site was tested using Lighthouse with the following results:
<img src="https://github.com/mbriscoe/Ethereal-Expressions/assets/86828720/ed031055-ecac-4a09-93e0-d9710011e550" style="width:70%;">


### Responsive Testing

Alongside the built in Bootstrap responsive CSS, media queries were used throughout our own CSS to provide a consistent user experience. Chrome dev tools were used frequently to test the site at standard screen sizes and the site was manually viewed on laptops, tablets and phones.

<img src="https://github.com/mbriscoe/Ethereal-Expressions/assets/86828720/216eaf29-7853-4fe9-b3e1-4ed9ff705c84" style="width:70%;">


### Browser Compatibility
The site was tested on the following browsers:
- Chrome
- Firefox
- Edge
- Opera
<img src="https://github.com/mbriscoe/Ethereal-Expressions/assets/86828720/2104c398-4375-40d0-af15-25cba812c33e" style="width:70%;">


### Validator Testing

- HTML

  - No errors were returned when passing through the official [_W3C validator_](https://validator.w3.org/nu/?doc=https://mbriscoe.github.io/Ethereal-Expressions)

- CSS
  - No errors were found with our own CSS code when passing through the official Jigsaw validator. However, there were many errors found in the Bootstrap CSS code, which is a normal result.

## Bugs
All bug fixes were dealt with efficiently and cleanly.
- BUG: contact page width issue
- BUG: Footer overlapping content
- BUG: Shading display on gallery page


## Deployment

- The site was deployed to GitHub pages from the main branch of the repository early in the developemnt stage for continuous deployment and checking.

- The live link can be found [_here_](https://mbriscoe.github.io/Ethereal-Expressions/)


## Credits

### Content

- all content is copyright Broken Lines Publishing Limited 2024.
- The posts were created by various members of the band.

### Media

- For this project, all media was supplied by Broken Lines.
