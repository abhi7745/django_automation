import sys
import os
import webbrowser

project_name = sys.argv[1]
# print(project_name)
project_name = project_name.replace(' ', '_')

base_dir = 'H://A_Django//'

try:
    # Creating a new directory
    os.chdir(base_dir) # change directy
    os.mkdir(project_name) # make a directy with user input

    # virtual Environment setup, activtivating , installing django and required libraries etc......
    os.chdir(base_dir + project_name)
    os.system('virtualenv venv')
    os.chdir(base_dir + project_name + '//venv//scripts')
    os.system('activate')
    os.system('pip install django')


    # install django in global in pc
    os.chdir(base_dir + project_name)
    # django-admin startproject sample .
    os.system('django-admin startproject ' + project_name + ' .')
    # os.chdir(base_dir + project_name + '//' + project_name)
    os.system('python manage.py startapp mainapp') # creating a new app in django project
    os.mkdir('static') # creating a static folder for css,js,images, etc...
    os.mkdir('template') # creating a template folder for handling frondend files like html

    os.system('python manage.py runserver') # running the server

    webbrowser.open('http://127.0.0.1:8000/') # autoload on default browser

except FileExistsError:
    print('File already exits.')



