
================
Django on Gondor
================

This Django project is a very simple example that will work out-of-the-box on
Gondor. You can use this to start your project that will be hosted on Gondor.

Usage
=====

Create a virtual environment (see `virtualenv`_) and install Django::

    pip install Django==1.4.2

Now you are ready to start your Django project. Use ``startproject`` to get
this template.

pinax-project-account
=====================

a starter project the incorporates account features from django-user-accounts
and integrates with gondor

Usage:

    django-admin.py startproject --template=https://github.com/diarmuidw/pinax-project-account/zipball/master <project_name>


To make this project runnable you will need to install its dependencies in
your virtual environment.

::

    pip install -r requirements.txt
    
You might get an error with the postgress install but you can comment that lines out

psycopg2==2.4.5

Make sure to uncomment it when deploying to Gondor so that your database will run!

modify gondor.yml to add in your gondor site key 
You may also need to change projectname to whatever your project is


    git init
    git add .
    git commit -m "Initial project layout"
    gondor deploy primary master


Layout
======

The project layout follows the Django 1.4+ layout.

::

    pinax-project-account/
        .git or .hg (version control metadata)
        fixtures/
            initial_data.json (where any data that should be loaded into the database on each deploy)
        gondor.yml (Gondor configuration file)
        manage.py
        project_name/ (project's Python package)
            __init__.py
            settings.py
            settings_gondor.py (Django settings for use on Gondor)
            static/ (see README in directory)
            templates/ (where templates for your project goes)
            urls.py
            wsgi.py (WSGI entry point for Django)
        requirements.txt (pip file to declare dependencies)

