from flask import Flask, render_template, request,send_from_directory
from DataBase import Refrences as ref
from DataBase import Files
from Classes.Person.User import User
from Models.User_Activity import User_Activity_

# control register action
def reg():
    if request.method=='POST':

      username = request.form['username']
      password = request.form['password']

      if ref.is_User_Exist(username) or len(username)==0 or len(password)==0 :
        return "user is already exist"
      else:
        user=User(username,password)
        ref.save_User(user)
        return render_template('register.html')

    else:
     return render_template('register.html')

# control entrance action
def entrance_():


    username = request.form['username']
    password = request.form['password']

    if not(ref.is_User_Exist(username)) or len(username) == 0 or len(password) == 0:
        return "user is not exist"
    else:
        Files.write(username)
        return User_Activity_(username)

