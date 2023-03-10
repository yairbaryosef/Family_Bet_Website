from firebase_admin import credentials, db
import firebase_admin
from Classes.Constants.constants import constants

cred = credentials.Certificate('DataBase/Firebase.json')
try:
    firebase_app = firebase_admin.get_app()
except ValueError:
    firebase_app = firebase_admin.initialize_app(cred,{
        "databaseURL":"https://family-bet-e1503-default-rtdb.firebaseio.com"
    })

def is_User_Exist(name):
    try:
     db_ref = db.reference().child(constants.get_User(constants)).child(name)
     data = db_ref.get()
     return data!=None
    except Exception:
        return False
def save_User(user):
    db_ref = db.reference().child(constants.get_User(constants)).child(user.username)

    data = db_ref.set(user.default(user))

def getUser(name):
    try:
      db_ref = db.reference().child(constants.get_User(constants)).child(name)
      data = db_ref.get()
      return data
    except Exception:
        return None