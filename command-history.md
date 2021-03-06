////////////// how to use git in a basic manner ////////////
git add .
git commit -m "some comment"
git push -u oriign main
////////////////////////////////////////////////////////////

//// Creating a Core app to be used in other app /////////
Sometimes, it is necessary to duplicate some portions of code
in different apps. To alleviate this issue and preserve the consistency
of the project, it is of good practice to create a core app and put
common codes there. For example, "created" and "updated" are two model members
that can be used in many models.
Also, we have initialized the room application in this commit.
//////////////////////////////////////////////////////////

/// Completing Room model ////////////////////////////////
First, we have to install a django library for countries, as
pipenv shell
pipenv install django-countries
Then, add django_countries to installed apps.
Now, one just needs to import it and use it, as
from django_countries.fields import CountryField
Next, add all the required fields to the Room model.
/////////////////////////////////////////////////////////

///// How to use manytomany relationships ////////////////
In this commit, I want to use manytomany relationships to
create room types, amenities, and son on. To do so, I need to
define an abstract class for items with two fields called name, and
maybe subtitle. Then, using this abstract class, I define other classes
for my purposes.
//////////////////////////////////////////////////////////

/////// Adding other items to a room /////////////////////
such as amenities, ...
//////////////////////////////////////////////////////////

////// Working with Meta class ////////////////////////////
Meta class of a Model have many options that we can use to
configure the behavior of the class. For example, verbose_name and
verbose_name_plural can be used to define the name of the class in
plural situations.
///////////////////////////////////////////////////////////

///// Adding Photo Class to the Room model///////////////////
Rooms can have many photos. So, we create a Photo class and
assign each photo to a room by a foreignkey concept.
////////////////////////////////////////////////////////////

///// Completing the Review Class Model/////////////////////
////////////////////////////////////////////////////////////

////// Completing Reservation Model ////////////////////////
////////////////////////////////////////////////////////////

////// Completing List Model //////////////////////////////
///////////////////////////////////////////////////////////

///// Adding Conversation and Message Model/////////////////
During a conversation, multiple users can participate and send
messages to each other. To model this procedure as a database entity,
we define a conversation class with participants as manytomany field.
Then, we define a Message class that connects to the Conversation class.
////////////////////////////////////////////////////////////

//// Improving the Admin panel for Room model//////////////
///////////////////////////////////////////////////////////

/////// Customizing Room admin panel ///////////////////////
ordering with specific columns
////////////////////////////////////////////////////////////

/////// Defining custom function in Admin Model for Room/////
It is sometimes necessary to define some custom functions to
show some stattistics in the admin panel. For example, Django does
not support manytomany fields to be displayed via list_display variable.
To do so, it is required to define a custom function and handle it manually.
/////////////////////////////////////////////////////////////

///// How to work with model Managers and Querysets /////////
It is of utmost important to know how to work with django models using
Managers and Querysets. To do so, we can enable django-shell and investigate
the different models using commandline. To activate django-shell, type the following
command in your pipenv-enabled shell:
$python manage.py shell
--> Managers help to retrieve rows from the database without writing
any sql queries.

