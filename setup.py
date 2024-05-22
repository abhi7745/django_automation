# setup.py

from setuptools import setup, find_packages

setup(
    name='djangoautomation',
    version='0.1',
    author='Abhijith KR',
    author_email='abhijithkr.com@gmail.com',
    url='https://github.com/abhi7745/django_automation.git',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'create=build.create:main',
        ],
    },
)