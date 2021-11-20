<a href="https://ibb.co/BC9qwjv"><img src="https://i.ibb.co/QK4rXnh/Screenshot-2021-11-20-at-10-31-24.png" alt="Screenshot-2021-11-20-at-10-31-24" border="0"></a>


# Game Review Site
GameReview is an online site/app designed to let user's find and review their favourite games. As well as look for other user's views on games they have a potential interest in playing.

## User stories
---

### External User’s  Goal
- Find games which they would like to play
- Leave feedback and personal views/experiences of games they have played

### Site Owner’s Goal
- Earn money on each game purchased via links from the site

### First Time Visitor Goals
- As a first time visitor I want to know the purpose of the site and easily be able to navigate it
- As a first time visitor I want to be able to easily register
- As a first time visitor I want to be able to create my first review easily
- As a first time visitor I want to be able to see top rated games

### Returning Visitor Goals
- As a returning visitor I want to be able to update or edit a previous review
- As a returning visitor I want to be able to see other user’s reviews on new or older games
- As a returning vistor I want to see if there are any new highly rated games

### Frequent Visitor Goals
- As a frequent visitor I want to be able to update previous reviews in line with games being updated and improved
- As a frequent visitor I want to be able to easily follow a link to highly rated game to purchase it

## Design 
---

* Colour Scheme
Main colour scheme for the site will be a dark theme with #2F3437 (Onyx) and #666666 (Dim Gray) for headers background colours and cards. I will then be using a mix of #FF7073 (Light Coral), #9CF6F6 (Celeste) and #FOE5E9 (Lavender Blush) to stand out against the darker main colours of the backgrounds. These colours compliment each other well and I feel give a video game theme type feel to the website. 

* Typography
Permanent Marker font / Press Start 2p will be used for the main branding for the site in the header. The rest of the site will use Zen Kurenaido which is clear and easy to read and also gives a video game type feel.

* Imagery


## Wireframes 
---

[Small screens](lib/static/wireframes/small-ms3.pdf)

[Medium screens](lib/static/wireframes/med-ms3.pdf)

[Large screens](lib/static/wireframes/lrg-ms3.pdf)

## Data Structure
---
[Rough Data Structure](lib/static/wireframes/data-structure.png)

### Any updates made to the Wireframes?

## Features 
---
### Features to implement in the future
- Rather than a simple buy now link, a price comparison checker and affiliate links to a number of stores selling the game would serve both the customer and the site owner better.
- The API I used didn't contain game information, however giving each individual game it's own page with more information and perhaps videos, would be more informative to users.

- I have also realised too late it would have been a good idea to limit the ammount of user reviews rendered on the reviews page. This is beacuase this page will become increasingly slower as more reviews are added. This would have been easily implementable but I only thought of it last minute when carrying out testing on performance.

## Technologies used
----
### Languages used
- Html
- CSS
- JavaScript
- Python

### Frameworks, Libraries & Programs Used
- Materialize 
- Font Awesome
- MongoDB

## Testing
---

### Testing User Stories from User Experience (UX) Section

#### Site Owner's Goals
- Earn money on each game purchased via links from the site

  i. Affiliate links are placed on every game card generated and each point to Amazon video games category with a search for the relevant game name.

#### First Time Visitor Goals
- As a first time visitor I want to know the purpose of the site and easily be able to navigate it.

  i. As a first time visitor the site is clearly named and shows clear sections pointing the user towards registering and reviewing.

- As a first time visitor I want to be able to easily register

  i. Registration is straightforward and massages are flashed to help a user if they have for example not entered matching passwords.

- As a first time visitor I want to be able to create my first review easily

  i. reviews are easily created (once logged in). Through the data accessed via the RawG api you can then post your review to the site.

- As a first time visitor I want to be able to see rated games

  i. Reviews of games can be accessed regardless of being a registered user or not

#### Returning visitor Goals
- As a returning visitor I want to be able to update or edit a previous review

  i. Previous reviews can be updated either from the reviews page either by scrolling through or using the search functionality. Or they can also be updated from the user's own profile which lists all the user reviews.

- As a returning visitor I want to be able to see other user’s reviews on new or older games

  i. All reviews can be seen on the reviews page and searched for using the search bar at the top for more specific results

#### Frequent Vistor Goals
- As a frequent visitor I want to be able to update previous reviews in line with games being updated and improved

  i. Previous reviews can be updated either from the reviews page either by scrolling through or using the search functionality. Or they can also be updated from the user's own profile which lists all the user reviews.

- As a frequent visitor I want to be able to easily follow a link to highly rated game to purchase it

  i. Buy links are available on every game from the home page. These link to amazon with the search querying the game name in the video games section of amazon.

