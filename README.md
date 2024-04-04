# Ecommerce website -Django

# Virtual Environment setup -
* Open terminal or command prompt
* Create virtualenv - `virtualenv venv`
* Activate vietualenv - `source venv/bin/activate`
* Install django - `pip install django`
* Start/Create Project - `django-admin startproject [project_name]`
* Go to the project directory - `cd [project_name]` or `cd ./[project_name]`

# Setup for vercel -
* Inside the `settings.py` file create host by using 
`ALLOWED_HOSTS = ['.vercel.app']`

![](docs/image.png)

* Create a `requirements.txt` file by using `pip freeze > requirements.txt`
* Create a `.json` file. Ex - `vercel.json`

![](docs/image-1.png)

* vercel.json -

![](docs/image-2.png)

* wsgi.py file - 

![alt text](docs/image-3.png)


# Over View# django-ecommerce
# django-ecommerce
