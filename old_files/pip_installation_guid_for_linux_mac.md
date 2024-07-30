# Pip Installation Guide for Linux and macOS

## How to Install the djangoautomaton Package on a Local Machine

### Prerequisites:

Before using this script, ensure that the following prerequisites are met:

- Python is installed on your system.

### Usage:

1. Clone this repository or download the repository to your local machine.

```bash
git clone https://github.com/abhi7745/django_automation.git
```

2. Open a terminal or command prompt and navigate to the directory where the setup.py script is located. Copy and paste the following command into your terminal and press Enter:

```bash
pip install -e .
```

- Depending on your system configuration, you may need to use `pip3` instead of `pip`. If you encounter any issues with `pip`, try using `pip3`

- If you encounter permission errors while running the pip install command, you may need to use sudo:

```bash
sudo pip install -e .
```

- After installation, you can run the script like this: `create <projectname>`

- If `create <projectname>` does not work, close the terminal and open a new one, then try again!


