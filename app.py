from flask import Flask, render_template, request, redirect, abort    

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
    return render_template("pokemons.html", pokemons=pokemons)

@app.route("/<name>", methods=["GET"])
def pokemon(name):
    for p in pokemons:
        if (p["name"] == name):
            return render_template("pokemon.html", pokemon=p)
    return render_template("not_found.html")

@app.route("/createPokemon", methods=["GET"])
def createForm():
    return render_template("create_pokemon.html")

@app.route("/extractFormData", methods=["POST"])
def extractForm():
    n = request.form["name"]
    w = request.form["weight"]
    h = request.form["height"]
    i = request.form["img"]
    if (n != "" and w != "" and h != "" and i != ""):
        pokemons.append({ "name": n, "weight": w, "height": h, "img": i })
        return redirect("/")
    else:
        abort(400) # Bad Request
    