from flask import Flask, render_template, request
from DataBase import Refrences as ref, FireStore
from Classes.Person.User import User
from datetime import datetime
from DataBase import Files
from Classes.Tournamet.Tournament import Tournament
from Classes.Constants.constants import constants


# User Activity
def User_Activity_(username):
    user = ref.getUser(username)
    list = []
    for tour in user['tournaments_id']:
        try:
            t = FireStore.getTour(tour)
            if t != None:
                tour_ = Tournament.json_to_tournament(t[constants.tournament()])
                if tour_.type == constants.al_league():
                    tour_.picture = '../Images/drawable/al_league.jpg'
                elif tour_.type == constants.winner_league():
                    tour_.picture='../Images/drawable/winner.jpg'
                print(tour_.type)
                list.append(tour_)
        except Exception:
              pass

    return render_template('User_Activity.html', items=list)

def Predictor_Activity(tour):
    user=Files.read()
    if request.method == 'POST':
        away_score = request.form.get('away_score')
        if away_score != '' and away_score is not None:
            card_number = request.form['card_number']
            game=tour.games[int(card_number)-1]
            game['bets'][user]['score_away_team_bet'] = int(away_score)
            # Perform some action with the new text here
            date_obj = datetime.strptime(game['last_date'], "%b %d, %Y %H:%M:%S")
            if date_obj < datetime.now():
                print("The date is in the past")
                game['bets'][user]['score_away_team_bet'] = 0
            else:
                print("The date is in the future")
                FireStore.saveTour(tour)
        else:
            away_score = request.form.get('home_score')
            if away_score!='' and away_score is not None:
                card_number = request.form['card_number']
                game = tour.games[int(card_number) - 1]
                game['bets'][user]['score_home_team_bet'] = int(away_score)
                date_obj = datetime.strptime(game['last_date'], "%b %d, %Y %H:%M:%S")
                if  date_obj< datetime.now():
                    print("The date is in the past")
                    game['bets'][user]['score_home_team_bet'] = 0
                else:
                    print("The date is in the future")
                    FireStore.saveTour(tour)
            else:
                print("save")
            # Perform some action when the form is submitted
            # saveTour(tour_)
    # Check if the date is in the past
    return render_template('Predictor_Activity.html', items=tour,user=user)




