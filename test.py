from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

def test_homepage(self):
    with app.test_client() as client:
        response = self.client.get("/")
        html = res.get_data(as_text=Ture)

        self.assertIn('<td>{{ cell }}</td>', html)





def test_check_word(self):
    with app.test_client() as client:
        self.assertEqual((response.json['result'], 'ok')
)




def test_post_score(self):
    with app.test_client() as client: 
        
        self.client.post(/'post-score',data = {'highscore': 0} )
        self.assertEqual(res.status_code, 200)
        self.assertIn('<input name='word'>', html)        