# Django Card Market
<h1 align="center">
  <a href="" target="_blank"><img src="https://i.imgur.com/4M00e3p.png" alt="Home Page"/></a>
</h1>

### Magic market
This project is my submission for my Data Centric milestone project as part of my training to become a Full Stack Web Developer. The purpose is to apply skills learnt during the Python and Data Centric Development modules. This website uses what I learnt, specifically CRUD operations with the MongoDB database, and rendering data with Jinja and communicating with the backend using flask. The course is provided by the Code Institute. 

As someone with Celiac's disease it can be very challenging to adapt to the Gluten Free diet. Going out for meals becomes a lot more restrictive, and cooking at home can become extremely monotonous if you're always making the same three things. Finding recipes online becomes disheartening once you realize that nearly all of them require multiple ingredients to be replaced. Celiac Haven was created to approach that problem. It's a collection of gluten free, yet delicious, recipes that people everywhere can contribute to. The only gluten free replacements are ingredients that all celiacs already have at home!

The website can be found [here](http://gf-cookbook.herokuapp.com/)

## Table of Contents
1. [**UX**](#ux)
    - [**Colour Scheme**](#colour-scheme)
    - [**Wireframes**](#wireframes)
    - [**General Design Principles**](#general-design-principles)
2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**To-Do List**](#to-do-list)

3. [**Technologies used**](#technologies-used)
    - [**Languages**](#languages)
    - [**Additional Technologies**](#additional-technologies)

4. [**Testing**](#testing)
    - [**Debugging in Chrome**](#debugging-in-chrome-dev-tools)
    - [**Manual Testing**](#manual-testing)
    -[**Validators**](#validators)

5. [**Deployment**](#deployment)
    - [**Local Setup**](#local-setup)
    - [**Deployment Online**](#deployment-online)

6. [**Bugs, Problems and Difficulties**](#bugs-problems-and-difficulties)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)



## UX
### User Stories 
Users of the site are able to:
- Navigate the various apps using the responsive navigation menu.
- Search for card names using the search bar.
- View the top 5 most popular cards on the website, as well as the latest 5 cards to be posted in a carousel-style display. 
- Read up on the latest news in the updates section of the website.
- Access learning material and use the website as a portal to various other community resources.
- Navigate the website easily and effortlessly with redundant navigation in the footer section, as well as view the developers GitHub and LinkedIN.
- Browse all the cards available on the website on the all listings page. The user can preview the card, access all other listings of the same name as a card they're interested in by clicking on the listing name, and access the profile of the user who uploaded the listing.
- Add cards to their cart if the user is authenticated.
- Edit the amount of cards in their cart, or checkout their cart using Stripe payment. 
- View their own profile and edit their listings, or view other users profiles. 
- Register an account, as well as login/logout functionality.
- Advanced search features that allow the user to search for much more specific cards than just typing in their name, with filters such as min/max price, vendor name etc.


### Colour Scheme
This was one of the most surprisingly challenging aspects of the website since I needed the website to appear professional while also being aesthetically pleasing. Dark mode was the initial idea but it was more difficult to make a darker themed website look good as a marketplace website than for example, a video service website such as youtube with a lot of colourful content in the video thumbnails. The final approach was a mostly white website with a very subtle blueish-grey secondary colour.
- The primary background color is ![#2a3439;](https://placehold.it/15/2a3439/2a3439) `#2a3439;`.
- The popular cards section on the home page has a very light grey colour instead of white, which serves to subconsciously break up the website into sections in a content heavy page.

### Wireframes
Wireframes were done using Adobe XD. They can be found [here](https://github.com/DanielJMaia/cookbook-project/issues/1)

### General Design Principles
I set out to make a marketplace website that was simple to navigate and was as functional as possible, even if it meant not being able to make some more aesthetically pleasing choices. An example of this is the home page carousel for the most popular cards and latest listings. The initial approach was to have just the image of the card, and then the user can scroll through them and click on the card to view it. This was more minimalistic and visually pleasing, but it meant that to get information about the item such as the price, a user would have to navigate to a different page and then navigate back if they weren't interested. I chose to add more information to the page, making it less visually pleasing but significantly more functional since now a user can access the vendors profile, view the card price and other relevant information and even add listings to their cart.


---


## Features
### Existing Features
- Site Wide Features
    - Site title which links to the home page. This is common practice across all websites.   
    - Responsive Navbar, if the user is authentica:
        - Browse page, where the user can view all the cards available on the website.
        - My profile, where users can view their own profile. This is very important for vendors who want to go over and edit all their listings.
        - Add a new listing, which allows users to sell cards. They are redirected to a form where they can add a title, description, edition etc. Certain fields have restrictions, such as the condition field which is a dropdown that retrieves its values from the Card model, and the price which is a 2 decimal field number.
        - View Cart page which allows the user to view their shopping cart.
        - Logout,  which logs the user out of their account.
        - Advanced Search, which allows the user to access the advanced search page.
    - A footer with additional information about the company, as well as links to the websites authors' GitHub and LinkedIN pages. It also has a quick access navigation menu that mimics the navigation menu at the top.
- The Home Page 
    - It has a large banner image with some text in the bottom right. This text can advertise the latest product, or link to specific parts of the website. When working for a client, this would be a custom designed banner image that highlights the purpose of the website immediately upon opening it. 
    - Some text which can also be adapted to be some promotional text, latest updates, a message from the company.
    - The top 5 most popular cards on the website, sorted by listing views. This and the latest cards includes the card image, additional information such as the name, additional information, the edition, the condition and price. If the user is logged in, it also allows them to add the listing to their cart.
    - The latest 5 cards, sorted by published date. 
    - Deck help section. This is a community oriented section that allows the user to read up on deck building tips and access resources to help them by clicking on the image. It encourages the user to get in touch with the employees which helps build a relationship and makes them more likely to shop here.
- Browse
    - This page displays a table containing every card on the website, with 20 cards per page shown at once. It's where the users go to, as the name implies, simply browse what's available. They can hover over the camera icon to show an image of the card, view all cards of the same name by clicking on the card name, view other listings by the same person as a card by clicking the vendor name, and view the specific card page where they can see all the information, and add the card to their cart. On mobile, certain columns such as the image preview are hidden to maintain as clean as aesthetic as possible. 
- Login/Register Page if the user isn't authenticated
    - These pages provide the exact functionality you'd expect, a user can either login to their existing account using their email and password, or register an account by providing an email address, a username, a password and password confirmation.
- Add a new lsiting
    - This is a form that allows the user to upload a new listing to their account. As mentioned above, the form takes fields such as title, description etc. and allows the user to type pretty much anything. It also contains inputs such as condition where the user has to select from a dropdown menu which interacts with the backend. 
- View Cart
    - This page allows the user to view the items which they've added to their shopping cart. It displays each listing individually on the left side, as well as the quantity which is easy to edit. On the right side, it has a mock user address, the total quantity of items the user is going to purchase and the total cost. If this website was going into production there would be a way for the user to put in their shipping address and it would go through the multiple checkout steps instead of redirecting straight to the stripe payment, but that's outside of the scope for this project.
- Logout
    - As expected, this logs the user out.
- Advanced Search
    - This feature was quite important to me. Marketplace websites are often a place where users simply browse for products, as opposed to going straight to product X. Adding filters such as min/max price and then displaying a filtered table based of those parameters significantly improves the browsing experience.
- Basic Search bar
    - This allows the user to search by card name, and displays the results in a table. 

### To-Do List
- More advanced checkout
    - As mentioned above, a website like this in production would take the user through several checkout steps, such as asking for the user shipping and billing address.
- Vendor Features
    - Once checkout has been processed, it would be nice to have the vendor informed that their orders have been bought and then have them receive buyer information. The buyer should also receive an email confirmation with a transaction ID.
- The final step would be using the Scryfall API to set up a database with all 20 000+ cards. This would then serve to provide autocomplete functions when searching cards, as well as significantly more filtering options. 


---


## Technologies used
### Languages
- HTML - The language used to create the structure of the pages.
- CSS - The language used to style pages.
- JavaScript - The language used to create dynamic content such as the bootstrap carousels.
- Python - The language used to work in Django and create everything in the backend, including the accounts app, the checkout app, the search app and cards and user database.
### Additional Technologies
This includes frameworks, libraries and services.
- [Django](https://docs.djangoproject.com/en/3.0/) - Python Web Framework which formed the core of my entire project. 
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) - Web Template engine for Python.

- [Heroku](https://heroku.com/) - Cloud platform service which was used to host the final version of the website.

- [JQuery](https://jquery.com/) - JavaScript library used to initialize Materialize elements and the image preview section of edit_recipe.html and create_recipe.html.
- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/) - A widely used framework for building responsive, mobile-first sites. Bootstrap classes, as well as their JS were used widely throughout the entire project. 
- [GitHub](https://github.com/) - GitHub provides a remote repository with git control.
- [GitPod](https://gitpod.io) - An online cloud-based IDE built with deep GitHub integration, using this IDE was a breath of fresh air after AWS and being able to share my workspace  was massively helpful.

---


## Testing
Testing was done in the Chrome Browser, and due to time constraints there was no automatic unit-testing. 
### Debugging in Chrome Dev Tools
The Chrome Dev Tools were the single most useful debugging resource throughout the creation of this website. The most important features were
- Console logging. This allowed me to view the value of variables and data from the DB in the console. If incorrect values, or no values, were being returned, I could pinpoint the exact issue.
- Network logs were useful when I was creating all my routes. They allowed me to check that all my external files were loading.
- Responsive Layout. This project was created using a mobile first mentality. Viewing the page on a large amount of sizes and screen ratio ensured that at no point the project wasn't accessible on all devices.
#### Other Browsers Used For Testing
I do not have any devices that can run Safari. In a professional environment I assume I'd have colleagues who own Macs. If not, I'd have to run Macintosh (or perhaps just Safari) in a virtual environment on Windows or Linux.
- Firefox Developer Edition
- Microsoft Edge

### Manual Testing
On all browsers:
- The mobile version scales as intended, and provides 100% of the functionality of the desktop one.
- Each navigation item was pressed from the index, category, recipe, edit recipe and add recipe pages. This includes the title which redirects to the home page. 
- The searchbar was used on each of these pages.
- An incorrect entry was typed in i.e. "asdasd" to make sure that the error message appeared. 
- Partial words were types in to make sure they still returned results. 
    - chicken - This returns all the recipes with chicken in their title.
    - thie - This returns the banana and blueberry smoothie.
    - OATS - This returns the berries, oats and yoghurt cereal recipe. 
    - a - This returns all recipes with the letter a in their title.
- The view recipe page displays the ingredients and method arrays on new lines for each array item.
- On the add recipe page, I ensured that a recipe couldn't be submitted without the required field.
- An error message correctly displays if there wasn't a picture associated with the URL the user typed in for the recipe image.
- The image preview displays instantly  in the image preview box when the user types in a valid URL.
- Deleting a recipe actually deletes it, and adding one adds it to the correct category.
- The edit recipe button displays the edit page with each input autofilled with the correct values.
- The delete button properly displays a functioning alert.
- Each category displays the appropriate recipes, and clicking a recipe displays the appropriate page.
- The social media links open in a new tab and direct to the correct github and LinkedIN profiles

### Validators
HTML, CSS, JS and Python validators were used to ensure that the code was syntactically correct. For CSS, everything came back 100% correct. However, for the HTML files that wasn't the case, and this is due to Jinja. The W3 Validator returned all instances of {{}} as errors. The solution was to simply go through each error carefully and confirm that each one was directly related to instances of Jinja templating. I checked that my JS code was syntactically correct using [esprima](https://esprima.org/demo/validate.html) by pasting the contents of one JS file at a time.
- HTML Validator - [W3] (https://validator.w3.org/) - This only displayed errors with Jinja, and by going through the code carefully I ensured there were no other syntax mistakes.
- CSS Validator - [W3] (https://jigsaw.w3.org/css-validator/) - No syntax errors were detected.
- Python Validator - [extendsclass.com](https://extendsclass.com/python-tester.html) - No syntax errors were detected. I also was able to run the code successfully without any console errors.
- JS Validator - [JSLint](https://www.jslint.com/) - No syntax errors were  detected.

---


## Deployment
### Local Setup
Ensure that the following is installed on your system
- Python3
- PIP3
- PyMongo
- Flask
- Git

The steps to deploying this website on your system are as follows:
1. Download this repository from GitHub, or type the command
```
git clone https://github.com/DanielJMaia/cookbook-project.git
```
2. Add the following environment variables: IP - 0.0.0.0, PORT - 5000 and MONGO_URI you'll get in a moment. You can create these in a .env file, or if you're using GitPod simply add them to your environment variables in the dashboard.
3. Add a requirement.txt file by running the following command 
```
pip3 freeze –local > requirements.txt
```
4. Create a database in MongoDB called milestone-project-cookbook
5. Add the following collections: categories, difficulty, recipes.
6. Populate the difficulty collection with the following documents: 
```
_id: <ObjectID>
difficulty: "Easy"

_id: <ObjectID>
difficulty: "Medium"

_id: <ObjectID>
difficulty: "Hard"
```
7. Populate the categories collection with the following documents:
```
_id: <ObjectID>
title: "Breakfast"
url: "https://i.imgur.com/bnodfjl.jpg"

title: "Easy Meals"
url: "https://i.imgur.com/N1MmIXr.jpg"

title: "Smoothies & Shakes"
url: "https://i.imgur.com/XdGfkfs.jpg"

title: "Fancy Dishes On A Budget"
url: "https://i.imgur.com/h4Yvo9d.jpg"

title: "No Oven Needed"
url: "https://i.imgur.com/JX323Oa.jpg"

title: "Deserts"
url: "https://i.imgur.com/aP70sED.jpgsd"

```

Images of the three catalogues can be found [here](https://github.com/DanielJMaia/cookbook-project/issues/2)

The recipes collection can be populated using the website.

8. In MongoDB find the connect button for the Cluster and press connect  your application. Select Python from the list of Drivers and your current version of Python. Copy the connection string and use that as your MONGO_URI environment variable. Remember to replace "root":"password" with your MongoDB user username and password. 
9. In the bash terminal type python3 app.py to run the application, and preview the running application in a browser or IDE preview window. 

### Deployment Online
1. Create a Procfile by typing 
```
echo web: python run.py > Procfile 
```
You must ensure that it's pointing to the correct file, in this case the Procfile says "web: python3 app.py"
2. Create an account for the web service hosting platform Heroku. 
3. Install Heroku by typing in the terminal
```
npm install -g heroku
```
4. Type heroku in the terminal to ensure it's installed correctly, and if so type
```
heroku login
```
5. Create a new heroku project and set the config variables in settings > reveal config vars. They are the same three as set earlier, IP, PORT and MONGO_URI.
6. After ensuring that you have the requirements.txt and Procfile files up to date, add the project to git by typing 
```
git add .
``` 
in the terminal. 
7. Finally, push the project to Heroku by typing in the terminal
```
git push heroku master
```

---


## Bugs, Problems and Difficulties
*sigh*


## Credits
### Content
Some recipes were taken from [Gousto](https://www.gousto.co.uk/) recipe pamphlets, and the chocolate cake was [Jamie Oliver's Gluten Free Chocolate Cake](https://www.jamieoliver.com/recipes/chocolate-recipes/gluten-free-chocolate-cake/). Some others were personal recipes, such as the smoothie.
### Media
Images retrieved from [Pexels.com](https://www.pexels.com/) unless states otherwise.

Smoothie Category Image found [here](https://beamingbaker.com/triple-berry-smoothie-5-ingredient-paleo-vegan-gluten-free-dairy-free/).

Quote Background Image found [here](https://www.pexels.com/photo/burger-and-vegetables-placed-on-brown-wood-surface-1565982/).

Spicy Chicken Rice Recipe Image found [here](https://www.tablespoon.com/recipes/mexican-chicken-and-rice-skillet/eda0017c-42a8-404b-bc47-22eebcd0586c).

Chorizo Risotto Image found [here](https://www.taste.com.au/recipes/chorizo-pasta/6871b2f9-5686-4354-974d-d7aca8e94388).

Sticky soy chicken recipe image found [here](https://www.bbc.co.uk/food/recipes/asian-style_sticky_23400).

Placeholder upload image found [here](https://woodworkersbelfast.com/placeholder-png/).

My Imgur gallery is currently private and therefore can only be viewed by me.


### Acknowledgements

Travis

[![Build Status](https://travis-ci.org/DanielJMaia/magic-market-project.svg?branch=development)](https://travis-ci.org/DanielJMaia/magic-market-project)