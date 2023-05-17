# Automated Django Project Creation Code

This repository contains a Python script that automates the process of creating a Django project. It sets up a base project directory, creates a dedicated virtual environment, and generates the necessary files and folders for a Django project.

## Prerequisites

- Before using this script, ensure that the following prerequisites are met:

- Python is installed on your system.
- virtualenv is installed. If not, you can install it using the following command:

```bash 
    pip install virtualenv 
```


## Usage
1. Clone this repository or copy the script to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the following command:

```bash
    python create_project_setup.py <project_name>
```

Replace <project_name> with the desired name for your Django project. Make sure to provide a project name without any spaces.

4. The script will create a base project directory and set up a dedicated virtual environment.

5. Django will be installed in the virtual environment, and a new Django project with the specified name will be created.

6. Additionally, a new Django app named "mainapp" will be created within the project.

7. Two folders, static and template, will be generated in the project directory to handle static files and templates, respectively.

8. The Django development server will be started automatically, and the project will be accessible at http://127.0.0.1:8000/.

9. Your default web browser will open automatically to display the Django project.


## Note
- If the specified project name or directory already exists, the script will display a "File already exists" message and terminate without making any changes.

- Make sure to modify the base_dir variable in the script to specify the desired base directory for your Django projects.

- Feel free to customize the script further to meet your specific project requirements.