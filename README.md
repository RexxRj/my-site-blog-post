# Blog Project In Django

# Introduction

This is a simple blog posting project created using django. Database used is PostgreSQL and deployement is done using render.

The project is made using django 5.1.5 and python 3 in mind.

# Main Features

### Homepage

Homepage contains a brief introduction along with the latest posts uploaded being shown.

![Default Home View](__screenshots/home.png?raw=true "Title")

### Posts

This page shows all the posts available in database

![Post View](__screenshots/posts.png?raw=true "Posts")

### Post Details

This page shows the details of the selected post utlizing slug urls.

![Post Detail View](__screenshots/post_details.png?raw=true "Post_Detail")

### Read Later

Read Later button in post details stores the post id in session. The user can access the saved posts from stored posts.

![Stored Posts View](__screenshots/stored_posts.png?raw=true "Stored_Posts")

# Future Scope

- Add Posts Feature for users.
- Login Feature for users.

# Usage

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django

And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/RexxRj/Project-Repo/zipball/master \
      --extension=py,md \
      <project_name>


### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django

And then:

    $ python3 -m django startproject \
      --template=https://github.com/RexxRj/Project-Repo/zipball/master \
      --extension=py,md \
      <project_name>



After that just install the local dependencies, run migrations, and start the server.

# {{ project_name|title }}

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}

Activate the virtualenv for your project.

Install project dependencies:

    $ pip install -r requirements/local.txt

Then simply apply the migrations:

    $ python manage.py migrate

You can now run the development server:

    $ python manage.py runserver
