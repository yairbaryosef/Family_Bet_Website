from firebase_admin import credentials, firestore
import firebase_admin
from Classes.Constants import constants
from Classes.Tournamet.Tournament import tournament_to_json_string




#GET THE TOUR BY ITS PATH
def getTour(path):
    json = {
        "type": "service_account",
        "project_id": "family-bet-e1503",
        "private_key_id": "23085a2059ec093843775334972d49cb32745075",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDXhyWuZ7QtlL5C\nFZ2SLI0zA7zLjQ2LGp6f87CqYIlil9iYWfCOWk0bBdogZnrDHGBElQFvFGY5m4db\nCzhNOBVvoLaqYACiNsdEoamJxRKVp1MWkSoDDdNKXxLCn1t9aFkczelc1S3xTCxy\nhBOEP5pJJwarycaqixamhEdSvJElZg24LR8Wn+5Zymc6h/v671CujTJVQvI7EmLC\n17xJ5KvKb1iryBaH4q4HBq79iTGGAu/k7psMsPbYrE5UYzp4ZF50lLmUcnoxCCR8\n/RTlUzd/1YnasCDmCGMMWzcr64cLl6FRf8Jg/LoP0dzJrQAL4Z48D3Mvjq+EBthU\nQGCmKEjzAgMBAAECggEAIv0KdcwvDgvsxmSk7mMeJFnRzzJIWxHeDiBs8ykgfyl1\nx5HTlqsmg6GzvfkfqnH+V36LEOHSZegPlWJLvbls6BttMVkhcTQMWGIYLZ3uZ5jA\nySlAFTvW1mbQcFjswiiWTYdIquyOp0f9mopCHYDdG/gNF1v2d57ZyqbZv0mOafAM\nOUIXoZGrNyE1CdO9vSrP19X3ehbjYOHnwMkWozU53RbNF1Uz7Mk5boWElYBL8vtR\nkcCWk7a2aVOe2FCV+/W/RCEsy8PcHrg8thKeXVUVBZGAFpzzZ3bnZaC+5+NixTj2\ntoB0LWbzW+446cosn0hRhKZxn/UgRzqmXBjMJ0NVxQKBgQDur5FUkh+bPO7bUJnA\nfesvvpcPlriZi7KJt3pdZFkRIatRIuK3yo+zfgvTgxrXLpRjFwk33ZPNPXCQppee\nbuv6vl7cvhm55DdXhlFhGZlXhE57K7MRHtUtcgFNA5SrY5EHjBYTJmIHumWsT3xS\nWXokDH7nQfR0aHop6sTa/G1orwKBgQDnKYirHuqKJ8y3XXALo6Fl2wEGN6fpUs4Q\nkisG2LcsvH0XGHyzuRDJah8ey5tyQ7f1QodpyzivvT+QCvQDtxacq2hwVsk8Zelo\n5OWgCsQQkG1KigUwr1vzIoLGdE3b6RBX5OXjblOZWyvmPNRxXMTTpSsy3m/10xB7\no6QDM4Js/QKBgQCwlvZX8pAtw0QYwKYwUzj4pvKOVv2WpFNgLn36sK5wzU85hSzl\nu5jbvGq1fy8ReuXP9hAc4/NhCo7IhmhwkDJI3iXC/WZ9MMp9F+QHie/4XuvNlwQx\nq3Ue3VT3DKomr1BynAMNAf3PJ+nnNRuOtaJ3H0OYhyR8J3wSnR4twkqUAwKBgCWd\nNIfjt/ZTE5Sit6CtN44DXN9OHxxwROedYTL0AJpe8VvYuDHmYzzi771rFBg7vKtD\n8BTe5JJ0EOu3XI1eNWe43H2rIYOacaiH1nV8SvsHBUGjw8RwRF4Dt5PjSOgHvIkQ\nzfd79E5372S/cTIhDkYCEk1stHsjpQL5Va7PquFhAoGAWlRsG+rfE+EPHVPDQGKH\nejA+k7xsiFqLn0vcZ1KdSO1sUOKfsTRhVfSBBjwNh8aXAEOuULc9hruQUrmil/Ns\n2ZoDACu0tkUHwkDmmnZu1dQEWcX+PYBsAI3qSXkbN9qpcv/ifh1sY76Zy4J+Dfto\nGIXEd8olEBCXFtDaU6J/xVk=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-42je7@family-bet-e1503.iam.gserviceaccount.com",
        "client_id": "102500645201396024637",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-42je7%40family-bet-e1503.iam.gserviceaccount.com"
    }
    cred = credentials.Certificate(json)

    try:
        firebase_app = firebase_admin.get_app()
    except ValueError:
        firebase_app = firebase_admin.initialize_app(cred)

    db = firestore.client()
    s=path
    doc_ref = db.collection('Tournaments').document(s)
    doc_data = doc_ref.get().to_dict()
    t=doc_data
    return t
    # Print the dictionary

