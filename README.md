# Tech Job Finder

<img src="https://github.com/KevinCurtisDev/tech_job_finder/blob/master/jobfinder/static/images/techjobfinder.png" style="width: 100%; height: auto;">

## Summary
Tech Job Finder is a web application built with the django framework. The webApp allows users to securely sign up/in. Once signed in the user is taken to a job listings page, where he/she can look through job listings, check job details, apply to the recruiter who posted the listng, and offer a donation for use of the service.

## Features
Custom styled admin area. Admin log in. Super user view, add, edit, delete operations on jobs and recruiters from the admin area. General user login/sign up area. The main feature is a job listing board - showing the latest tech jobs on offer. this area also includes search functionality to find specific jobs. There is a job enquiry area, allowing users to enquire about a specific job to its associated recruiter. Email notification for recruiters (notifying when an enquiry has been made for a specific job posting) is included. Donation page using stripe to make a secure payment. The webapp is responsively designed to work accross multiple sized devices. Custom built slide in menu using pure css (checkbox hack). Elements and pages are conditionally rendered  depending on whether a user is logged in or not. Pop up success/error notifications offering a better user experience with instant feedback are used throughout the application. Pagination is used for displaying a limited number of jobs per page.

## User experience
The user experience for the Tech job finder app has been designed around use cases for the following users:

* System administrator
* Recruiter
* Tech Job seeker

### User stories
The following user stories were used to guide the development of the UI and the database structure.

#### Site administrator:
As an administrator, I want to log in to the backend admin area. Add, remove or edit jobs, add, remove or edit recruiters and recruiter details, link specific jobs toindividual recruiters, view or delete enquiries.

Actions taken:

#### Recruiter:
As a recruiter, I want to log in to the backend admin area. View job enquiry details and details of the sender of the enquiry.

Actions taken:

#### Tech job seeker


Actions taken:

## Wireframing the UI and app layout
Balsamiq was used to create wireframes of the UI and app layout, illustrating how the app should look and function across multiple screen sizes and devices. You can view the wireframes at the following link: [wireframe preview](https://github.com/KevinCurtisDev/tech_job_finder/blob/master/wireframes/techjobfinder.pdf)

The display will look the same on both desktop and tablet sized screens.

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
* Contacts - 
* Jobs -Generates a view for the job listing section and individul job listing/query.
* Recruiters - 
* Accounts - Generates the user login and register views, and validates user credentials.

### HTML Template structure

Jinja templating hase been implemented in structuring the html layout. Each page extends a base html page that includes elements common to all pages. The common elements have been further abstracted away by building them as smaller (partial) html components. Conditional statements in the jinja templates account for what is displayed in the header section based on whether the user is logged in or out.

### Database design


## Testing

### Implemented tests

#### UX & Ui

* Ease of use and navigation
* Page redirects make contextual sense?
* The User knows where they are in the app at any given time
* The user knows that they are logged in or out
* Is there sufficient feedback to the user when they carry out an action on the webapp?
* Loading times and jank check on page paints/repaints
* Responsive design makes sense accross multiple devices and browsers?
* Webapp functions as it should across various browsers


#### Logic 

* Conditionally show specific links in nav bar
* Conditionally show specific pages when logged in
* Allow specific actions for regular users
* Allow specific actions for super user
* Do all backend and frontend form validation checks work?
* Can I make a payment when logged in, do I get notified if the payment worked or not?
* Can I message the recruiter responsible for post a job
* As a recruiter, do I get notified/emailed about new enquiries?
* As a super user can I add/remove content /users


### Testing outcomes

#### Chrome Lighthouse Audit

Google chrome's lighthouse audit was run on the site and returned the following results. Accessibility will be addressed when reviewing the code base. Making the site a pwa will also be considered upon review. All other results returned a higher than average score.

<img src="https://github.com/KevinCurtisDev/tech_job_finder/blob/master/jobfinder/static/images/lighthouseaudit.png" style="width: 100%; height: auto;">

#### Manual testing outcomes
Manual testing was carried out for each type of user. The following user flows were confirmed.

##### Unregistered users 
* can sign up or view the about page.
* can not log in.
* can not sign up with a user name or email address already registered.
* are shown error messages in the browser to warn about sign up information.

##### Registered users
* can sign in.
* can view job listing once signed in.
* can view individual job details once signed in.
* can make enquiries about specific jobs to the job poster once signed in.
* can make a donation once signed in.
* can sign out once signed in.

##### Super user
* can sign into the backend admin area.
* can add new job listings and associate them with a specific recruiter.
* can delete job postings.
* can add or delete recruiters.
* can view enquiries sent to individual recruiters.

##### Recruiter
* can sign in to the backend admin area.
* recieves email notifications to their personal email notifying them of enquiries.
* can view enquiries.

## Deployment

### Live website
The completed webapp will be deployed to the Digital Ocean hosting platform. 

### Running on a local machine

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
FIguring out the database schema was initially a difficult process, as I found myself adding and removing features as I built the web app, which meant changing the database structure a number of times. In the end, I went with a simple setup inspired by Brad Traversy (Traversy Media).

## Sources
All images were taken from unsplash.com.

## Future enhancements

The web app could be further improved by including a candidate profile section and a search feature for companies to look up suitable candidates based on those profiles. There could also be two additional sections including a tech blog and a tech job statistics dashboard showing the most in use skills and programming languages based on geographical location.