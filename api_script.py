from flask import Flask

#Create a Flask object
app = Flask(__name__)

#File location for a read_me file
@app.route('/read_me')
def read_me():
        return 'Some placeholder text'

#Placeholder for the location of data
@app.route('/data/')
def data_output():
        return 'example data placeholder'