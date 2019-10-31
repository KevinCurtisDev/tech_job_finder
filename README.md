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
As an administrator, I want to..

* 

Recruiter
As a recruiter, I want to..

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

* Conditionally show specific pages when logged in
* Allow specific actions for regular users
* Allow specific actions for super user
* Do all backend and frontend form validation checks work?
* Can I make a payment when loggin in, do I get notified if the payment worked or not?

#### Chrome Lighthouse Audit

* Run all lighthouse audit checks and update with suggested improvements

### Testing outcomes

## Deployment

The completed webapp will be deployed to the Digital Ocean hosting platform. 

## Difficulties

## Sources

## GDPR concerns and suggestions

In order to limit the information held about users of the webapp and mitigate possible GDPR violation, I suggest limiting information stored in the database to hashed paswords and email addresses. Allowing stripe to take care of the payment transactions will also remove GDPR concerns around storing card details.