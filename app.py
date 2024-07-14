from flask import Flask, render_template, request
import apps.password_generator as pg

app = Flask(__name__)

APPS_PREFIX = '/apps'

@app.route('/')
def index(name=None):
    return render_template('page_index.html', name='Flask')

@app.route(APPS_PREFIX+'/password_generator', methods=['GET', 'POST'])
def password_generator():
    if request.method == 'POST':
        # Get data that user entered in the frontend form
        number_of_characters = int(request.form['number_of_characters'])
        is_memorable = 'is_memorable' in request.form
        add_numbers = 'add_numbers' in request.form
        add_symbols = 'add_symbols' in request.form

        # Generate password using password_generator.py
        password = pg.generate_password(number_of_characters=number_of_characters, is_memorable=is_memorable, add_numbers=add_numbers, add_symbols=add_symbols)
        # Return the password to the frontend
        return password
    # Everything here is "GET"
    return render_template('page_password_generator.html')

@app.route(APPS_PREFIX+'/recipe_book', methods=['GET', 'POST'])
def recipe_book():
    if request.method == 'POST':
        return "nothing here yet"
    # Everything here is "GET"
    return render_template('page_recipe_book.html')



if __name__ == '__main__':
    app.run(debug=True)