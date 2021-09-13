# Board games project  
The site provides a catalog of board games with user authorization, comments and likes. There is also an API.  

## Getting Started  
The first thing to do is to clone the repository:  

```sh
$ git clone https://github.com/polina-koval/BG.git 
$ cd BG
```  

Create a virtual environment to install dependencies in and activate it:  

```sh
$ virtualenv venv  
$ source venv/bin/activate
```

Then install the dependencies:  

```sh
(venv)$ pip install -r requirements.txt
```  

There is a file in the repo ".env.example", this file for use in local development. Duplicate this file as .env in the root of the project and update the environment variable SECRET_KEY.  

```sh
$ cp .env.example .env
```

Once pip has finished downloading the dependencies and the variable is updated:  
 
```sh
(venv)$ python manage.py runserver
```  

Navigate to `http://127.0.0.1:8000/catalog` to the website and `http://127.0.0.1:8000` to the API.  

## Built with   
- Django  
- Django Rest Framework