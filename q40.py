app = Flask(__name__)
@app.route('/form', methods=['GET'])
def show_form():
    return render_template('form.html')
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Process the data (e.g., save to database, perform calculations)
        # Here you can add your logic to process the form data
        
        return f'Form submitted successfully! Name: {name}, Email: {email}'
if __name__ == '__main__':
    app.run(debug=True)
