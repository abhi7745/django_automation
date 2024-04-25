import sys
import os
import webbrowser
from path import BASE_DIR
import platform, shutil, subprocess

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
                    # os.chdir(base_dir + project_name + '\\venv\\scripts')
                    # os.system('activate')
                    # os.chdir(os.path.join(base_dir, project_name, 'venv', 'Scripts'))
                    # installing django in virtual environment
                    # subprocess.run('activate && pip install django', shell=True, check=True)
                    activate_script = os.path.join(base_dir, project_name, 'venv', 'Scripts', 'activate')
                    # Activate the virtual environment and install Django
                    subprocess.run(f'"{activate_script}" && pip install django', shell=True, check=True)
                    

                # elif system == "Linux":
                #     print(system)
                #     os.chdir(base_dir + project_name)
                #     # os.system('source venv/bin/activate')
                #     # os.system('pip install django')
                #     activate_script = os.path.join('venv', 'bin', 'activate')
                #     subprocess.run(['bash', '-c', f'source {activate_script} && pip install django'], check=True)
                #     print(os.getcwd())
                    

                # elif system == "Darwin":
                #     os.chdir(base_dir + project_name)
                #     subprocess.call(['source', 'venv/bin/activate'], shell=True)

                # elif system == "Linux" or system == "Darwin":
                #     activate_script = os.path.join(base_dir, project_name, 'venv', 'bin', 'activate')
                #     # installing django in virtual environment
                #     subprocess.run(f'. {activate_script} && pip install django', shell=True, check=True)
                    

                elif system == "Linux" or system == "Darwin":
                    activate_script = os.path.join(base_dir, project_name, 'venv', 'bin', 'activate')
                    # Install Django within the virtual environment
                    subprocess.run(f'bash -c "source {activate_script} && pip install django"', shell=True, check=True)
                
                
                # Change directory to the project directory
                os.chdir(os.path.join(base_dir, project_name))

                # Run django-admin startproject command within the activated virtual environment
                subprocess.run(f'bash -c "source {activate_script} && django-admin startproject {project_name} ."', shell=True, check=True)

                # Importing settings_rewriter from utils module
                from utils.settings_writter import settings_rewriter, static_writer, database_configure

                # Running python manage.py startapp command within the activated virtual environment
                # print('length or apps: ############# ',len(apps))
                if len(apps) > 0:
                    for app in apps[::-1]:
                        subprocess.run(f'bash -c "source {activate_script} && python manage.py startapp {app}"', shell=True, check=True)
                        if system == "Linux" or system == "Darwin":
                            settings_rewriter(os.path.join(base_dir, project_name, project_name, 'settings.py'), app)
                
                static_writer(os.path.join(base_dir, project_name, project_name, 'settings.py'))

                # Create static and template directories
                os.mkdir('static')
                os.mkdir('template')

                # Run the Django development server within the activated virtual environment
                subprocess.run(f'bash -c "source {activate_script} && python manage.py migrate && python manage.py runserver"', shell=True)

                
                # os.chdir(base_dir + project_name)
                # os.system('pip install django')
                # # django-admin startproject sample .
                # os.system('django-admin startproject ' + project_name + ' .')
                # # os.chdir(base_dir + project_name + '//' + project_name)

                # from utils.settings_writter import settings_rewriter
                # if len(apps) > 0:
                #     for app in apps[::-1]:
                #         os.system(f'python manage.py startapp {app}') # creating a new app in django project
                #         if system == "Linux":
                #             # os.chdir(base_dir + project_name)
                #             # os.system('source venv/bin/activate')
                #             settings_rewriter(base_dir + project_name + '/' + project_name + '/settings.py', app)

                # os.mkdir('static') # creating a static folder for css,js,images, etc...
                # os.mkdir('template') # creating a template folder for handling frondend files like html


                # # input('Please select you database: enter (m) for mysql, (p) for postgresql, (m) for mongo db')

                # os.system('python manage.py migrate') # running the server
                # os.system('python manage.py runserver') # running the server

                # webbrowser.open('http://127.0.0.1:8000/') # autoload on default browser

            except FileExistsError:
                print(f'{project_name} folder already exits.')
        else:
            print("Unsupported operating system")
    else:
        print(f"Project 'name' required,\nplease follow these format 'python create.py <project_name>' ")


else:
    print('Please set BASE_DIR in path.py file and run the script again')



