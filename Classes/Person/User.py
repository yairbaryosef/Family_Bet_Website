import json
class User:
 def __init__(self, username, password):
  self.username = username
  self.password = password
  self.name = "name"
  self.profile = "None"
  self.predictors = []
  self.tournaments_id = []
  self.count_tours = 0
  self.tournaments_id = []


 def get_name(self):
    return self.name

 def get_predictors(self):
    return self.predictors

 def get_username(self):
    return self.username

 def get_password(self):
    return self.password

 def get_tournaments_id(self):
    return self.tournaments_id

 def set_name(self, name):
    self.name = name

 def add_tournament(self, tournament):
    self.tournaments_id.append(tournament)

 def get_profile(self):
    return self.profile

 def set_password(self, password):
    self.password = password

 def set_profile(self, profile):
    self.profile = profile

 def get_count_tours(self):
    return self.count_tours

 def set_count_tours(self, count_tours):
    self.count_tours = count_tours

 def default(self, obj):
        if isinstance(obj, User):
            return {
                "username": obj.username,
                "password": obj.password,
                "name": obj.name,
                "profile": obj.profile,
                "predictors": obj.predictors,
                "tournaments_id": obj.tournaments_id,
                "count_tours": obj.count_tours
            }
        return json.JSONEncoder.default(self, obj)
