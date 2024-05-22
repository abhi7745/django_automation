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

## Usage:
### 1. Clone this repository or download the repository to your local machine.

```bash
git clone https://github.com/abhi7745/django_automation.git
```

### 2. Open a terminal or command prompt and navigate to the directory where the create.py script is located.

- Run the following command:

    ```bash
    python create.py <project_name>
    ```

    Replace <project_name> with the desired name for your Django project. Make sure to provide a project name without any spaces

- Example:

    ```bash
    python create.py Ecommerce
    ```

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
  
  - Navigate to the root folder of the script.
  - Locate a file named `path.py` and open it.
  - Set the path location in the `BASE_DIR` variable.
  
    Example configurations:
    
    - For Windows:
      ```python
      BASE_DIR = r"C:/your/path/to/project/folder"
      ```

    - For Linux / Mac:
      ```python
      BASE_DIR = r"/your/path/to/project/folder"
      ```

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

- Your default web browser will open automatically to display the Django project.

### Pro tip:

When executing Python code as "python create.py <projectname>" becomes tedious, follow these pro tips to streamline your workflow with "create <projectname>".

- #### Make the script executable using your normal pip installation:

  - [How to install in "Windows"](https://github.com/abhi7745/django_automation/blob/master/pip_installation_guid_for_windows.md)
  
  - [How to install "Linux and Mac"](https://github.com/abhi7745/django_automation/blob/master/pip_installation_guid_for_linux_mac.md)


### Feedback and Contributions:

Your feedback and contributions are highly appreciated! If you find this project helpful, please consider supporting it in the following ways:

- **Star the Repository:** Show your appreciation by starring the repository.
- **Fork:** Fork the repository to contribute your own enhancements.
- **Share:** Spread the word! Share this repository with your friends and colleagues.

Feel free to customize the script further to meet your specific project requirements. 

Thank you for your support!