# FSND_Capstone_Casting_Agency
Fullstack Nanodegree Final Project - Casting Agency

# Casting Agency
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

No frontend developed yet, only server side.

Application hosted on Heroku 

https://hana-capstone.herokuapp.com


## Working with the application locally
1. **Install Dependencies**:
    pip3 install -r requirements.txt 
2. **Run the Flask Application locally**:
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run   

## API Reference

### Getting Started
* Base URL: Currently this application is only hosted locally. The backend is hosted at `https://hana-capstone.herokuapp.com/`
* Authentication: This application use Auth0 service

* Use this link to get new token [Get Token](https://ihana.us.auth0.com/authorize?audience=capstone1&response_type=token&client_id=msQq1qKHWVlCqV93c2W71ZvXjZuPlRfl&redirect_uri=https://localhost:8080/login-results)     


### Error Handling

Errors are returned as JSON in the following format:<br>

    {
        "success": False,
        "error": 404,
        "message": "resource not found"
    }

The API will return three types of errors:

* 404 – resource not found
* 422 – unprocessable
* 401 - Unauthorized
* 400 - bad request
* 500 - internal server error
* 403 - Forbidden