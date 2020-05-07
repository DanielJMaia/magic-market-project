# Django Card Market
<h1 align="center">
  <a href="" target="_blank"><img src="https://i.imgur.com/jEqfUpo.png" alt="Home Page"/></a>
</h1>

### Magic market

This project is my final submission for the Code Institute course "Full Stack Developer". The purpose of this project is to apply skills learnt during the final sections of the course, specifically using and implementing a fullstack website created using Django, a python web framework created to ease the creation of complex, database-driven websites. The development of this website was a brilliant learning opportunity and has left me far more confident moving forwards and working on professional websites for real clients. 

The website is a marketplace website, similar to ebay, where users can buy and sell Magic: The Gathering cards. While there definitely isn't a shortage of marketplace websites selling Magic cards, competition is extremely healthy and allowing users to sell their collections instead of one company selling cards to buyers will result in an overall decrease of prices in what is currently a very expensive market. This also helps smaller stores in towns where there just isn't enough people buying their cards at their physical location stay afloat, and it's not hard to imagine that with competitive pricing those smaller stores could make most of their revenue selling cards online, using their physical location mianly to host tournaments and build a local community. Last but definitely not least, online marketplaces like this allow players who don't have easy access to a local games shop purchase all the latest product! Friend groups who live nowhere near a store can still get together and play cards. This game has been around for two decades and websites like this help bring it straight to people's front door.

