# Tech Job Finder

<img src="https://github.com/KevinCurtisDev/tech_job_finder/blob/master/docs/images/techjobfinder.png" style="width: 100%; height: auto;">

## Summary
Tech Job Finder is a web application built with the django framework. The webApp allows users to securely sign up/in. Once signed in the user is taken to a job listings page, where he/she can look through job listings, check job details, apply to the recruiter who posted the listng, and offer a donation for use of the service.

See the live production site at: [Tech Job Finder](http://178.128.166.217/)

## Features
* Custom styled admin area. 
* Admin log in. 
* Super user view, add, edit, delete operations on jobs and recruiters from the admin area. 
* General user login/sign up area. The main feature is a job listing board - showing the latest tech jobs on offer. This area also includes search functionality to find specific jobs. 
* Job enquiry area, allowing users to enquire about a specific job to its associated recruiter. 
* Email notification for recruiters (notifying when an enquiry has been made for a specific job posting). 
* Donation page using stripe to make a secure payment. 
* The webapp is responsively designed to work accross multiple sized devices. 
* Custom built slide in menu using pure css (checkbox hack). 
* Elements and pages are conditionally rendered  depending on whether a user is logged in or not. 
* Pop up success/error notifications offering a better user experience with instant feedback are used throughout the application. 
* Pagination is used for displaying a limited number of jobs per page.

## User experience
The user experience was designed to be simple and to the point, with the intention of minimising the frustrations of the job seeker. The user experience has been fromed around use cases for the following users - with the main focus being the job seeker, thus taking a user centric approach to development:

* System administrator
* Recruiter
* Tech Job seeker

### User stories
The following user stories were used to guide the development of the UI and the database structure.

#### Site administrator:
As an administrator, I want to -
* log in to the backend admin area. 
* add, remove or edit jobs, add, remove or edit recruiters and recruiter details.
* link specific jobs toindividual recruiters, view or delete enquiries.


#### Recruiter:
As a recruiter, I want to - 
* log in to the backend admin area. 
* View job enquiry details and details of the sender of the enquiry.

#### Tech job seeker
As a job seeker, I want to -
* get information about the platform.
* sign up.
* sing in.
* see current job listings.
* search jobs.
* see specific job details.
* make a job enquiry.
* log out.

## Wireframing, layout, & style choice
Balsamiq was used to create wireframes of the UI and app layout, illustrating how the app should look and function across multiple screen sizes and devices. You can view the wireframes at the following link: [wireframe preview](https://github.com/KevinCurtisDev/tech_job_finder/blob/master/wireframes/techjobfinder.pdf)

The display will look the same on both desktop and tablet sized screens.

* Font used: Lato (from google fonts) was used as it projects a clean corporate look.
* Colour palette: Used a monochrome colour palette, with dark green as the base colour in order to invoke a sense of balance and trust.

## Technologies

* [Django framework](https://docs.djangoproject.com/en/2.2/) (python programming language)
* [PostgreSQL](https://www.postgresql.org) (database)
* JavaScript (frontend interaction)
* HTML5 & CSS3 (layout and styling)
* [Stripe API](https://stripe.com/ie) (for processing payments)
* [Balsamiq](https://balsamiq.com/) (wireframing during design phase)
* [Digital Ocean](https://www.digitalocean.com/) (hosting)

## Site architecture
Django applications are made up of multiple self contained applications that interact with each other. The views that render on a user's device are generated from html templates, which contain blocks of python code, injected by jinja.

### Apps

* Pages - Generates views for the index and about pages.
* Donations - Generates a payement page, which redirects to the job listing page (with a success message po up) on payment completion.
* Contacts - Generates a model for job enquiries to be sent to recruiters.
* Jobs - Generates a view for the job listing section and individul job listing/query.
* Recruiters - Generates model for recruters in the database.
* Accounts - Generates the user login and register views, and validates user credentials.

### HTML Template structure

Jinja templating hase been implemented in structuring the html layout. Each page extends a base html page that includes elements common to all pages. The common elements have been further abstracted away by building them as smaller (partial) html components. Conditional statements in the jinja templates account for what is displayed in the header section based on whether the user is logged in or out.

In terms of structuring the html, there is a base.html file which holds the primary elements and links that are common to all pages throughout the application. There are also partial html files (header and footer) that are common to each page. These partials are included in the base.html file. Each page in the app then extends from the base.html, including its own, unique, content between block tags:
```jinja 
{% block contentent %}
```

### Database design
Database design used the following classes and attributes:
* Job
    * id (PK)
    * title
    * location
    * type
    * description
    * salary
    * lised date
    * added
    * recruiter id (FK)
* Recruiter
    * id (PK)
    * name
    * photo
    * bio
    * email
    * phone
* Contacts
    * id(PK)
    * Job
    * job_id(FK)
    * name
    * email
    * message
    * contact_date
    * user_id(FK)

Django provides a auth_user class, and django_admin class, in order to handle permissions.

## Testing

See details of manual tests carried out here: [Tests](https://github.com/KevinCurtisDev/tech_job_finder/blob/master/docs/tests.md)

## Deployment

### Live website
The completed webapp will be deployed to the Digital Ocean hosting platform. 

#### deployment steps
1. Sign in to digital ocean and create a droplet (Ubuntu instance)
2. Set up droplet with ssh key.
3. Click create droplet.
4. Install server dependencies:
```cmd
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```
5. Set up the postgresql database.
6. Create a database user and grant all priveleges (as in the digital ocean docs).
7. Install a virtual environment on the ubuntu machine:
```cmd
sudo apt install python3-venv
```
8. Create and activate a virtual environment in the root directory.
9. Clone the project from github:
```cmd
git clone https://github.com/KevinCurtisDev/tech_job_finder.git
```
10. Install dependencies:
```cmd
pip install -r requirements.txt
```
11. Set up gunicorn and nginx on the server (ref: digital ocean docs)


### Running on a local machine

1. Clone or download the project (green clone button is located at the top right of this page). Altenatively, on your pc, ope the terminal/command line and cd into the location you want to clone the project too, then run the following command:
```cmd 
git clone https://github.com/KevinCurtisDev/tech_job_finder
```
2. Create a virtual environment. 

    * To do this on  a mac, cd into the root directory of the project, then run the command: 
    ```cmd
    python -m venv ./venv 
    ```
    * To do this on  a windows machine, cd into the root directory of the project, then run the command: 
    ```cmd
    py -m venv ./venv
    ```

3. Install project dependencies: 
```cmd
pip install -r requirements.txt
```
4. Create a secrets.py file. 
5. Register with stripe.com and get the appropriate keys. Add your keys to the secrets.py file.
6. You need to have PostgresQL running on your machine. Once it is running, configure the connection with your user name and password in the secrets.py file.
7. Run migrations: 
    * mac-
    ```cmd
    python manage.py runmigrations
    python manage.py migrate
    ```
    * windows
    ```cmd
    py manage.py runmigrations
    py manage.py migrate
    ```
8. Generate a super user:
    * mac-
    ```cmd
    python manage.py createsuperuser
    ```
    * windows
    ```cmd
    py manage.py createsuperuser
    ```
9. Log in to the admin area with your super user credentials at : 127.0.0.1:8000/admin
10. Add recruiter profiles. Add jobs and associate them to individual recruiters.



## Code sample

The following snippet shows a Job class used to create job entries in the postgresql database:

```python
class Job(models.Model):
    #Create database fields for individual jobs
    recruiter = models.ForeignKey(Recruiter, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=200)
    description = models.TextField(max_length=800)
    salary = models.IntegerField()
    listed_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
```


## Difficulties

### Email
Setting up gmail SMPT in order to send messages required a bit of playing around with email settings.

### UI (User interface)
Figuring out the best way to handle the UI of a web app like this was a challenge and an area I will revisit after some further study. While the UI flows quite well, it can at times be difficult to tell how potential users will interact with it. I feel further testing is needed with a larger demographic of tech job hunters and recruiters.

### Database
Figuring out the database schema was initially a difficult process, as I found myself adding and removing features as I built the web app, which meant changing the database structure a number of times. In the end, I went with a simple setup inspired by Brad Traversy (Traversy Media).

## Sources
All images were taken from unsplash.com.

## Future enhancements

The web app could be further improved by including a candidate profile section and a search feature for companies to look up suitable candidates based on those profiles. There could also be two additional sections including a tech blog and a tech job statistics dashboard showing the most in use skills and programming languages based on geographical location. Adding an SSL certificate to the site is an essential next step for live web hosting.