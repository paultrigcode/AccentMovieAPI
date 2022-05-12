# AccentDesign Python Recruitment Test Solution

This is the recruitment test solution for the position of Python Developer at Accent to develop a basic movie database interacting with an external API. 


## Installation

The project can be installed using a virtual environment

## Virtual Env Requirements

- Python3.9.0

## Virtual Environment Installation
Creation of virtual environment was done using Venv.

## Create env file
as seen in .envexample , create a .env file and your IMDB API_KEY

## Setting Up The Project

TO set up the project, run the following command

- `git clone https://github.com/paultrigcode/AccentMovieAPI.git`
- `cd  into_the_project_folder`
- `python3 -m venv env`
- `python manage.py migrate`
- `python manage.py runserver`


After you are done with the installation, you should be able to access the API documentation at `http:127.0.0.1:8000/swagger`.

## Tech Stack

- Python
- Django
- Django Rest Framework
- Swagger UI
- Venv
- SQLite

## Justification For Using SQLite DB

1) SQLite is serverless as it doesn't need a different server process or system to operate.
2) SQLite is a cross-platform DBMS that can run on all platforms, including macOS, Windows
3) SQLite doesn't require any configuration. It needs no setup or administration and as such it easy to setup and run the project for the purpose of this assessment.

## Test
 To run test run the command below :

- `python manage.py test`