The website can be found [here](https://magic-market.herokuapp.com/)

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
- View the top 3 most popular cards on the website, as well as the latest 3 cards to be posted in an easy to view row. Subtle animations help the aesthetic of this section, with cards raising a little when the user hovers over them. 
- Read up on the latest news in the updates section of the website.
- Access learning material and use the website as a portal to various other community resources.
- Navigate the website easily and effortlessly with redundant navigation in the footer section, as well as view the developers GitHub and LinkedIN.
- Browse all the cards available on the website on the all listings page. The user can preview the card, access all other listings of the same name as a card they're interested in by clicking on the listing name, and access the profile of the user who uploaded the listing.
- Sell cards by filling out a simple and fast form. They add fields like a name, a description, which edition the card is, how many are for sale and attach an image. The image size doesn't matter since the website forces the image to be the correct size for display on the website, and all cards have the same aspect ratio.
- Add cards to their cart if the user is authenticated. The maximum amount of cards they can add corresponds to the amount of that card the vendor has for sale.
- View all the cards of the same name that are on sale, so as to always ensure they're finding the cheapest option.
- Edit the amount of cards in their cart, or checkout their cart using Stripe payment. 
- View their own profile and edit their listings, or view other users profiles. 
- Register an account, as well as login/logout functionality.
- Edit their account.
- Advanced search features that allow the user to search for much more specific cards than just typing in their name, with filters such as min/max price, vendor name etc.


### Colour Scheme
This was one of the most surprisingly challenging aspects of the website since I needed the website to appear professional while also being aesthetically pleasing. Dark mode was the initial idea but it was more difficult to make a darker themed website look good as a marketplace website than for example, a video service website such as youtube with a lot of colourful content in the video thumbnails. The final approach was a mostly white website with a very subtle blueish-grey secondary colour. The home page contains some lighter blues that were added later to make the website more welcoming and to fit with the large image shows when you open the site.
- The primary background color is ![#2a3439;](https://placehold.it/15/2a3439/2a3439) `#2a3439;`.
- The secondary, lighter blue colour is ![#3d698c;](https://placehold.it/15/3d698c/3d698c) `#3d698c;`. This is a nice colour on the home page, but wasn't used for the rest of the website as it's a more content focused site.
- The popular cards section on the home page has a very light grey colour instead of white, which serves to subconsciously break up the website into sections in a content heavy page.

### Wireframes
Wireframes were done using Adobe XD. They can be found [here](https://github.com/DanielJMaia/magic-market-project/issues/2)

### General Design Principles
I set out to make a marketplace website that was simple to navigate and was as functional as possible, even if it meant not being able to make some more aesthetically pleasing choices. An example of this is the home page section for the most popular cards and latest listings. The initial approach was to have just the image of the card, and then the user can scroll through them and click on the card to view it. This was more minimalistic and visually pleasing, but it meant that to get information about the item such as the price, a user would have to navigate to a different page and then navigate back if they weren't interested. I chose to add more information to the page, making it less visually pleasing but significantly more functional since now a user can access the vendors profile, view the card price, see the condition and even add listings to their cart. If they want more information such as the quantity, they can click on the card itself to be redirected to that specific listing. 

Another example of a more minimalistic but functional approach is that the tables used in sections such as "browse" are very information heavy, but with no additional "fluff" to make it look prettier. The user can still view the cards by hovering over the camera icon, but a more visually pleasing option would have been a large grid with the images already displayed. It would have added a lot of colour to the site, but in exchange for significantly fewer cards per page. 


---


## Features
### Existing Features
- Site Wide Features
    - Site title which links to the home page. This is common practice across all websites.   
    - Responsive Navbar, if the user is authenticated:
        - Browse page, where the user can view all the cards available on the website.
        - Advanced Search, which allows the user to access the advanced search page.
        - Account, a dropdown menu. This contains:
            - My profile. This allows the user to edit their listings, view their most recent listings, view their most popular cards and view all the cards they have for sale.
            - A sell cards section. Users are redirected to a form where they can add a title, description, edition etc. Certain fields have restrictions, such as the condition field which is a dropdown that retrieves its values from the Card model, and the price which is a 2 decimal field number.
            - Order history, a page which displays a users order history so they can view all the cards they've bought.
            - Logout,  which logs the user out of their account.
        - Cart page which allows the user to view their shopping cart. A number appears next to it which is equivalent to the amount of cards in their cart.
    - A footer with additional information about the company, as well as links to the websites authors' GitHub and LinkedIN pages. It also has a quick access navigation menu that mimics the navigation menu at the top.

- The Home Page 
    - It has a large banner image with a section in the bottom right that catches the eye and prompts the user to start browsing the vast collection of cards on the website. This area can advertise the latest product, or link to specific parts of the website. When working for a client, this would be a custom designed banner image that highlights the purpose of the website immediately upon opening it. 
    - Some text which can also be adapted to be some promotional text, latest updates, a message from the company. In this case it covers the company's reaction to the global pandemic, a very significant event happening in our lives right now.
    - The latest 5 cards, sorted by published date. I chose to include this before the following popular cards sectio because I believe it's better to have a list of cards that's always changing instead of a list that will remain mostly unchanged.
    - The top 5 most popular cards on the website, sorted by listing views. This and the latest cards includes the card image, additional information such as the price, the edition and the condition. If the user is logged in, it also allows them to add the listing to their cart or edit it if it's their listing.
    - Deck help section. This is a community oriented section that allows the user to read up on deck building tips and access resources such as the MTG subreddit or a card browsing website to help them by clicking on the image. It encourages the user to get in touch with the employees which helps build a relationship and makes them more likely to shop here.

- Browse
    - This page displays a table containing every card on the website, with 10 cards per page shown at once. It's where the users go to, as the name implies, simply browse what's available. The table is sortable (each table header can be clicked to sort by price, name etc), paginated and contains extra information such as how many total entries there are. The user can choose to show between 10, 20 and 50 cards per page. They can hover over the camera icon to show an image of the card, view all cards of the same name by clicking on the card name, view other listings by the same person as a card by clicking the vendor name, and view the specific card page where they can see all the information, and add the card to their cart if it's not their own card. On mobile, certain columns such as the image preview are hidden to maintain as clean as aesthetic as possible. 

- Login/Register Pages if the user isn't authenticated
    - These pages provide the exact functionality you'd expect, a user can either login to their existing account using their email and password, or register an account by providing an email address, a username, a password and password confirmation.

- Add a new lsiting
    - This is a form that allows the user to upload a new listing to their account. As mentioned above, the form takes fields such as title, description etc. and allows the user to type pretty much anything. It also contains inputs such as condition where the user has to select from a dropdown menu which interacts with the backend. The vendor also has to include the total quantity of that card that are going up for sale. This is a very important field as cards that have 0 quantity aren't displayed on the website. When a user is adding cards to their cart, they can only add up to the amount of cards for sale, and if the user successfully buys a card then that amount of cards gets removed from the total amount for sale. This is to take away some of the manual labour on the side of the vendor, they don't have to be on top of which cards are being bought and manually removing taking down the listings. The decision to remove the cards at checkout instead of when adding to the cart was to ensure that people didn't add cards to their cart as a way to remove the listings from view and essentially "reserving" cards, even if it's for a short amount of time until the cart resets. 

- Order history
    - This section of the website allows users to view their previous purchases. They contain order information such as the Order ID, the shipping address, when it was placed and who the order is being dispatched to. Below the order information header is a list of the cards bought, how many of those cards were bought and the price of those cards.

- Cart
    - This page allows the user to view the items which they've added to their shopping cart. It displays each listing individually on the left side, as well as the quantity which is easy to edit. On the right side, it has a mock user address, the total quantity of items the user is going to purchase and the total cost. If this website was going into production there would be a way for the user to put in their shipping address and it would go through the multiple checkout steps instead of redirecting straight to the stripe payment, but that's outside of the scope for this project.

- Logout
    - As expected, this logs the user out.

- Advanced Search
    - This feature was quite important to me. Marketplace websites are often a place where users simply browse for products, as opposed to going straight to product X. Adding filters such as min/max price and then displaying a filtered table based of those parameters significantly improves the browsing experience.

- Basic Search bar
    - This allows the user to search by card name, and displays the results in a table. 

### To-Do List
- More advanced checkout
    - As mentioned above, a website like this in production would take the user through several checkout steps, such as asking for the user shipping and billing address. It would send a confirmation email containing tracking information.
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
- Postgres Database (MySQL) - An open source database management system.
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
Ensure that the following is installed on your system.
- Python3
- PIP3
- Django
- Git

The steps to deploying this website on your system are as follows:
1. Download this repository from GitHub, or type the command
```
git clone https://github.com/DanielJMaia/magic-market-project
```
2. Make sure you have everything mentioned above installed on your system. You can run 
```
sudo pip3 install django==1.11.29 for django.
```
Go through the requirements.txt and make sure you have everything installed. Don't forget Django Storages! 
```
pip3 install django-storages && pip3 install boto3
```
3. The project and the apps should all have imported when you cloned the git project. However, you'll need to make a superuser. Do this using 
```
python3 manage.py createsuperuser
```
4. In order to run this project you need to access the database, and there's two ways to do that. You can access the S3 database, or use the django database which you run locally. I'm going to cover the S3 storage since #1 This works with the HTML code without having to modify anything and #2 It's better to set up the bucket now so that later down the line you don't have to go and re-do all the databases. Just remember to collectstatic when you make changes to your CSS or you won't see them.
5. Set up S3 buckets. I'm not going to do into depth on how to do this, you can read up on it [here](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/) This page helped me quite a bit in going throught he process step by step.
6. Change the AWS_STORAGE_BUCKET_NAME and the region to your bucket and region in settings.py.
7. Set up Stripe in order to get payment working. 
8. Set your environment variables. These are the two STRIPE keys, your Django SECRET_KEY, postgres DATABASE_URL, your AWS_ACCES_KEY_ID and your AWS_SECRET_ACCESS_KEY.
Also set PORT=8000.
9. Run collectstatic to migrate all the static and media files on to the S3 bucket.
10. You're going to need to add your local machine the the list of allowed hosts. Go ahead into settings, set 
```
Debug = True
```
then run the project using 
```
python3 manage.py runserver
```
Copy the recommended host from the error message in the ALLOWED_HOSTS section in settings.py

### Deployment Online
1. Create a Procfile by typing 
```
echo web: python run.py > Procfile 
```
You must ensure that it's pointing to the correct file, in this case the project is called magicmarket.
2. Create an account for the web service hosting platform Heroku. 
3. Install Heroku by typing in the terminal
```
npm install -g heroku
```
4. Type heroku in the terminal to ensure it's installed correctly, and if so type
```
heroku login
```
5. Create a new heroku project and set the config variables in settings > reveal config vars. They are the same as set earlier.
6. After ensuring that you have the requirements.txt and Procfile files up to date, add the project to GitHub by typing 
```
git add .
``` 
in the terminal. 
7. Finally, push the project to GitHub by typing in the terminal
```
git push origin master
```
Make sure that the project is building off the master branch in heroku, and that you've gone into resources and enabled your free dynos. 
8. Redeploy the branch in the deploy section of the heroku dashboard.
---


## Bugs, Problems and Difficulties
- Hiding/showing images in the browse section using JS. Removing the flickering on those images. Also, positioning those elements above the content while also using overflow on the table.
- Redirecting users to a specific profile and a specific card based. I was trying to go to a profile using a username in the frontend but the eventual fix was going to the backend using the ID, then looking at the user model and going to the profile linked to that ID through the backend. 
- Django messages. Rendering logout page is a bad idea. Also, no fade :(
- Secondary key referencing. It's double underscores, not single.
- Greater than/less than filtering. It really doesn't like null fields, and trying to replace null values with 0 or 999999 in the backend was very difficult. This is the only bug I gave up on fixing and just added default values. Same result, ever so slightly less clean. 
- Viewing previous orders. Very annoying. This caused hours and hours of issues. The eventual fix was to clear all my previous migrations because my objects were missing certain fields that I later added, and then coded into the views. Basically I was trying to view order history by accessing the user object tied to the order, but 90% of the orders didn't have a user object. I couldn't even get into the admin panel so I had to delete all my objects. Basically user column didn't exist. AAAA. THis one sucked. 
- Media image URLs change when you upload everything to an S3 bucket. I didn't realise this, and spent a long time wondering why my site was getting my static files from S3 and my media files from GitPod. 


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

[![Build Status](https://travis-ci.org/DanielJMaia/magic-market-project.svg?branch=master)](https://travis-ci.org/DanielJMaia/magic-market-project)