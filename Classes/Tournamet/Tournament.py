from typing import List, Dict
import json


class Tournament:
    def __init__(self):
        self.dealer = ""
        self.type = ""
        self.country = "c"
        self.sport_Type = "S"
        self.predictors = []
        self.participants = []
        self.predictorHashMap = {}
        self.games = []
        self.league = None
        self.champion_points = 0
        self.champion = ""
        self.score_for_right_bet = 0
        self.score_for_bool_bet = 0
        self.tournament_Id = 0
        self.Winner = None
        self.tour_picture = ""
        self.tour_name = ""
        self.password = ""
        self.picture=""

    def init_tour(self, tournament):
        self.dealer = tournament.dealer
        self.type = tournament.type
        self.predictors = tournament.predictors
        self.participants = tournament.participants
        self.predictorHashMap = tournament.predictorHashMap
        self.games = tournament.games
        self.league = tournament.league
        self.champion_points = tournament.champion_points
        self.champion = tournament.champion
        self.score_for_right_bet = tournament.score_for_right_bet
        self.score_for_bool_bet = tournament.score_for_bool_bet
        self.tournament_Id = tournament.tournament_Id
        self.Winner = tournament.Winner
        self.tour_picture = tournament.tour_picture
        self.tour_name = tournament.tour_name
        self.password = tournament.password

    def get_tour_name(self) -> str:
        return self.tour_name

    def get_password(self) -> str:
        return self.password

    def get_tour_picture(self) -> str:
        return self.tour_picture

    def get_winner(self):
        return self.Winner

    def get_games(self) -> List:
        return self.games

    def get_predictors(self) -> List:
        return self.predictors

    def get_dealer(self) -> str:
        return self.dealer

    def get_tournament_Id(self) -> int:
        return self.tournament_Id

    def get_score_for_bool_bet(self) -> int:
        return self.score_for_bool_bet

    def get_score_for_right_bet(self) -> int:
        return self.score_for_right_bet

    def set_tour_picture(self, tour_picture: str):
        self.tour_picture = tour_picture

    def set_dealer(self, dealer: str):
        self.dealer = dealer

    def set_games(self, games: List):
        self.games = games

    def set_predictors(self, predictors: List):
        self.predictors = predictors

    def set_tournament_Id(self, tournament_Id: int):
        self.tournament_Id = tournament_Id

    def set_score_for_bool_bet(self, score_for_bool_bet: int):
        self.score_for_bool_bet = score_for_bool_bet

    def set_password(self, password: str):
        self.password = password

    def set_score_for_right_bet(self, score_for_right_bet: int):
        self.score_for_right_bet = score_for_right_bet

    def set_tour_name(self, tour_name: str):
        self.tour_name = tour_name

    def set_winner(self, winner):
        self.Winner = winner

    def add_game(self, game):
        self.games.append(game)

    def add_predictor(self, predictor):
        self.predictors.append(predictor)

    def add_participant(self, user):
        self.participants.append(user)

    import json

    def tournament_to_json(tournament):
        return json.dumps(tournament.__dict__)

    @staticmethod
    def json_to_tournament(json_str):
        json_data = json.loads(json_str)
        tournament = Tournament()
        tournament.__dict__.update(json_data)
        return tournament

if __name__ == '__main__':
    true=True
    false=False

def tournament_to_json_string(tournament) -> str:
        return json.dumps(tournament.__dict__)


