# flaskcookiecutter_demo_app

Cookiecutter template for flask restful, including blueprints, application factory, and more


## Introduction

This cookie cutter is a very simple for starting a REST api using Flask, flask-restful, marshmallow, SQLAlchemy and jwt.
It comes with basic project structure and configuration, including Login and registration APIs, application factory and basics unit tests.

Features

* Simple flask application using application factory,
* Authentication using [Flask-JWT-Extended](http://flask-jwt-extended.readthedocs.io/en/latest/) including access token and refresh token management
* Unit tests using pytest and factoryboy
* Configuration using environment variables

Used packages :

* [Flask](http://flask.pocoo.org/)
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/)
* [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* [Flask-JWT-Extended](http://flask-jwt-extended.readthedocs.io/en/latest/)
* [marshmallow-sqlalchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)
* [pytest](https://docs.pytest.org/en/latest/)
* [factoryboy](http://factoryboy.readthedocs.io/en/latest/)



## Usage

* [Installation](#installation)
* [Configuration](#configuration)
* [Authentication](#athentication)
* [Using Docker](#using-docker)


### Installation

#### Install cookiecutter

Make sure you have cookiecutter installed in your local machine.

You can install it using this command : `pip install cookiecutter`

#### Create your project

Starting a new project is as easy as running this command at the command line. No need to create a directory first, the cookiecutter will do it for you.

To create a project run the following command and follow the prompt

`cookiecutter https://github.com/jcarpenterdeqode/flaskcookiecutter_demo_app.git`

#### Using docker

cd myproject

`docker-compose build`

`docker-compose up`
### if server not running than again run 
`docker-compose up`

Your app is running in port 5000 in local machine.

#### Using application

we have 2 urls for login and registration of user:

## http://127.0.0.1:5000/api/auth/register/

Schema :

{
    "username" : "testuser",
    "email" : "test@gmail.com",
    "password" : "Test@123"
}

## http://127.0.0.1:5000/api/auth/login/

Schema :

{
    "email" : "test@gmail.com",
    "password" : "Test@123"
}



