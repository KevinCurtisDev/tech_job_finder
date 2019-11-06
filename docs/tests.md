# Testing

## Implemented tests

### UX & Ui

* Ease of use and navigation
* Page redirects make contextual sense?
* The User knows where they are in the app at any given time
* The user knows that they are logged in or out
* Is there sufficient feedback to the user when they carry out an action on the webapp?
* Loading times and jank check on page paints/repaints
* Responsive design makes sense accross multiple devices and browsers?
* Webapp functions as it should across various browsers


### Logic 

* Conditionally show specific links in nav bar
* Conditionally show specific pages when logged in
* Allow specific actions for regular users
* Allow specific actions for super user
* Do all backend and frontend form validation checks work?
* Can I make a payment when logged in, do I get notified if the payment worked or not?
* Can I message the recruiter responsible for post a job
* As a recruiter, do I get notified/emailed about new enquiries?
* As a super user can I add/remove content /users


## Testing outcomes

### Chrome Lighthouse Audit

Google chrome's lighthouse audit was run on the site and returned the following results. Accessibility will be addressed when reviewing the code base. Making the site a pwa will also be considered upon review. All other results returned a higher than average score.

<img src="https://github.com/KevinCurtisDev/tech_job_finder/blob/master/docs/images/lighthouseaudit.png" style="width: 100%; height: auto;">

### Manual testing outcomes
Manual testing was carried out for each type of user. The following user flows were confirmed.

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