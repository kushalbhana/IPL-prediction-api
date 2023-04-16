from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import json
import pickle

# Create your views here.
@csrf_exempt
def prediction(request):
    # if request.method == 'POST':

    # Venues for IPL matches
    stadiums= ['Barabati Stadium', 'Brabourne Stadium', 'Buffalo Park',
       'De Beers Diamond Oval', 'Dr DY Patil Sports Academy',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'Dubai International Cricket Stadium', 'Eden Gardens',
       'Feroz Shah Kotla', 'Himachal Pradesh Cricket Association Stadium',
       'Holkar Cricket Stadium', 'JSCA International Stadium Complex',
       'Kingsmead', 'M Chinnaswamy Stadium',
       'MA Chidambaram Stadium, Chepauk', 'New Wanderers Stadium',
       'Newlands', 'OUTsurance Oval',
       'Punjab Cricket Association Stadium, Mohali',
       'Rajiv Gandhi International Stadium, Uppal',
       'Sardar Patel Stadium, Motera', 'Sawai Mansingh Stadium',
       'Shaheed Veer Narayan Singh International Stadium',
       'Sharjah Cricket Stadium', 'Sheikh Zayed Stadium',
       "St George's Park", 'Subrata Roy Sahara Stadium',
       'SuperSport Park', 'Vidarbha Cricket Association Stadium, Jamtha',
       'Wankhede Stadium']
    
    # Data we got from front end
    teams = ['CSK', 'DC', 'KKR', 'MI', 'PBKS', 'RCB', 'RR', 'SRH']
    stadium = stadiums.index('Holkar Cricket Stadium')
    battting_team = teams.index('CSK')
    bowling_team = teams.index('MI')
    run_left= 121
    ball_left= 95
    wicket_left= 6
    current_runrate= 8
    required_runrate= run_left/(ball_left/6)

    # prediction model
    prediction_model_1 = pickle.load(open('C:/Users/kusha/Documents/Hackathon/GFG/casting_api/api/components/models/gb_rr', 'rb'))
    prediction_model_2 = pickle.load(open('C:/Users/kusha/Documents/Hackathon/GFG/casting_api/api/components/models/gb_x', 'rb'))
    prediction_model_3 = pickle.load(open('C:/Users/kusha/Documents/Hackathon/GFG/casting_api/api/components/models/rf_rr', 'rb'))
    prediction_model_4 = pickle.load(open('C:/Users/kusha/Documents/Hackathon/GFG/casting_api/api/components/models/rf_x', 'rb'))

    i=0.3*prediction_model_2.predict_proba([[battting_team, bowling_team, stadium, run_left, ball_left, wicket_left]])+0.7*prediction_model_4.predict_proba([[battting_team, bowling_team, stadium, run_left, ball_left, wicket_left]])
    j=0.3*prediction_model_1.predict_proba([[battting_team, bowling_team, stadium, required_runrate, current_runrate]])+0.7*prediction_model_3.predict_proba([[battting_team, bowling_team, stadium, required_runrate, current_runrate]])
   
    final = 0.6*j+0.4*i
    final_prediction = final*100
    win_prediction = {
        'battting_team' : final_prediction[0][0],
        'bowling_team' : final_prediction[0][1],
    }
    
    json_data = json.dumps(win_prediction)
    return HttpResponse(json_data)



def score_prediction(index):
    prediction_model_1 = pickle.load(open('C:/Users/kusha/Documents/Hackathon/GFG/casting_api/api/components/models/Score_pred', 'rb'))
    new_data = pd.DataFrame({'batting_team': [0], 'bowling_team': [4], 'venue':[12]})
    predicted_score = prediction_model_1.predict(new_data)
    print('Predicted first innings score:', predicted_score)
    return HttpResponse('Score')