> > > from users.models import User
> > > User.objects
> > > <django.contrib.auth.models.UserManager object at 0x7fd4dc944fd0>
> > > User.objects.all()
> > > <QuerySet [<User: airbnb>, <User: ramin>]>
> > > As you can see, user manager returns a Queryset.
> > > There are two python functions namely, vars and dir that are helpful for
> > > investigating classes. Look at the examples below:
> > > all_users=User.objects.all()
> > > dir(all_users) --> returns all methods and properties of an object
> > > ..., 'count', 'create', 'dates', ....
> > > vars(all_users) --> returns changeable attributes of an object
> > > Now, let's discover something interesting.
> > > airbnb=User.objects.get(username="airbnb")
> > > dir(airbnb)
> > > ... , 'reservation_set', 'review_set', 'room_set', 'save', 'save_base', ...
> > > You see something interesting, "\*\_set". this object shows that there is a
> > > foreignkey from Room table to the User table. It is awesome.
> > > airbnb.room_set.all()
> > > <QuerySet [<Room: Ramin's Mansion>]>
> > >
> > > Another way to access rooms of a user is to define a related_name field when
> > > defining a forienkey such as:
> > > host = models.ForiegnKey("users.User", related_name="rooms", on_delete="models.CASCADE")
> > > now, we can access the rooms of a user from the user object by calling as:
> > > user.rooms.all() == user.room_set.all()

Change the related_name of all foriegnkey and manytomany fields.

Using the related_name option make life easier.
/////////////////////////////////////////////////////////////

////////// Improving All Admins //////////////////////////////
In this section, we learn how to define methods inside Models.
Sometimes we need to have some statistics to show to users. In this case,
it is better to define methods inside the model to do the task for us.
//////////////////////////////////////////////////////////////

/////improving List, Message, and Conversation Admin//////////////////////
We can define methods inside Models and then use them inside Admins and
wherever they suit.
/////////////////////////////////////////////////////////////

//////// How to use Media in Django ///////////////////////
To upload photos and other types of media, we need to tell Django where we want
to save them on the filesystem. To do so, there is a variable called MEDIA_ROOT
inside settings.py, which is suitable for this purpose.

Also, remember to add this directory to the .gitignore file.

Also, it is required to add "upload_to" argument to ImageField inside Models.
When we upload a photo, that will be saved in the directory pointed to by upload_to
inside the MEDIA_ROOT directory.
///////////////////////////////////////////////////////////

//////// Make Photo Admin fantastic ////////////////////////
Adding thumbnail to the Photo Admin. Because of security reasons, Django
won't interpret your html and js codes inside a string. To let it know that I know
what I do, use mark_safe method with your html-included string.
///////////////////////////////////////////////////////////

/////// Some more points about Admin ////////////////////////
raw_id_fields ---> This variable is used when we have a foriegnkey in a table
and we want to be able to easily select its value with a nice interface. Then, using this
makes life more fun.

admin.TabularInline --->There is also a nice feature in the admin panel that makes Django a fantastic
framework. You can fill elements of the foriegnkey table inside the admin panel that is the source of
that foriegnkey.

/////////////////////////////////////////////////////////////

///// Django Model.save() and Admin.save_model() /////////////
There are two save methods two intercept the save process. The one inside the
model is called by any saving process. But, the one inside the Admin panel is only called when
the admin saves the model. This is very useful to change the admin save method for
different admins. This is a really cool feature of Django.
//////////////////////////////////////////////////////////////

///// How to add custom commands to Django manage.py /////////////////
First, inside each app create the following directories and files:
management
|
|**init**.py
|commands
|**init**.py
|mycommand.py

That python file can be run as:
$ python manage.py mycommand
/////////////////////////////////////////////////////////////////////

//////// Seed Amenities, Facilities, .... ////////////////////////////
There is a useful django package to create fake data and fill database.
In this section, we want to install and use it.
$pipenv install django_seed
$pipenv install psycopg2
Then, put it into installed_apps.
/////////////////////////////////////////////////////////////////////

/////////// Seed Reviews, Reservations, and Lists ///////////////////////////////

//////////////////////////////////////////////////////////////////

/////// Important points about Django, urls, views, and templates ////////
--> Django recieves httprequest from client and transforms it into a python request object
that can be accessed using the request variable passed to the view related to that
url. We can print vars(request) and dir(request) to acquire lots of useful information
regarding this important variable.

--> There is an app called core that we will use it for special url destinations.
It is highly recommended to classify urls in a professional and organized fashion. For example,
we place homepage url is the core app.

--> We put all templates in a directory called templates at the root of the project.
To do so, it is required to add some codes to the settings file.

//////////////////////////////////////////////////////////////////////////

///////////////// Basic structure of Templates ////////////////////////////
Django templates provide a powerful way for structuring the project in a logical manner.
The idea is to divie annd conquer the project frontend with a simple and effective
structure.
///////////////////////////////////////////////////////////////////////////

/////////////////////////////// Pagination ////////////////////////////////
When you are deciding to show lots of content in your pages, it is a good
idea to show them in chunks and not to query all them from the database. In this regard,
it is helpful to use the pagination mechanism. In this part, we want to show the pagination
process both manually and automatically using Django capabilities.

There are cool things about django templates which are called template tags and
filters. When designing a manual pagination using "Next and Previous" concept,
it is necessary to use django tags to increase and decrease the value of page as:
<a href="?page={{page|add:1}}">Next</a>
<a href="?page={{page|add:-1}}">Previous</a>

The next method is to use Django's pagination feature.

the orphans argument of the Paginator class is used to show the last remaining
items in the last page if number of remaining items is less than or equal to
the orphans.

There is still another method using django-based classes that only require to
configure the paginator parameters. That is cool!
The great website for understanding class-based views is https://ccbv.co.uk/

In class-based views, we can add multiple values to the context using
get_context_data method.

///////////////////////////////////////////////////////////////////////////

///////////////// urls and arguments //////////////////////////////////////
Django provides a nice interface to accept url arguments and use them inside
the views. Using 'app_name' and 'namespace', and 'name' make it easy to use django templates to
handle url patterns via {% url 'namespace:name' url_arguments %}.
///////////////////////////////////////////////////////////////////////////

////// How to use urls in models and django admin //////////////////////////
Sometimes it is useful to access a model-row's view on the site. For example,
consider a situation where you want to see a room detail page by pressing a button
on the admin panel. To do so, there is a method called get_absolute_url in the model class.
Check for its implementation on the Room model.

////////////////////////////////////////////////////////////////////////////

////////////// Adding room specifications to the detail page ///////////////
It is a quite easy task. Just get the room object from the database based on the pk.
Then, send that information to the detail template and render there.
Show different information via html.
--> An important point that we have to pay attention to is that, sometimes, there is no
record in the database for what we are querying it. At those situations, we have to use try/except
block or another method and redirect it to a 404 page. See the commit for more detail.
Also, try to use reverse method as much as possible.
/////////////////////////////////////////////////////////////////////////////

////////// Class-based view for Room detail page ///////////////////////////
It is required to configure this class to work properly.
Remember that we learn by seeing errors. In other words, with trial and error process.
DetailView will automatically handle the 404 situation.
////////////////////////////////////////////////////////////////////////////

/////// Coding search functionality for Room app ///////////////////////////
Airbnb has a nice GUI for searching with the help of React. Here, we concentrate
on the functionality of the search method or view. At the beginnig, it is necessary
to establish the basic structure for this purpose like adding view, url, form, input name.

We can search for various features for a room such as country, room type, and ... .

Also, it is necessary to show the selected options to the user after pressing search btn.

The following Django template tag does not work:

<option value="{{room_type.pk}}" 
{% if selected_room_type == room_type.pk %} selected {% endif %}>
{{room_type.name}}
</option>
but instead the following works:
{% if selected_room_type == room_type.pk %}
<option value="{{room_type.pk}}" 
 selected >
{{room_type.name}}
</option>
{% endif %}

////////////////////////////////////////////////////////////////////////////

///////////// Filter Rooms like a boss ////////////////////////////////////
Django's ORM supports various conditional filtering that we are going to examine
them in the following section.

Django provides powerful forms to make life easier for us. In this part,
we're going to develop a form for room search.Let's do it professionally.
To remember user selected choices, it is only required to add request.GET as
an argument to the form: forms.SearchForm(request.GET).

Adding pagination to the room search is a bit challenging, but I solved it
using get_full_path method and a little bit of slicing to find the appropriate href
and sending it back in the context to render in the href of next and previous tags.
///////////////////////////////////////////////////////////////////////////

/////// User related views///////////////////////////////////////////////////
LoginView---->

- basic setup including url, view, template
- adding simple form to login user
- adding clean_email to the form to validate user email
- adding clean method and removing clean_email and clean_password:
  The reason behind this decision is that when checking for password
  validity, we need to query the database to find the user. Although we
  can can solve this problem with a variable inside the class, but we prefer
  to use another forms method called "clean". This is better.
  Also, there is a cool method called add_error, that can be used to associate
  an error to a specific form variable.
- authentication, login, and logout
- Ofcourse, the next step is to would be to use FormView class to write our LoginView.
  SignUpView------>>>
- basic setup including url, template, view, form,.
- create_user, authenticate, and login the new user into the platform
  ModelForm ----->>>>
  This class makes it possible to create forms using models. This ia fantastic!
  Because with the help of this capability of Django, there is no need to define the
  fields of the forms manually. It is done automatically via ModelForm.
  Lets rebuild SignUpForm using ModelForm.

-Email configs and usage ------>>>>>>>>
First, we have to set some email-related configs in settings.py, then use send_email
method to achieve the goal of user registration of sending newsletters.
an important point that must be taken into account is that never expose your credentials in
the settings.py file. Use other files or environment valriables to store passwords or keys. Also,
bare into mind that you must put these files into the .gitignore file to prevent them from
publishing genrelly.
There is a django package for this purpose called django-dotenv.
$ pipenv install django-dotenv
Also, we have to create a .env file to put all security constants there.
Now, We can read environment variables using os.environ.get(blalbla).
For verifying user email, it is necessary to have two fields in the model called
email_confirmed and email_secret. Also, we're going to define verify_email methd inside the
Uder model so we can use it whenever we need to verify a user email, for example if a
user wants to change his/her email.
/////////////////////////////////////////////////////////////////////////////

# Github Login

Open Authorization (OAuth) is used for access delegation for third-party apps to access a user account using tokens not passwords.

## Github OAuth flow

The web application flow to authorize users for your app is:

1- Users are redirected to request their GitHub identity
2- Users are redirected back to your site by GitHub
3- Your app accesses the API with the user's access token

## Required steps

1. Go to the developer settings section of the github, create an OAuth app, and acquire a client_id and client_secret.
2. Save these parameters in the .env file.
3. Create a view called github_login and redirect the user to the github site with some special parameters as below:

```python
redirect_url = f"https://github.com/login/oauth/authorize?client_id={client_id}&callback_uri={callback_uri}&scope=read:user"
```

4. Now, github sends a code to the callback_url that we must use that code along CLIENT_ID and CLIENT_SECRET to post to another url to obtain an access token that we can use it to call github apis based on scope criteria. To send post request to github, we're going to use the 'requests' library.

```bash
   $ pipenv install requests
```

5. Also, it is required to add different login methods to the User model.

6. And one final point is that in order to be able to read the user email from GitHub, the user must make his/her email public via the github settings.

## Tailwindcss
Tailwind CSS works by scanning all of your HTML files, JavaScript components, and any other templates for class names, generating the corresponding styles and then writing them to a static CSS file.

It's fast, flexible, and reliable ??? with zero-runtime.

> Install **Tailwind Css IntelliSense** for vscode.

### Tailwindcss installation
1. We need to install nodejs and npm:
`$> sudo apt install nodejs npm`

2. Initialize node project:
`$> npm init`

3. Install required node packages
`$> npm install gulp gulp-postcss gulp-sass gulp-csso node-sass autoprefixer -D`

4. Install tailwindcss
`$> npm install tailwindcss -D`

5. Add node_modules to .gitignore.

6. `$> npx tailwind init`

7. Create the following directory structure:
`$> mkdir assets`
`$> mkdir assets/scss`
`$> touch assets/scss/styles.scss`

8. Add `gulpfile.js` and write some init code.

9. Add this to the package.json
`"scripts":{
  "css": "gulp"
}`

10. `$> npm run css`

> In order to enable Django server to access the generated css files, it is required to add the following code into the settings.py file:
```python
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
```
> Also, we must enable css usage in the project by adding the following lines to the base.html template:
```html
{% load static %}

<link rel="stylesheet" href="{% static 'css/styles.css' '%}">
```
> It must be pointed out that the tailwindcss's Play CDN is a good option for development purposes. However, for real performance, it is better to the above method. 


> **Size in Tailwindcss**
There is a measurement unit in Tailwindcss called ==*rem*==. The **em** in this unit represents the closest *font-size* of the class. For example:
```css
.box{
  font-size: 20px;
  .child{
    width: 0.5em;
  }
}
```
Here, `0.5em` is equal to `10px`. But `rem` means root em. The example below shows the concept:
```css
html{
  font-size: 10px;
}
.box {
  font-size: 20px;
  .child{
    width: 0.5rem;
  }
}
```
Here, the width of child will be `5px`.

### Useful extensions for designers
- Page ruler
- Colorzilla
- Coolors.co


> `vh` in css means viewport height.

## How to add room_card?
1- First, create an html file in partials named `room_card.html`.
2- To find the first photo of each room, we can add a method to the model class to extract it as below. The name of the method is `first_photo`.
3- Then call that method using the django template language as `{{room.first_photo}}`