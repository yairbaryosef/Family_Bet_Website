# This is a sample Python script.
from flask import Flask
from firebase import Firebase
app=Flask(__name__)

@app.route("/")
def home():
    firebase = Firebase(firebaseConfig)
    return "hello world"

if __name__=="__main__":
    app.run()



firebaseConfig = {
        "apiKey": "AIzaSyCXihpxRXMPb6ZIVb9wl4mvG3IfW_hQKJQ",
        "authDomain": "mula-82f9c.firebaseapp.com",
        "databaseURL": "https://mula-82f9c-default-rtdb.firebaseio.com",
        "projectId": "mula-82f9c",
        "storageBucket": "mula-82f9c.appspot.com",
        "messagingSenderId": "433864646392",
        "appId": "1:433864646392:web:6617de372268f1ed5d650d",
        "measurementId": "G-0V2VDZMBDD"


}