# GameShop App | Milestone Project 4

This is an incomplete application. Due to time constraints with my new job, I have not had the time needed to fully complete my final projects. Therefore, I have attempted to get as much of my application built as a MVP (minimum viable product) with a basic README in order to get them uploaded before the final deadline. 

# The Application & its Functions


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


## Technologies Used

* [HTML5]()
* [CSS3]()
* [SASS]()
* [FONT AWESOME5]
* [DJANGO]()
* [BULMA FRAMEWORK]()
* [HEROKU]
* [SUBLIME TEXT3]()
* [SQLITE3]()

### Credits

[Django Documentation](https://docs.djangoproject.com/en/3.0/).
The [Udemy Course](https://www.udemy.com/course/complete-django-masterclass/) that was most heavily relied upon for this project. I also borrowed pretty quite a lot of ideas from another [Udemy Course](https://www.udemy.com/course/web-software-development-with-django-game-store-app/). And as such, I would like to particularly thank both of those teachers on Udemy for their course work that assisted me in building this application.

