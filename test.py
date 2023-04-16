import requests
import json

URL = "http://127.0.0.1:8000/score_prediction/"

data = {
        'venue' : 'Holkar Cricket Stadium',
        'batting_team' : 'CSK',
        'bowling_team' : 'MI',
        'run_left' : 121,
        'ball_left' : 95,
        'wicket_left' : 6, 
        'current_runrate' : 8
    }

json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)

data = r.json()
print(data)