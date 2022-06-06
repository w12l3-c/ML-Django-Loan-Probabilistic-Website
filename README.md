# README
This project is made from machine learning model and python package Django to make it a web service. The objective is to let the user input some of their finacial information and the model will determine their status as safe or risky for loan application.<br><br>
It is created as a school project and it will not serve any commerical purpose

## Model
A logistic regression model that uses various inputted features like user income, debt ratio, credit score, delinquency rate, etc. to predict if a bank will classify them as a safe or risky borrower. This model is realtively general and doesn't predict if a user will receive a particular loan for a particular amount from the bank. Instead, it serves a broader and arguably more important purpose - it tells the user how the bank assesses risk by giving them any loan. For instance, if they are predicted to be a risky borrower, they should expect to pay higher interest rates and have more loan applications turned down.

## Django
Django is a Python Web Framework that can use python languages to build APIs, it is one of the most used python web framework along with Flask. It is also has a lot of other extension frameworks that help different aspects of development<br>
For more information: [django official website](https://www.djangoproject.com/)

## Installing packages
To install all the required python packages for the computer to run, you can run the following code in your coding environment terminal.<br>
`$pip install -r requirements.txt`
<br><br>
Some necessary packages:
- Django
- Django Rest Framework
- Django Allauth
- sklearn
- numpy
- pandas

## To run the project
Procedure:
1. First create a directory and fork all the files into that directory
2. Open your terminal/window prompt either in IDE or Computer
3. Move to the directory you just made by `cd #name_of_the_file`
4. Run ```dir``` in windows or ```ls``` in MacOS or ```-lh``` in Linux to make sure `manage.py` file is in that directory
5. Run `$python3 manage.py runserver`
6. It will pop out a hyperlink that said `http://127.0.0.1:8000/` and clicking on it will take you to the website on local host.

## Directories
- static
  - Static directory holds all the css, javascript, and images
  - It is accessed by most of the htmls in the repository
- mlearn
  - It is the center file in django where you create the settings for the website and the routing of the website
- products
  - It is the model of the machine learning and contains all the files related to it
    - HTMLs
    - Models
    - Serializers
    - Forms
- templates
  - It holds other html templates except from the ones in product
 
 ## User Guide
 Please go to the Wiki page of this repository
