# FSND_Capstone_Casting_Agency
Fullstack Nanodegree Final Project - Casting Agency

# Casting Agency
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

No frontend developed yet, only server side.

Application hosted on Heroku 

https://hana-capstone.herokuapp.com

# Motivation
This project to show my learning journey during this nanodegree

1.  Database with  **postgres**  and  **sqlalchemy**  (`models.py`)
2.  API  with  **Flask**  (`app.py`)
3.  TDD  **Unittest**  (`test_app.py`)
4.  Authorization &  Authentification **Auth0**  (`auth.py`)
5.  Deployment on  **`Heroku`**



## Working with the application locally
Make sure you have [python 3](https://www.python.org/downloads/) or later installed
1. **Clone The Repo**
    ```bash
    git clone https://github.com/HanaAlklayah/FSND_CapstoneCastingAgency.git
    ```
2. **Set up a virtual environment**:
    ```bash
    virtualenv env
    source env/Scripts/activate # for Windows
    source env/bin/activate # for MacOs/Linux
    ```
3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt # for Windows/Linux
    pip3 install -r requirements.txt # for MacOs
    ```
4. **Export Environment Variables**

    Refer to the `setup.sh` file and export the environment variables for the project.

5. **Create Local Database**:

    Create a local database and export the database URI as an environment variable with the key `DATABASE_URL`.

6. **Run Database Migrations**:
    ```bash
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    ```

7. **Run the Flask Application locally**:
    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run

    # if using CMD in Windows

    set FLASK_APP=app.py
    set FLASK_ENV=development
    flask run
    ``` 

## Testing
To run the tests, run
```bash
dropdb capstone
createdb capstone
python test_app.py # if running locally
```

## API Reference
### Getting Started
* Base URL: Currently this application is only hosted locally. The backend is hosted at `https://hana-capstone.herokuapp.com/`

* Authentication: This application use Auth0 service

* Use this link to get new token [Get Token](https://ihana.us.auth0.com/authorize?audience=capstone1&response_type=token&client_id=msQq1qKHWVlCqV93c2W71ZvXjZuPlRfl&redirect_uri=https://localhost:8080/login-results) 

Users in this application are:

* Assistant : Can view actors and movies
    * Email: CapstoneCastingAssistant@gmail.com
    * Password: Capstone1!
* Director : Assistant Access + CURD on actors + Modify movies
    * Email: CapstoneCastingDirector@gmail.com
    * Password: Capstone1!
* Executive: Full Access
    * Email: Capstone@gmail.com
    * Password: Capstone1!



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

### Endpoints

#### GET /actors

* General: Return list of actors in Database
* Sample: `curl --location --request GET 'localhost:8080/actors' \
--header 'Authorization: Bearer PRODUCER_TOKEN'`<br>
    ```bash
    {
        "actors": [
            {
            "age": 25, 
            "gender": "Female", 
            "id": 2, 
            "name": "Actor 2"
            }, 
            {
            "age": 30, 
            "gender": "Male", 
            "id": 3, 
            "name": "Actor 3"
            }
        ], 
        "success": true
    }
    ```
#### GET /movies

* General: Return list of movies in Database
* Sample: `curl --location --request GET 'localhost:8080/movies' \
--header 'Authorization: Bearer PRODUCER_TOKEN'`<br>
    ```bash
    {
        "movies": [
            {
            "id": 2, 
            "release_date": "Mon, 08 Mar 2021 00:00:00 GMT", 
            "title": "Movie 2"
            }, 
            {
            "id": 3, 
            "release_date": "Tue, 09 Mar 2021 00:00:00 GMT", 
            "title": "Movie 3"
            }, 
            {
            "id": 4, 
            "release_date": "Wed, 10 Mar 2021 00:00:00 GMT", 
            "title": "Movie 4"
            }, 
            {
            "id": 5, 
            "release_date": "Thu, 11 Mar 2021 00:00:00 GMT", 
            "title": "Movie 5"
            }
            ], 
        "success": true
    }
    ```
#### POST /actors

* General:
    * Create actor using JSON Request Body
    * Return ID of created actor
* Sample: `curl -X POST 'localhost:8080/actors' \
-H 'Authorization: Bearer PRODUCER_TOKEN' \ 
-H 'Content-Type: application/json' \
--data-raw '{ 
     "name":"Actor 4", 
     "age": 23, 
     "gender": "Female"
    }'`
        ```bash
        {
           "actor": {
                "age": 23,
                "gender": "Female",
                "id": 4,
                "name": "Actor 4"
            },
            "success": true
        }
        ```

#### POST /movies

* General:
    * Create movie using JSON Request Body
    * Return ID of created movie
* Sample: `curl -X POST 'localhost:8080/movies' \
-H 'Authorization: Bearer PRODUCER_TOKEN' \
-H 'Content-Type: application/json' \
--data-raw '{
    "release_date":"Mon, 08 Mar 2021 00:00:00 GMT",
    "title": "Movie 2"}'`
        ```bash
        {
            "movie": {
                "id": 6, 
                "release_date": "Mon, 08 Mar 2021 00:00:00 GMT", 
                "title": "Movie 2"
            }, 
            "success": true
        }
        ```
#### PATCH /actors/<actor_id>

* General:
    * Modify actor given id in URL provided the information to update
* Sample: `curl -X PATCH 'localhost:8080/actors/2' \
-H 'Authorization: Bearer PRODUCER_TOKEN' \
-H 'Content-Type: application/json' \
--data-raw '{
    "name" : "Actor 2",
    "age" : 25
}'`

        {
            "actor": {
                "age": 25,
                "gender": "Female",
                "id": 2,
                "name": "Actor 2"
            },
            "success": true
        }
#### PATCH /movies/<movie_id>

* General:
    * Modify movie given id in URL provided the information to update
* Sample: `curl -X PATCH 'localhost:8080/movies/2' \
-H 'Authorization: Bearer PRODUCER_TOKEN' \
-H 'Content-Type: application/json' \
--data-raw '{
    "title":"New Movie",
    "release_date":"Mon, 08 Mar 2021 00:00:00 GMT"
}'`

#### DELETE /actors/<actor_id>

* General: Delete an actor given id in URL
* Sample: `curl -X DELETE 'localhost:8080/actors/1' \
-H 'Authorization: Bearer PRODUCER_TOKEN'`

        {
            "deleted_id": 1,
            "success": true
        }

#### DELETE /movies/<movie_id>

* General: Delete movie given id in URL
* Sample: `curl -X DELETE 'localhost:8080/movies/1' \
-H 'Authorization: Bearer PRODUCER_TOKEN'`

        {
            "deleted_id": 1,
            "success": true
        }