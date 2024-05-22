import sys
import os
import webbrowser

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from path import BASE_DIR
import platform, shutil, subprocess
# Importing settings_rewriter from utils module
from utils.settings_writter import settings_rewriter, static_writer


import random
import time
# Loading function
def Loading(value=True):
    loading = ['|||||', '/////', '\\\\\\']
    # loading = ['🌟🌟🌟🌟🌟', '💫💫💫💫💫', '✨✨✨✨✨', '🌈🌈🌈🌈🌈', '🌸🌸🌸🌸🌸', '🌼🌼🌼🌼🌼', '🌞🌞🌞🌞🌞', '🌛🌛🌛🌛🌛', '🌟💫✨💫🌟']
    
    while value:
        random.shuffle(loading)  # Shuffle the loading icons randomly
        for i in loading:
            # print(f'Please wait...{i}', end="\r")
            print(f'\rPlease wait...{i}', end="")
            time.sleep(0.1)
        value = False

def main():

    # projectname Missing from Command Line Arguments - solver
    while True:
        if len(sys.argv) <= 1:
            project_name = input('You missed entering your project name. Please enter it here: ')
            if project_name.strip():
                sys.argv.append(project_name)
                break
            else:
                continue
        else:
            break
    
    global BASE_DIR  # Declare BASE_DIR as a global variable
    # path selection section
    while True:
        project_loc = input("\nPlease select your project directory, enter one of the following options:\n'c' to create the project in the current directory\n'p' to create project with your custom path: ")
        if project_loc.lower() == 'c':
            BASE_DIR = os.path.join(os.getcwd(), '')  # Combine the current working directory with an empty string to append the path separator
            print('BASE_DIR: ', BASE_DIR)
            break

        elif project_loc.lower() == 'p':
            # Create directory and its intermediate directories if they do not exist
            if BASE_DIR.strip():
                os.makedirs(BASE_DIR, exist_ok=True)  # This will create "/path/to/new/directory" along with any intermediate directories
                if not BASE_DIR.endswith(os.path.sep):
                    BASE_DIR = BASE_DIR + os.path.sep
                print('BASE_DIR: ', BASE_DIR)
                break
            else:
                print('Please set BASE_DIR in path.py file and run the script again')
                sys.exit(0)


        else:
            continue

    Loading()
    if BASE_DIR != "":

        if not len(sys.argv) <= 1:
            project_name = sys.argv[1]
            # print(project_name)
            project_name = project_name.replace(' ', '_')
            # apps = sys.argv[2:]

            system = platform.system()
            base_dir = BASE_DIR

            # project folder exist solver section
            if os.path.exists(base_dir + project_name):
                # value = input(f'Project "{project_name}" already exists in the directory. \nPlease enter (y) to delete the folder and create new project, \n(n) to recreate with new project name, \n(e) to exit from program')
                value = input(f'\nThe project named "{project_name}" already exists within the directory, enter one of the options below:\n'
                    f"'d' to delete the folder and create a new project,\n"
                    f"'n' to recreate with a new project name, or\n"
                    f"'e' to exit from the program: ")

                if value.lower() == 'd':
                    Loading()
                    shutil.rmtree(base_dir + project_name)  # Remove directory and its contents
                
                elif value.lower() == 'n':
                    project_name = input("Please enter a new project name: ")
                    project_name = project_name.replace(' ', '_')
                
                elif value.lower() == 'e':
                    print("Your program stoped successfully")
                    sys.exit(0)
                
                else:
                    print("Wrong input you entered")
                    sys.exit(0)
            

            apps = []
            # admin app_name error solver
            while True:
                app_input = input("\nPlease enter your app names separated by space or Press 'Enter' to leave app creation: ")
                if app_input.strip():  # Check if input is not empty or just whitespace
                    app_list = app_input.split()
                    if 'admin' in app_list:
                        exact_admin = False
                        for app in app_list:
                            if app == 'admin':
                                exact_admin = True
                                break
                        if exact_admin:
                            # app_conflict = input('\nThe app name "admin" will conflict with the default Django admin ("django.contrib.admin"). \nDo you want to re-enter the app names again? (y) to continue and (n) to leave app creation: ')
                            app_conflict = input("\nThe app name 'admin' will clash with the default Django admin ('django.contrib.admin'). \nTherefore, you need to modify the name 'admin' to something like 'admin_panel', 'admin_section', 'admin_profile', etc. \nWould you like to enter the app names again? Enter 'y' to continue or 'n' to leave app creation: ")
                            if not app_conflict.strip() or app_conflict.lower() == 'y':
                                continue
                            else:
                                break
                        else:
                            apps = app_list
                            break
                    else:
                        apps = app_list
                        break
                else:
                    break


            print(f'\nCreating your project on "{base_dir}" directory')
            Loading()

            # main project creation section
            if system == "Windows" or system == "Linux" or system == "Darwin":
                try:
                    # Creating a new directory
                    os.chdir(base_dir) # change directy
                    os.mkdir(project_name) # make a directy with user input

                    # virtual Environment setup, activtivating , installing django and required libraries etc......
                    os.chdir(base_dir + project_name)
                    os.system('pip install virtualenv')
                    os.system('virtualenv venv')

                    activate_script = ""
                    # checking which operating system
                    print(system, os.getcwd())
                    if system == "Windows":
                        activate_script = os.path.join(base_dir, project_name, 'venv', 'Scripts', 'activate')
                        Loading()
                        # Activate the virtual environment and install Django
                        subprocess.run(f'"{activate_script}" && pip install django', shell=True, check=True)
                        Loading()
                        subprocess.run(f'django-admin startproject {project_name} .', shell=True, check=True)

                        # Running python manage.py startapp command within the activated virtual environment
                        # print('length or apps: ############# ',len(apps))
                        Loading()
                        if len(apps) > 0:
                            for app in apps[::-1]:
                                subprocess.run(f'python manage.py startapp {app}', shell=True, check=True)
                                settings_rewriter(os.path.join(base_dir, project_name, project_name, 'settings.py'), app)


                    elif system == "Linux" or system == "Darwin":
                        activate_script = os.path.join(base_dir, project_name, 'venv', 'bin', 'activate')
                        # Install Django within the virtual environment
                        Loading()
                        subprocess.run(f'bash -c "source {activate_script} && pip install django"', shell=True, check=True)
                        
                        Loading()
                        # Run django-admin startproject command within the activated virtual environment
                        subprocess.run(f'bash -c "source {activate_script} && django-admin startproject {project_name} ."', shell=True, check=True)


                        # Running python manage.py startapp command within the activated virtual environment
                        # print('length or apps: ############# ',len(apps))
                        Loading()
                        if len(apps) > 0:
                            for app in apps[::-1]:
                                subprocess.run(f'bash -c "source {activate_script} && python manage.py startapp {app}"', shell=True, check=True)
                                settings_rewriter(os.path.join(base_dir, project_name, project_name, 'settings.py'), app)

                    Loading()
                    static_writer(os.path.join(base_dir, project_name, project_name, 'settings.py'))
                    
                    # Change directory to the project directory
                    Loading()
                    os.chdir(os.path.join(base_dir, project_name))

                    # Create static and template directories
                    Loading()
                    os.mkdir('static')
                    os.mkdir('template')

                    # Run the Django development server within the activated virtual environment
                    if system == "Windows":
                        Loading()
                        activate_script = os.path.join(base_dir, project_name, 'venv', 'Scripts', 'activate')
                        # Activate the virtual environment and install Django
                        subprocess.run(f'{activate_script}', shell=True, check=True)
                        subprocess.run(f'python manage.py migrate && python manage.py runserver', shell=True, check=True)

                    elif system == "Linux" or system == "Darwin":
                        Loading()
                        subprocess.run(f'bash -c "source {activate_script} && python manage.py migrate && python manage.py runserver"', shell=True)

                except FileExistsError:
                    print(f'{project_name} folder already exits.')
            else:
                print("Unsupported operating system")
        else:
            print(f"Project 'name' required,\nplease follow these format 'python create.py <project_name>' ")


    else:
        print('Please set BASE_DIR in path.py file and run the script again')

if __name__ == "__main__":
    main()