### Further Testing

- The site was tested across multiple browsers including ; Firefox, Chrome, Explorer and Safari.

- The site was tested across multiple screen sizes and resolutions from small to larger phones, tablets, laptops and desktop monitors.

- All navigation links and external links were tested extensively to ensure they were working on each and every page, and went to the right place.

- Friends and family tested the site and provided feedback.

- Used the W3C Markup Validator and W3C CSS Validator to check every page of the project to ensure there were no syntax errors.

### Validation Checks

- [CSS](lib/static/validation/css.validator.png)

- [Home/Games page](lib/static/validation/screenshot.games.png)
- [Review page](lib/static/validation/screenshot.getreview.png)
- [Register page](lib/static/validation/screenshot.register.png)
- [Sign in page](lib/static/validation/screenshot.signin.png)
- [Change password page](lib/static/validation/screenshot.changepass.png)
- [Confirm delete account page](lib/static/validation/screenshot.delete.png)
- [Edit Review page](lib/static/validation/screenshot.edit.png)

### Bugs and Fixes 
- I originally started my project in another repository and was coding locally using VS code. This however led to many problems as i wasn't aware i would have to use a virtual enviroment when coding locally. This led to problems deploying with way too many requirements being needed. I had to more or less start from scratch using gitpods online code editor. Which I had no problems with moving forwards.

- I originally tried to do a seperate for loop inside a for loop for my buttons as my game['name'] variable was throwing a HTML error when run through the validator. This didn't work however as i then ended up with 8 buttons on top of eachother. Therefore i used the Jinja in line functions to replace the blank space with a "+". 

- Mainly the links from the "buy now" buttons do take the user to relevant results. However they aren't all consistent as if for example the game is on the app store it wont be purchaseable through amazon. At the least it does show other relevant things they could buy realting to the game though. 

- I have also realised too late it would have been a good idea to limit the ammount of user reviews rendered on the reviews page. This is beacuase this page will become increasingly slower as more reviews are added. This would have been easily implementable but I only thought of it last minute when carrying out testing on performance.

- I put my API call inside a try except statement so that the app would load even depsite an error being thrown. However i forgot to put a statement in informing the user. Realised too late before project submission.


## Deployment
---

I deployed this site on heroku through github, below are the steps that i took;

### Github 
The project was deployed to Heroku using the following steps;
1. Logged into my github accound and created a new workspace
1. Using the Code Institute template i named my new project and created the repository
1. using the method "pip3 freeze > requirements.txt" in the terminal you will create a requirements text file which heroku will need to deploy successfully"
1. Before being able to deploy the app an initial commit must be made, see below example
1. ```
   cd myapp
   git init
   Initialized empty Git repository in .git/
    git add .
    git commit -m "My first commit"
    Created initial commit 5df2d09: My first commit
    44 files changed, 8393 insertions(+), 0 deletions(-)
   create mode 100644 README
   create mode 100644 Procfile
   create mode 100644 app/controllers/source_file
1. Any changes then have to be pushed to Github before Heroku can display the site in it's current state.

### Forking the GitHub Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the GitHub Repository
1. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
1. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone
1. Log in to GitHub and locate the GitHub Repository
1. Under the repository name, click "Clone or download".
1. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
1. Open Git Bash
1. Change the current working directory to the location where you want the cloned directory to be made.
1. Type git clone, and then paste the URL you copied in Step 3.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

### Heroku
1. Once logged into Heroku click 'New' then 'Create New app.'
1. Inside the settings you need to 'reveal config vars' and input these to match exactly the contents of your env file. This information needs to remain updated with any new sensitive information you are keeping hidden from the front end.
1. You are given three deployment methods. I choose to use the second option which was through Github (you will need to connect your heroku to your personal github).
1. From here it is just a case of finding the repository you wish to deploy and selecting the correct branch. 

## Credits
---

### Code 
- All code was written by the developer using the following documentation as an aid;
  1. https://docs.python-requests.org/en/latest/
  1. https://flask.palletsprojects.com/en/2.0.x/
  1. https://jinja.palletsprojects.com/en/3.0.x/
  1. https://werkzeug.palletsprojects.com/en/2.0.x/

### Content
- All content was written by the developer

### Media 

- All images and data excluding user reviews and ratings were sourced from [RAWG API](https://rawg.io/apidocs)

### Acknowledgements
- [Stack Overflow](https://stackoverflow.com/) was a great resource if i had any problems, often i could find the same or similar issue on here and get an idea for how to fix it.
- My mentor Narender helped me throughout the project and was always available if i needed advice.

