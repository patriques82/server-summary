from flask import Flask

pokemons = [
    { "name": "pikachu", "height": 0.4, "weight": 6.0, "img": "https://img.pokemondb.net/artwork/large/pikachu.jpg"  },
    { "name": "mewtoo", "height": 2.0, "weight": 122.0, "img": "https://img.pokemondb.net/artwork/large/mewtwo.jpg"  }, 
    { "name": "bulbasaur", "height": 0.7, "weight": 6.9, "img": "https://img.pokemondb.net/artwork/large/bulbasaur.jpg"  },
    { "name": "lugia", "height": 5.2, "weight": 216, "img": "https://img.pokemondb.net/artwork/large/lugia.jpg" }
]

app = Flask(__name__)

# / -> show all pokemons
# /Pikachu -> show specific pokemon (delete pokemon)
# /create -> display form to create pokemon

@app.route("/", methods=["GET"])
def index():
    return pokemons

@app.route("/<name>", methods=["GET"])
def pokemon(name):
    for p in pokemons:
        if (p["name"] == name):
            return p
    return "Not Found"

@app.route("/createPokemon", methods=["GET"])
def createForm():
    return "Create form"

app.run(debug = True)