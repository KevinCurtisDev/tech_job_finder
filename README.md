# Tech Job Finder

<img src="" style="width: 100%; height: auto;">

## Summary
Tech Job Finder is a web application built with the django framework. The webApp allows users to securely sign up/in. Once signed in the user is taken to a personalised dashboard with records of interactions he/she has had with recruiters about job postings. The user is also able to look through job listings, check job details, apply to the recruiter who posted the listng, and offer a donation for use of the service.

## User experience
The user experience for the Tech job finder app has been designed around use cases for the following users:

* System administrator
* Recruiter
* Job seeker

### User stories
The following user stories were used to guide the development of the UI and the database structure.

Site administrator
As an administrator, I want to log in to the backend admin area. Add, remove or edit jobs, add, remove or edit recruiters and recruiter details, link specific jobs toindividual recruiters, view or delete enquiries.

* 

Recruiter:
As a recruiter, I want to log in to the backend admin area. View job enquiry details and details of the sender of the enquiry.

* 

As a job seeker, I want to..

* 

## Wireframing the UI and app layout
Balsamiq was used to create wireframes of the UI and app layout, illustrating how the app should look and function across multiple screen sizes and devices. You can view the wireframes at the following link: [wireframe preview](https://github.com/KevinCurtisDev/tech_job_finder/blob/master/wireframes/techjobfinder.pdf)

The display will look the same on both desktop and tablet sized screens.

## Technologies

* Django framework (python programming language)
* PostgreSQL (database)
* JavaScript (frontend interaction)
* HTML5 & CSS3 (layout and styling)
* Stripe API (for processing payments)
* Balsamiq (wireframing during design phase)
* Digital Ocean (hosting)

## Site architecture

### Apps

* Pages - Generates views for the index, message board, and resources pages
* Donations - Generates a class based payement page, which redirects to a Charged page on payment completion.
* Contacts - 
* Jobs -
* Recruiters - 
* Accounts - Generates the user login and register views, and validates user credentials.

### HTML Template structure

Jinja templating hase been implemented in structuring the html layout. Each page extends a base html page that includes elements common to all pages. The common elements have been further abstracted away by building them as smaller (partial) html components. Conditional statements in the jinja templates account for what is displayed in the header section based on whether the user is logged in or out.


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

#### Chrome Lighthouse Audit

* Run all lighthouse audit checks and update with suggested improvements

### Testing outcomes

#### Unregistered users 
* can sign up or view the about page.
* can not log in.
* can not sign up with a user name or email address already registered.
* are shown error messages in the browser to warn about sign up information.

#### Registered users
* can sign in.
* can view job listing once signed in.
* can view individual job details once signed in.
* can make enquiries about specific jobs to the job poster once signed in.
* can make a donation once signed in.
* can sign out once signed in.

#### Super user
* can sign into the backend admin area.
* can add new job listings and associate them with a specific recruiter.
* can delete job postings.
* can add or delete recruiters.
* can view enquiries sent to individual recruiters.

#### Recruiter
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

## Sources

## Future enhancements

The web app could be further improved by including a candidate profile section and a search feature for companies to look up suitable candidates based on those profiles. There could also be two additional sections including a tech blog and a tech job statistics dashboard showing the most in use skills and programming languages based on geographical location.