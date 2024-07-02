
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Capture user input from the form
    family_size = request.form.get('family_size')
    budget = request.form.get('budget')
    dietary_restrictions = request.form.get('dietary_restrictions')

    # Process the input to generate a tailored shopping list
    shopping_list = []

    # Redirect to the shopping list page, passing the shopping list data
    return render_template('shopping_list.html', shopping_list=shopping_list)

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

if __name__ == '__main__':
    app.run(debug=True)
