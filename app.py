from flask import Flask, render_template, request, redirect, url_for
import requests
import pandas as pd

app = Flask(__name__)

# Replace with your real API key
API_KEY = "78842db8a6e549c9ad686b183e1387f3"

def get_recipes(ingredients, diet):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": API_KEY,
        "includeIngredients": ingredients,
        "diet": diet if diet != "None" else None,
        "number": 10,
        "addRecipeInformation": True
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("results", [])

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    recipes = []
    if request.method == "POST":
        ingredients = request.form.get("ingredients")
        diet = request.form.get("diet")
        if ingredients:
            recipes = get_recipes(ingredients, diet)
    return render_template("search.html", recipes=recipes)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run(debug=True)
