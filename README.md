# todo_app_crud

- a simple app that performs only Create-Retrieve-Update-Delete (CRUD) operations ,build using django framework of python.
-  Here we can create his todo list by adding items, crossed off the completed items, delete the completed items .
- Technologies Used :

        1. Python
        2. Django
        3. Bootstrap
        
-   • Set up a virtual environment
    • Install Django
    • Pin your project dependencies
    • Set up a Django project
    • Start a Django app
- Elaborate:

        1.Prepare Your Environment -
           To start your new Django web application, create a new folder and navigate into it.In this folder, you’ll set up a new virtual environment.
          python3 -m venv envname  #sets up a new virtual environment named envname
          source envname/bin/activate   #to activate the virtual environment.If the activation was successful, then you’ll see the name of your virtual environment,(envname), at the beginning of your command prompt. 

        2.Install Django and Pin Your Dependencies
            python3 -m pip install django  or python -m pip install django==version
          python3 -m pip freeze > requirements.txt # can pin your dependencies to make sure that you’re keeping track of which Django version you installed. writes the names and versions of all external Python packages that are currently in your virtual environment to a file called requirements.txt. This file will include the django package and all of its dependencies.
        Keeping a separate virtual environment for every project allows you to work with different versions of Django for different web application projects. Pinning the dependencies with pip freeze enables you to reproduce the environment that you need for the project to work as expected
        3.Set Up a Django Project - 

        django-admin startproject <project-name>   

        Or
        to avoid creating the additional top-level project folder, you can add a dot (.) at the end of the django-admin startproject command

              “ django-admin startproject <projectname> . “

        4. Set up a database and create a user -
          python3 manage.py migrate
          python3 manage.py createsuperuser
          python3 manage.py  runserver

        5. Start a Django App - create a Django app that’ll contain the specific functionality of your web application.
          python manage.py startapp <appname>
            add the app name in the settings.py/INSTALLED_APPS

        6. URL Routing -
          create appname/urls.py and  write a sample views in appname/views.py.Before that create a connection with todo/urls.py with the app’s urls.py file.
        7. Build Templates -
           appname/templates/appname/templatename.html	
        8. Setup database -
            create models for our requirements and run the command:
                python3 manage.py makemigrations
                python3 manage.py migrate
                python3 manage.py  runserver

         9.add styles for the templates .



