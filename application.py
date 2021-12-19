## flask imports
from flask import Flask
from AI import _is_string_spam
from flask import Response, request, jsonify, render_template, url_for
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
    result = _is_string_spam(email)
    return result