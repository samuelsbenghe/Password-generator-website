from flask import Flask, render_template, request
import apps.password_generator as pg

app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('page_index.html', name='Flask')

@app.route('/apps/password_generator', methods=['GET', 'POST'])
def password_generator(name=None):
    if request.method == 'POST':
        number_of_characters = int(request.form['number_of_characters'])
        is_memorable = 'is_memorable' in request.form
        add_numbers = 'add_numbers' in request.form
        add_symbols = 'add_symbols' in request.form

        password = pg.generate_password(number_of_characters=number_of_characters, is_memorable=is_memorable, add_numbers=add_numbers, add_symbols=add_symbols)
        return password
    return render_template('page_password_generator.html')

@app.route('/apps/birthday_reminder')
def birthday_reminder(name=None):
    return render_template('page_birthday_reminder.html')

if __name__ == '__main__':
    app.run(debug=True)