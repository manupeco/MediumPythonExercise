from flask import Flask
from flask import make_response
from flask import request
from callsupUseCase import sendCallsUp

app = Flask(__name__)

@app.route("/")
def index():
    return 'Index Page'

@app.route('/callsupDoc/', methods=['POST'])
def callsupDoc():    
    #req_data = request.args
    req_data = request.get_json()
    return sendCallsUp(req_data)
    