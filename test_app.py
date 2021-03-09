import os
import unittest
import json
from app import create_app
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Movies, Actors

'''
Assistant = {
'Content-Type': 'application/json',
'Authorization': os.environ['ASSISTANT_TOKEN']
}
Director = {
'Content-Type': 'application/json',
'Authorization': os.environ['DIRECTOR_TOKEN']
}
Executive = {
'Content-Type': 'application/json',
'Authorization': os.environ['PRODUCER_TOKEN']
}
'''

class CapstoneTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
        
    def tearDown(self):
        pass
    
    # Successful Tests
    def test_get_actors(self):
        res = self.client().get('/actors', headers=Assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(data['actors'], list)
    
    def test_get_movies(self):
        res = self.client().get('/movies', headers=Assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(data['movies'], list)
    
    def test_post_actors(self):
        res = self.client().post('/actors', headers=Director, json={
            "name": "Mohammad",
            "age": "20",
            "gender": "male"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['created_id'], 1)
    
    def test_post_movies(self):
        res = self.client().post('/movies', headers=Executive, json={"title": "The Mud", "release_date": "10/20/2010"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['created_id'], 1)
    
    def test_patch_actors(self):
        res = self.client().patch('/actors/1', headers=Director,
        json={"name": "Malak",})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    
    def test_patch_movies(self):
        res = self.client().patch('/movies/1', headers=Executive, json={"title": "Terminator",})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    
    def test_delete_actors(self):
        res = self.client().delete('/actors/1', headers=Director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted_id'], 1)
    
    def test_delete_movies(self):
        res = self.client().delete('/movies/1', headers=Executive)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted_id'], 1)
    
    # Unsuccessful Tests 
    def test_u_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
    
    def test_u_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        
    def test_u_post_actors(self):
        res = self.client().post('/actors', json={
            "name": "Hana",
            "age": "20",
            "gender": "female"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
    
    def test_u_post_movies(self):
        res = self.client().post('/movies', json={
            "title": "The Mud",
            "release_date": "10/20/2015"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
    
    def test_u_patch_actors(self):
        res = self.client().patch('/actors/1', json={
        "name": "Hana",
        "age": "25",
        "gender": "female" })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
    
    def test_u_patch_movies(self):
        res = self.client().patch('/movies/1', json={
        "title": "The Mud",
        "release_date": "10/20/2010" })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
    
    def test_u_delete_actors(self):
        res = self.client().delete('/actors/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
    
    def test_u_delete_movies(self):
        res = self.client().delete('/movies/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

if __name__ == "__main__":
    unittest.main()