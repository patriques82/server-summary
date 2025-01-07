import unittest
from app import app

class TestPokemonApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Name: mewtoo, Weight: 122.0, Height: 2.0",
            response.data.decode("utf-8")
        )
        self.assertIn(
            "Name: lugia, Weight: 216, Height: 5.2",
            response.data.decode("utf-8")
        )
    
    def test_create_pokemon(self):
        response = self.app.get("/createPokemon")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<form action="/extractFormData" method="POST">',
            response.data.decode("utf-8")
        )
    
    def test_extract_form_happy(self):
        response = self.app.post("/extractFormData", data={
            "name": "tyrinatar",
            "weight": 202,
            "height": 2,
            "img": "https://img.pokemondb.net/artwork/large/tyranitar.jpg"
        })
        self.assertEqual(response.status_code, 302)

    def test_extract_form_unhappy(self):
        response = self.app.post("/extractFormData", data={
            "name": "",
            "weight": "",
            "height": "",
            "img": ""
        })
        self.assertEqual(response.status_code, 400)