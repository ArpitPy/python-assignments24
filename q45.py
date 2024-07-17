from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        # Process form data (e.g., save to database)
        name = form.name.data
        email = form.email.data
        # Example: Print data
        print(f'Name: {name}, Email: {email}')
        return 'Form submitted successfully!'
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
