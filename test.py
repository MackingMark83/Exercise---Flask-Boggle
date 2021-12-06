from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    
        
    def test_homepage(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<button>Enter</button>', html)
    
    def test_find_from(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

    def test_find(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertNotIn('!<td>{{ H }}</td>', html)        


    
    




    
    # TODO -- write tests for every view function / feature!

