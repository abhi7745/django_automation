# Automated Django Project Creation Code:

This repository contains a Python script that automates the process of creating a Django project. It sets up a base project directory, creates a dedicated virtual environment, initializes your Django project with the preferred name, and generates the necessary files and folders for a Django project.


## What the Script Does:

- Sets up a base project directory.
- Creates a dedicated virtual environment.
- Creates your Django project with a preferred name.
- Generates the necessary apps, files and folders for a Django project.
- Run django database migrations
- Automatically run the server in 8000 port

## Prerequisites:

Before using this script, ensure that the following prerequisites are met:

- Python is installed on your system.
-  No need to activate any virtual environment

## Usage:

#### 1. Install the package using pip

```bash
pip install git+https://github.com/abhi7745/django_automation.git#egg=djangoautomation
```

#### 2. After successfully installing the package, you can use it as follows:

- Open a terminal or command prompt (no need to activate any virtual environment) and run the following command:

```bash
create <project_name>
```

Replace <project_name> with the desired name for your Django project. Make sure to provide a project name without any spaces

- Example:

```bash
create Ecommerce
```

If the command is not working, please close the current terminal and open a new one.

### 3. Selecting Project Directory:

You can specify where you want to save the project by providing the path location:

- The script will prompt you with the following message:

    ```
    Please select your project directory and enter one of the following options:
    'c' to create the project in the current directory
    'p' to create project with your custom path: 
    ```

- **Select 'c' :** The script automatically creates the project in your current directory.

- **Select 'p' :** If you choose to specify a custom path:
  
![Path prompt](https://github.com/abhi7745/django_automation/blob/master/images/path_prompt.png)

### 4. Enter your desired apps:

- After that script will prompt you with the following message:
    ```
    Please enter your app names separated by space or Press 'Enter' to leave app creation:
    ```
  
- Example:-
  ```
  Please enter your app names separated by space or Press 'Enter' to leave app creation: Seller Customer Admin_panel
  ```
- Hit enter


### Project Creation process in detail:

- The script will create a base project directory and set up a dedicated virtual environment.

- Django will be installed in the virtual environment, and a new Django project with the specified name will be created.

- Additionally, your preferred apps will be created within the project, and all apps configuration added to the `INSTALLED_APPS` section in the `settings.py` file.

- Two folders, static and template, will be generated in the project directory to handle static files and templates, respectively. Their configurations will be added to the `settings.py` file, and media configuration will also be added.


- The Django development server will be started automatically, and the project will be accessible at http://127.0.0.1:8000/.

- You can now open your default web browser and check at localhost or http://127.0.0.1:8000/.


### Feedback and Contributions:

Your feedback and contributions are highly appreciated! If you find this project helpful, please consider supporting it in the following ways:

- **Star the Repository:** Show your appreciation by starring the repository.
- **Fork:** Fork the repository to contribute your own enhancements.
- **Share:** Spread the word! Share this repository with your friends and colleagues.

Feel free to customize the script further to meet your specific project requirements. 

Thank you for your support!