#SAVE THE TOUR TO THE PATH
def saveTour(tour):
    json = {
        "type": "service_account",
        "project_id": "family-bet-e1503",
        "private_key_id": "23085a2059ec093843775334972d49cb32745075",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDXhyWuZ7QtlL5C\nFZ2SLI0zA7zLjQ2LGp6f87CqYIlil9iYWfCOWk0bBdogZnrDHGBElQFvFGY5m4db\nCzhNOBVvoLaqYACiNsdEoamJxRKVp1MWkSoDDdNKXxLCn1t9aFkczelc1S3xTCxy\nhBOEP5pJJwarycaqixamhEdSvJElZg24LR8Wn+5Zymc6h/v671CujTJVQvI7EmLC\n17xJ5KvKb1iryBaH4q4HBq79iTGGAu/k7psMsPbYrE5UYzp4ZF50lLmUcnoxCCR8\n/RTlUzd/1YnasCDmCGMMWzcr64cLl6FRf8Jg/LoP0dzJrQAL4Z48D3Mvjq+EBthU\nQGCmKEjzAgMBAAECggEAIv0KdcwvDgvsxmSk7mMeJFnRzzJIWxHeDiBs8ykgfyl1\nx5HTlqsmg6GzvfkfqnH+V36LEOHSZegPlWJLvbls6BttMVkhcTQMWGIYLZ3uZ5jA\nySlAFTvW1mbQcFjswiiWTYdIquyOp0f9mopCHYDdG/gNF1v2d57ZyqbZv0mOafAM\nOUIXoZGrNyE1CdO9vSrP19X3ehbjYOHnwMkWozU53RbNF1Uz7Mk5boWElYBL8vtR\nkcCWk7a2aVOe2FCV+/W/RCEsy8PcHrg8thKeXVUVBZGAFpzzZ3bnZaC+5+NixTj2\ntoB0LWbzW+446cosn0hRhKZxn/UgRzqmXBjMJ0NVxQKBgQDur5FUkh+bPO7bUJnA\nfesvvpcPlriZi7KJt3pdZFkRIatRIuK3yo+zfgvTgxrXLpRjFwk33ZPNPXCQppee\nbuv6vl7cvhm55DdXhlFhGZlXhE57K7MRHtUtcgFNA5SrY5EHjBYTJmIHumWsT3xS\nWXokDH7nQfR0aHop6sTa/G1orwKBgQDnKYirHuqKJ8y3XXALo6Fl2wEGN6fpUs4Q\nkisG2LcsvH0XGHyzuRDJah8ey5tyQ7f1QodpyzivvT+QCvQDtxacq2hwVsk8Zelo\n5OWgCsQQkG1KigUwr1vzIoLGdE3b6RBX5OXjblOZWyvmPNRxXMTTpSsy3m/10xB7\no6QDM4Js/QKBgQCwlvZX8pAtw0QYwKYwUzj4pvKOVv2WpFNgLn36sK5wzU85hSzl\nu5jbvGq1fy8ReuXP9hAc4/NhCo7IhmhwkDJI3iXC/WZ9MMp9F+QHie/4XuvNlwQx\nq3Ue3VT3DKomr1BynAMNAf3PJ+nnNRuOtaJ3H0OYhyR8J3wSnR4twkqUAwKBgCWd\nNIfjt/ZTE5Sit6CtN44DXN9OHxxwROedYTL0AJpe8VvYuDHmYzzi771rFBg7vKtD\n8BTe5JJ0EOu3XI1eNWe43H2rIYOacaiH1nV8SvsHBUGjw8RwRF4Dt5PjSOgHvIkQ\nzfd79E5372S/cTIhDkYCEk1stHsjpQL5Va7PquFhAoGAWlRsG+rfE+EPHVPDQGKH\nejA+k7xsiFqLn0vcZ1KdSO1sUOKfsTRhVfSBBjwNh8aXAEOuULc9hruQUrmil/Ns\n2ZoDACu0tkUHwkDmmnZu1dQEWcX+PYBsAI3qSXkbN9qpcv/ifh1sY76Zy4J+Dfto\nGIXEd8olEBCXFtDaU6J/xVk=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-42je7@family-bet-e1503.iam.gserviceaccount.com",
        "client_id": "102500645201396024637",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-42je7%40family-bet-e1503.iam.gserviceaccount.com"
    }
    cred = credentials.Certificate(json)
    try:
        firebase_app = firebase_admin.get_app()
    except ValueError:
        firebase_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    items=tour
    s= items.country+'_' +items.sport_Type+ '_' + items.dealer +'_' + items.tour_name
    doc_ref = db.collection('Tournaments').document(s)
    data={"Key":s,constants.constants.tournament():tournament_to_json_string(tour)}
    doc_ref.set(data)
    # Print the dictionary

if __name__ == '__main__':
    getTour('c_Basketball_yair_yair')

