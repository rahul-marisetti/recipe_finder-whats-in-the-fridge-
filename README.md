# recipe_finder-whats-in-the-fridge-

# recipe_finder-whats-in-the-fridge-

# 🧑‍🍳 What's in the Fridge?

**What's in the Fridge?** is a smart recipe finder that helps you cook delicious meals using ingredients you already have. Just enter the items in your fridge, and the app will suggest a variety of recipes using the Spoonacular API.

## 🚀 Features

- Enter one or more ingredients and get matching recipes.
- View recipe names, images, and used/missed ingredients.
- Simple, elegant, and responsive UI built with Streamlit.
- No need to sign up — just search and start cooking!

## 🧪 How It Works

1. Enter ingredients separated by commas (e.g. `tomato, onion, cheese`)
2. The app queries the Spoonacular Recipe API
3. Matching recipes are displayed with useful details

## ⚙️ Installation

```bash
git clone https://github.com/rahul-marisetti/recipe_finder-whats-in-the-fridge-.git
cd recipe_finder-whats-in-the-fridge-
pip install -r requirements.txt
streamlit run app.py


This app uses the free version of the Spoonacular API, which allows a limited number of requests per day. To ensure smooth usage, avoid excessive or repeated searches in a short time span.

For extended usage, consider generating your own API key via Spoonacular's official site("https://spoonacular.com/food-api").
