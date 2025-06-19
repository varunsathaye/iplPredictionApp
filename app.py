import pickle
import streamlit as st
import pandas as pd
st.title('IPL Win Predictor')
teams=['Royal Challengers Bengaluru','Punjab Kings','Delhi Capitals','Mumbai Indians','Kolkata Knight Riders','Rajasthan Royals','Sunrisers Hyderabad','Lucknow Super Giants', 'Gujarat Titans','Chennai Super Kings']
col1,col2= st.columns(2)
cities=['Delhi', 'Mumbai', 'Kolkata', 'Bangalore', 'Jaipur', 'Chennai',
       'Sharjah', 'Chandigarh', 'Dubai', 'Bengaluru', 'Hyderabad', 'Pune',
       'Durban', 'Dharamsala', 'Abu Dhabi', 'Cuttack', 'Navi Mumbai',
       'Visakhapatnam', 'Cape Town', 'Lucknow', 'East London',
       'Kimberley', 'Ahmedabad', 'Centurion', 'Port Elizabeth', 'Nagpur',
       'Mohali', 'Indore', 'Guwahati', 'Raipur', 'Johannesburg', 'Ranchi',
       'Bloemfontein']
pipe=pickle.load(open('pipe.pkl','rb'))
with col1:
    batting_team=st.selectbox('Select the batting side',sorted(teams))
with col2:
    bowling_team=st.selectbox('Select the bowling side',sorted(teams))

city=st.selectbox('Select the homeground city',cities)

target_runs=st.number_input('Target: ')
col3,col4,col5=st.columns(3)

with col3:
    current_runs=st.number_input('Score: ')
with col4:
    overs_bowled=st.number_input('Overs Bowled: ')
with col5:
    wickets=st.number_input('Wickets Lost: ')
if st.button('Predict'):
    runs_left=target_runs-current_runs
    balls_left=120-overs_bowled*6
    wickets_left=10-wickets
    crr=current_runs/overs_bowled
    rrr=(runs_left*6)/balls_left
    input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[city],'runs_left':[runs_left],
                  'balls_left':[balls_left],'wickets_left':[wickets_left],'target_runs':[target_runs],'crr':[crr],'rrr':[rrr]})
    result=pipe.predict_proba(input_df)
    loss=result[0][0]
    win=result[0][1]
    st.header(f'{batting_team}: {round(win*100)} %')
    st.header(f'{bowling_team}: {round(loss * 100)} %')