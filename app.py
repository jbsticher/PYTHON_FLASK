from flask import Flask
"""
run app from commmand line with: flask --app app run
flask --app app run --debug
"""
app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Yo dude!</h2>'

@app.route('/<name>')
def print_name(name):
    return f'<h3>Hello, {name}!</h3>'.title()

@app.route('/projects/')
def print_result():
    return 'Projects Page'

# if __name__ == ('__main__'):
#     app.run(debug=True)

