from flask import Flask, render_template, request,send_from_directory
from flask_cors import CORS
from DataBase import Refrences, Files
from Models.register import reg,entrance_
from DataBase.FireStore import getTour,saveTour
from Classes.Constants.constants import constants
from Classes.Tournamet.Tournament import Tournament
from Models.User_Activity import Predictor_Activity
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    try:
     user=Files.read();
     return render_template('main.html',user=user)
    except Exception:
     return render_template('main.html', user="user")
@app.route('/card/<item_id>', methods=['GET', 'POST'])
def show_item(item_id):
    t = getTour(item_id)
    tour_ = Tournament.json_to_tournament(t[constants.tournament()])
    return Predictor_Activity(tour_)
@app.route('/sendText', methods=['POST'])
def send_text():
    text = request.form['text']
    print('Text changed to:', text)
    # Perform some action with the new text
    return 'OK'
@app.route('/Images/<path:path>')
def send_image(path):
    return send_from_directory('Images', path)

@app.route('/entrance',methods=['GET', 'POST'])
def entrance():
    # Insert your code to handle the entrance button click here
    return entrance_()

@app.route('/register',methods=['GET', 'POST'])
def register():
    # Insert your code to handle the entrance button click here
    return reg()

@app.route('/register',methods=['GET', 'POST'])
def register2():
    # Insert your code to handle the entrance button click here
    Refrences.is_User_Exist()
    return reg()


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Code for user login
    return 'Login successful'



if __name__ == '__main__':
    app.run('0.0.0.0',port=80,debug=True)
