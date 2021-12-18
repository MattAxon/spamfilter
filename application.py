## flask imports
from flask import Flask

from flask import Response, request, jsonify, render_template
from flask import url_for
import AI
import json
import os



application = Flask(__name__)



@application.route('/')
def homePage():
    return render_template('index.html')

@application.route('/test', methods=['POST'])
def testEmail():
    newData = request.get_json()
    email = newData['email']
    return 'hi'