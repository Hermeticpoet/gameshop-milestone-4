# GameShop App | Milestone Project 4

## Table of Contents

1. [Introduction](#Introduction)
2. [UX](#UX)
3. [Features](#Features)
4. [Build-Process](#Build)
5. [Features-Left-to-Implement](#Features)
6. [Technologies-Used](#Technologies)
7. [Deployment](#Depolyment)
8. [Content](#Content)
9. [Credits](#Credits)


## Introduction

This is an incomplete application. Due to time constraints with my new job, I have not had the time needed to fully complete my final projects. Therefore, I have attempted to get as much of my application built as a MVP (minimum viable product) with a basic README in order to get them uploaded before the final deadline. I apologize for submitting this incomplete work but extenuating circumstances have prevented me from fully completing this entire project as I had originally intended.


## UX

A typical user will need to be able to access the home page. They should be able to log in to their own personal account and view all of their own purchases, as well as any products (games) they have built and uploaded to the site. They should also have full visibility on how many times their games were purchased.

The site navigation should be easily intuited which should give a pleasant user experience. 'Things should be where people expect them to be'. Clearly highlighted CTA buttons will be present to guide users on where to go and what to do, in order to achieve this goal. 

Plain but pleasing colour palette will be used with some subtle button hover effects to create a good aesthetic for the end users.


## Features

So basically you will be able to go to the logon page by clicking a button and then you can logon to the systme. And, you will be able to also also log in with Facebook if you are on the logon page.
The user can alternatively sign up as a new user and therefore the application will have two types of users.
It will have a normal player which will be able to purchase new games and they will be able to register as a developer by clicking a checkbox. 
On the main page the user will see a search bar. This will allow for returning search results of various games available to the user to purchase. After a user finds a game they would like to purchase, they will be redirected to the card showing that game and they will be able to buy that particular game themselves.
After this, the user will be redirected again to a web service that will allow them to make simple payments and following this they will once again be redirected to the home page where the game will be available for them to play.
It actuality, the application will renders the Web site Eurail. A Finnish news Web site inside an I-frame that will basically emulate the game.
If you are a developer, you will be able to sign up as such, and then be able to create a team of developers or simply work alone and create your own games that will be sold on the application site to other users. Developers will be able set their own prices for games that they create and upload to the catlogue.
Finally, users will be able to log into the application using their Facebook login authentication.

## Build Process

Django provides the scaffolding of the application. We are simply required to 'fill it out'. For instance, our templates folder must contain a subfolder with the same name as our app folder - 'shop', in my case, so that Django knows where to find all the correct templates for the application.

I have used the `{% load static %}` logic in order to pull the relevant data from the static folder into the base.html file so it can be used throughout the application. Then some simple link references can be used to point to the as needed code, including the 'bulma.css' framework. 

I tested the base.html route and rendering. There is a screenshot of this test in the images folder under filename: [base-html-test.png](gameshop/shop/static/shop/images/base-html-test.png).

## Features Left to Implement

As I have explained in the introduction. This project unfortunately was no completed due to time constraints. Therefore, there are a myriad of features left to implement. That which has not yet been completed will be at a later time by myself when I have the time. I would like to fully complete all my course material for my own personal satisfaction at this stage.

Given all of the above, the major features still left to be implemented would be the "User Authentication", "Payments System" and the "Facebook Login" portal. 


## Technologies Used

* [HTML5](https://www.w3.org/TR/html52/)
* [CSS3](https://www.w3.org/TR/2001/WD-css3-roadmap-20010523/)
* [SASS](https://sass-lang.com/)
* [FONT AWESOME5](https://fontawesome.com/start)
* [DJANGO 3.0](https://docs.djangoproject.com/en/3.0/releases/3.0/)
* [BULMA FRAMEWORK](https://bulma.io/)
* [HEROKU](https://devcenter.heroku.com/categories/reference)
* [SUBLIME TEXT3](https://www.sublimetext.com/docs/3/)
* [SQLITE3](https://www.sqlite.org/docs.html)
* [GUNICORN](https://docs.gunicorn.org/en/stable/settings.html)


### Deployment

This application was deployed to Heroku cloud hosting platform. There were issues around the build process with its deployment. I read the docs on the site and cleared all build processes and reinstated them but this did not resolve the issue. Again, at the risk of sounding like a broken record, time has prevented me from fully investigating and resolving this issue before my project deadline!


### Content

Due to the unfinished state of the project, there is very little content included in this initial final project. Notwithstanding that, the credits section will provide details of where most the content included in the application came from, namely two online courses I borrowed from in order to do this project.

#### Credits

[Django Documentation](https://docs.djangoproject.com/en/3.0/).
The [Udemy Course](https://www.udemy.com/course/complete-django-masterclass/) that was most heavily relied upon for this project. I also borrowed quite a lot of ideas from another [Udemy Course](https://www.udemy.com/course/web-software-development-with-django-game-store-app/). And as such, I would like to particularly thank both of those teachers on Udemy for their course work that assisted me in attempting to build this application.

