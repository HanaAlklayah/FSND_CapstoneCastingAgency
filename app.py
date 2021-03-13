import os
import json
from flask import (
    Flask, 
    request, 
    abort, 
    jsonify
    )
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import setup_db, Movies, Actors, db
from auth import AuthError, requires_auth
import sys



def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    migrate = Migrate(app, db)
    CORS(app)

    CORS(app, resources={'/': {'origins': '*'}})

    @app.route('/')
    def welcome():
        return 'Welcome to casting agency'

    #----------------- Movies ----------------#

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(self):
        movies = Movies.query.order_by(Movies.id).all()
        formatted_movies = [movie.format() for movie in movies]

        return jsonify({
            'success': True,
            'movies': formatted_movies
        })

    @app.route('/movies/<int:id>')
    @requires_auth('get:movies')
    def get_movie_by_id(jwt, id):
        movie = Movies.query.get(id)

        if movie is None:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'movie': movie.format(),
            }), 200

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movie(jwt):

        data = request.get_json()
        title = data.get('title', None)
        release_date = data.get('release_date', None)

        if title is None or release_date is None:
            abort(400)

        movie = Movies(title=title, release_date=release_date)

        try:
            movie.insert()
            return jsonify({
                'success': True,
                'movie': movie.format()
            }), 201
        except Exception:
            abort(500)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(self, id):

        try:
            movie = Movies.query.get(id)

            if not movie:
                print(sys.exc_info())
                abort(400)
                
            title = json_data_input('title')
            release_date = json_data_input('release_date')

            movie.title = title
            movie.release_date = release_date

            updated_movie = Movies(title, release_date)

            updated_movie.update()

            return jsonify({
                "success": True,
                "message": "update successfull",
                "movie details changed to ": updated_movie.format()
            })
        except Exception:
            print(sys.exc_info())
            abort(422)

        '''
        body = request.get_json()
        #body = json.dumps(body)

        if body is None:
            abort(422)

        movie = Movies.query.get(id)

        if movie is None:
            abort(404)

        title = body.get('title')
        release_date = body.get('release_date')

        if not title and not release_date:
            abort(422)

        movie.title = title or movie.title
        movie.release_date = release_date or movie.release_date
        movie.update()

        return jsonify({
            'success': True,
            'movie': movie.format()
        })
        '''
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(self, id):
        movie = Movies.query.get(id)

        if movie is None:
            abort(404)

        movie.delete()

        return jsonify({
            'success': True,
            'deleted_id': id
        })

    #--------------- Actors ------------------#

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(self):
        actors = Actors.query.order_by(Actors.id).all()
        formatted_actors = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'actors': formatted_actors
        })

    @app.route('/actors/<int:id>')
    @requires_auth('get:actors')
    def get_actor_by_id(jwt, id):
        actor = Actors.query.get(id)

        if actor is None:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'actor': actor.format(),
            }), 200

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(self):
        data = request.get_json()
        name = data.get('name', None)
        age = data.get('age', None)
        gender = data.get('gender', None)

        if name is None or age is None or gender:
            abort(400)

        actor = Actors(name=name, age=age, gender=gender)

        try:
            actor.insert()
            return jsonify({
                'success': True,
                'actor': actor.format()
            }), 201
        except Exception:
            abort(500)

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(self, id):
        body = request.get_json()

        if body is None:
            abort(422)

        actor = Actors.query.get(id)

        if actor is None:
            abort(404)

        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')

        if not name and not age and not gender:
            abort(422)

        actor.name = name or actor.name
        actor.age = age or actor.age
        actor.gender = gender or actor.gender
        actor.update()

        return jsonify({
            'success': True,
            'actor': actor.format()
        })

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(self, id):
        actor = Actors.query.get(id)

        if actor is None:
            abort(404)

        actor.delete()

        return jsonify({
            'success': True,
            'deleted_id': id
        })

    # Error Handling
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    @app.errorhandler(AuthError)
    def handle_auth_error(exception):
        response = jsonify(exception.error)
        response.status_code = exception.status_code
        return response

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
