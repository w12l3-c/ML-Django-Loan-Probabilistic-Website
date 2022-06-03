# README
This project is made from machine learning model and python package Django to make it a web service.
It is created as a school project.

## Model
It is a Machine Learning Model that predicts whether a user is a safe or risky borrower.

## Installing packages
To install all the required python packages for the computer to run, you can run the following code in your coding environment terminal.
`$pip install -r requirements.txt`
<br><br>
Some necessary files:
- Django
- Django Rest Framework
- Django Allauth
- sklearn
- numpy
- pandas

## To run the project
To run the project
- First create a directory and fork all the files into that directory
- then open your terminal
- cd to the directory you just made
- then in terminal, run `$python3 manage.py runserver`
- it will pop out a hyperlink that said `http://127.0.0.1:8000/` and clicking on it will take you to the website on local host.

## Directories
- Static
  - Static files holds all the css, javascript, and images
  - It is accessed by most of the htmls in the repository
- mlearn
  - It is the center file in django where you create the settings for the website and the routing of the website
- products
  - It is the model of the machine learning and contains all the files related to it
    - HTMLs
    - Models
    - Serializers
    - Forms
 
