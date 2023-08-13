import dash
import dash_core_components as dcc
import dash_html_components as html
import pymongo
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import seaborn as sns
from plotly.subplots import make_subplots
import numpy as np


# Connecting to the MongoDB and to fetch data relevant to each collection 
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["AnalyzingDataset"]

overs_collection_pak = db["OVERSPAK18"]
wickets_collection_pak = db["WICKETSPAK18"]
average_collection_pak = db["AVERAGEPAK18"]
economy_collection_pak = db["ECONOMYPAK18"]
strike_rate_collection_pak = db["STRIKERATEPAK18"]
dot_balls_collection_pak = db["DOTBALLSPAK18"]
runs_given_collection_pak = db["RUNSGIVENPAK18"]


overs_collection_eng = db["OVERSENG18"]
wickets_collection_eng = db["WICKETSENG18"]
average_collection_eng = db["AVERAGEENG18"]
economy_collection_eng = db["ECONOMYENG18"]
strike_rate_collection_eng=db["STRIKERATEENG18"]
dot_balls_collections_eng = db["DOTBALLSENG18"]
runs_given_collection_eng = db["RUNSGIVENENG18"]


overs_collection_ban = db["OVERSBAN19"]
wickets_collection_ban = db["WICKETSBAN19"]
average_collection_ban = db["AVERAGEBAN19"]
economy_collection_ban = db["ECONOMYBAN19"]
strike_rate_collection_ban=db["STRIKERATEBAN19"]
dot_balls_collections_ban = db["DOTBALLSBAN19"]
runs_given_collection_ban = db["RUNSGIVENBAN19"]


overs_collection_ind = db["OVERSIND19"]
wickets_collection_ind = db["WICKETSIND19"]
average_collection_ind = db["AVERAGEIND19"]
economy_collection_ind = db["ECONOMYIND19"]
strike_rate_collection_ind=db["STRIKERATEIND19"]
dot_balls_collections_ind= db["DOTBALLSIND19"]
runs_given_collection_ind = db["RUNSGIVENIND19"]



overs_collection_sl = db["OVERSSL19"]
wickets_collection_sl = db["WICKETSSL19"]
average_collection_sl = db["AVERAGESL19"]
economy_collection_sl = db["ECONOMYSL19"]
strike_rate_collection_sl=db["STRIKERATESL19"]
dot_balls_collections_sl= db["DOTBALLSSL19"]
runs_given_collection_sl = db["RUNSGIVENSL19"]


overs_collection_bangladesh = db["OVERSBAN21"]
wickets_collection_bangladesh= db["WICKETSBAN21"]
average_collection_bangladesh = db["AVERAGEBAN21"]
economy_collection_bangladesh = db["ECONOMYBAN21"]
strike_rate_collection_bangladesh=db["STRIKERATEBAN21"]
dot_balls_collections_bangladehs= db["DOTBALLSBAN21"]
runs_given_collection_bangladesh = db["RUNSGIVENBAN21"]



overs_collection_india = db["OVERSIND20"]
wickets_collection_india= db["WICKETSIND20"]
average_collection_india = db["AVERAGEIND20"]
economy_collection_india = db["ECONOMYIND20"]
strike_rate_collection_india=db["STRIKERATEIND20"]
dot_balls_collections_india= db["DOTBALLSIND20"]
runs_given_collection_india = db["RUNSGIVENIND20"]



overs_collection_ned = db["OVERSNED22"]
wickets_collection_ned= db["WICKETSNED22"]
average_collection_ned = db["AVERAGENED22"]
economy_collection_ned = db["ECONOMYNED22"]
strike_rate_collection_ned=db["STRIKERATENED22"]
dot_balls_collections_ned= db["DOTBALLSNED22"]
runs_given_collection_ned = db["RUNSGIVENNED22"]




overs_data_pak = list(overs_collection_pak.find().sort([("OversPak", pymongo.ASCENDING)]))
for doc in overs_data_pak:
  doc['OversPak'] = float(doc['OversPak'])

wickets_data_pak = list(wickets_collection_pak.find().sort([("WicketsPak", pymongo.ASCENDING)]))
for doc in wickets_data_pak:
  doc['WicketsPak'] = float(doc['WicketsPak'])

average_data_pak =list(average_collection_pak.find().sort([("AveragePak",pymongo.ASCENDING)]))
for doc in average_data_pak:
    doc['AveragePak']=float(doc['AveragePak'])

economy_data_pak =list(economy_collection_pak.find().sort([("EconomyPak",pymongo.ASCENDING)]))
for doc in economy_data_pak:
    doc['EconomyPak']=float(doc['EconomyPak'])

strike_rate_data_pak =list(strike_rate_collection_pak.find().sort([("StrikeRatePak",pymongo.ASCENDING)]))
for doc in strike_rate_data_pak:
    doc['StrikeRatePak']=float(doc['StrikeRatePak'])

dot_balls_data_pak =list(dot_balls_collection_pak.find().sort([("DotsBallsPak",pymongo.ASCENDING)]))
for doc in dot_balls_data_pak:
    doc['DotsBallsPak']=float(doc['DotsBallsPak'])

runs_given_data_pak =list(runs_given_collection_pak.find().sort([("RunsGivenPak",pymongo.ASCENDING)]))
for doc in runs_given_data_pak:
    doc['RunsGivenPak']=float(doc['RunsGivenPak'])






overs_data_eng = list(overs_collection_eng.find().sort([("OversEng", pymongo.ASCENDING)]))
for doc in overs_data_eng:
  doc['OversEng'] = float(doc['OversEng'])


wickets_data_eng = list(wickets_collection_eng.find().sort([("WicketsEng", pymongo.ASCENDING)]))
for doc in wickets_data_eng:
    doc['WicketsEng'] = int(doc['WicketsEng'])

average_data_eng =list(average_collection_eng.find().sort([("AverageEng",pymongo.ASCENDING)]))
for doc in average_data_eng:
    doc['AverageEng']=float(doc['AverageEng'])

economy_data_eng=list(economy_collection_eng.find().sort([("EconomyEng",pymongo.ASCENDING)]))
for doc in economy_data_eng:
    doc['EconomyEng']=float(doc['EconomyEng'])

strike_rate_data_eng =list(strike_rate_collection_eng.find().sort([("StrikeRateEng",pymongo.ASCENDING)]))
for doc in strike_rate_data_eng:
    doc['StrikeRateEng']=float(doc['StrikeRateEng'])

dot_balls_data_eng =list(dot_balls_collections_eng.find().sort([("DotBallsEng",pymongo.ASCENDING)]))
for doc in dot_balls_data_eng:
    doc['DotBallsEng']=float(doc['DotBallsEng'])

runs_given_data_eng =list(runs_given_collection_eng.find().sort([("RunsGivenEng",pymongo.ASCENDING)]))
for doc in runs_given_data_eng:
    doc['RunsGivenEng']=float(doc['RunsGivenEng'])







overs_data_ban = list(overs_collection_ban.find().sort([("OversBan", pymongo.ASCENDING)]))
for doc in overs_data_ban:
  doc['OversBan'] = float(doc['OversBan'])


wickets_data_ban = list(wickets_collection_ban.find().sort([("WicketsBan", pymongo.ASCENDING)]))
for doc in wickets_data_ban:
    doc['WicketsBan'] = int(doc['WicketsBan'])

average_data_ban =list(average_collection_ban.find().sort([("AverageBan",pymongo.ASCENDING)]))
for doc in average_data_ban:
    doc['AverageBan']=float(doc['AverageBan'])

economy_data_ban=list(economy_collection_ban.find().sort([("EconomyBan",pymongo.ASCENDING)]))
for doc in economy_data_ban:
    doc['EconomyBan']=float(doc['EconomyBan'])

strike_rate_data_ban =list(strike_rate_collection_ban.find().sort([("StrikeRateBan",pymongo.ASCENDING)]))
for doc in strike_rate_data_ban:
    doc['StrikeRateBan']=float(doc['StrikeRateBan'])

dot_balls_data_ban =list(dot_balls_collections_ban.find().sort([("DotBallsBan",pymongo.ASCENDING)]))
for doc in dot_balls_data_ban:
    doc['DotBallsBan']=float(doc['DotBallsBan'])

runs_given_data_ban =list(runs_given_collection_ban.find().sort([("RunsGivenBan",pymongo.ASCENDING)]))
for doc in runs_given_data_ban:
    doc['RunsGivenBan']=float(doc['RunsGivenBan'])





overs_data_ind = list(overs_collection_ind.find().sort([("OversInd", pymongo.ASCENDING)]))
for doc in overs_data_ind:
  doc['OversInd'] = float(doc['OversInd'])


wickets_data_ind = list(wickets_collection_ind.find().sort([("WicketsInd", pymongo.ASCENDING)]))
for doc in wickets_data_ind:
    doc['WicketsInd'] = int(doc['WicketsInd'])

average_data_ind =list(average_collection_ind.find().sort([("AverageInd",pymongo.ASCENDING)]))
for doc in average_data_ind:
    doc['AverageInd']=float(doc['AverageInd'])

economy_data_ind=list(economy_collection_ind.find().sort([("EconomyInd",pymongo.ASCENDING)]))
for doc in economy_data_ind:
    doc['EconomyInd']=float(doc['EconomyInd'])

strike_rate_data_ind =list(strike_rate_collection_ind.find().sort([("StrikeRateInd",pymongo.ASCENDING)]))
for doc in strike_rate_data_ind:
    doc['StrikeRateInd']=float(doc['StrikeRateInd'])

dot_balls_data_ind =list(dot_balls_collections_ind.find().sort([("DotBallsInd",pymongo.ASCENDING)]))
for doc in dot_balls_data_ind:
    doc['DotBallsInd']=float(doc['DotBallsInd'])

runs_given_data_ind =list(runs_given_collection_ind.find().sort([("RunsGivenInd",pymongo.ASCENDING)]))
for doc in runs_given_data_ind:
    doc['RunsGivenInd']=float(doc['RunsGivenInd'])





overs_data_sl = list(overs_collection_sl.find().sort([("OversSl", pymongo.ASCENDING)]))
for doc in overs_data_sl:
  doc['OversSl'] = float(doc['OversSl'])


wickets_data_sl = list(wickets_collection_sl.find().sort([("WicketsSl", pymongo.ASCENDING)]))
for doc in wickets_data_sl:
    doc['WicketsSl'] = int(doc['WicketsSl'])

average_data_sl =list(average_collection_sl.find().sort([("AverageSL",pymongo.ASCENDING)]))
for doc in average_data_sl:
    doc['AverageSL']=float(doc['AverageSL'])

economy_data_sl=list(economy_collection_sl.find().sort([("EconomySL",pymongo.ASCENDING)]))
for doc in economy_data_sl:
    doc['EconomySL']=float(doc['EconomySL'])

strike_rate_data_sl =list(strike_rate_collection_sl.find().sort([("StrikeRateSL",pymongo.ASCENDING)]))
for doc in strike_rate_data_sl:
    doc['StrikeRateSL']=float(doc['StrikeRateSL'])

dot_balls_data_sl =list(dot_balls_collections_sl.find().sort([("DotBallsSL",pymongo.ASCENDING)]))
for doc in dot_balls_data_sl:
    doc['DotBallsSL']=float(doc['DotBallsSL'])

runs_given_data_sl =list(runs_given_collection_sl.find().sort([("RunsGivenSL",pymongo.ASCENDING)]))
for doc in runs_given_data_sl:
    doc['RunsGivenSL']=float(doc['RunsGivenSL'])





overs_data_bangladesh = list(overs_collection_bangladesh.find().sort([("OversBangladesh", pymongo.ASCENDING)]))
for doc in overs_data_bangladesh:
  doc['OversBangladesh'] = float(doc['OversBangladesh'])

wickets_data_bangladesh = list(wickets_collection_bangladesh.find().sort([("WicketsBangladesh", pymongo.ASCENDING)]))
for doc in wickets_data_bangladesh:
  doc['WicketsBangladesh'] = float(doc['WicketsBangladesh'])

average_data_bangladesh =list(average_collection_bangladesh.find().sort([("AverageBangladesh",pymongo.ASCENDING)]))
for doc in average_data_bangladesh:
    doc['AverageBangladesh']=float(doc['AverageBangladesh'])

economy_data_bangladesh =list(economy_collection_bangladesh.find().sort([("EconomyBangladesh",pymongo.ASCENDING)]))
for doc in economy_data_bangladesh:
    doc['EconomyBangladesh']=float(doc['EconomyBangladesh'])

strike_rate_data_bangladesh =list(strike_rate_collection_bangladesh.find().sort([("StrikeRateBangladesh",pymongo.ASCENDING)]))
for doc in strike_rate_data_bangladesh:
    doc['StrikeRateBangladesh']=float(doc['StrikeRateBangladesh'])

dot_balls_data_bangladesh =list(dot_balls_collections_bangladehs.find().sort([("DotBallsBangladesh",pymongo.ASCENDING)]))
for doc in dot_balls_data_bangladesh:
    doc['DotBallsBangladesh']=float(doc['DotBallsBangladesh'])

runs_given_data_bangladesh =list(runs_given_collection_bangladesh.find().sort([("RunsGivenBangladesh",pymongo.ASCENDING)]))
for doc in runs_given_data_bangladesh:
    doc['RunsGivenBangladesh']=float(doc['RunsGivenBangladesh'])



overs_data_india= list(overs_collection_india.find().sort([("OversIndia", pymongo.ASCENDING)]))
for doc in overs_data_india:
  doc['OversIndia'] = float(doc['OversIndia'])

wickets_data_india = list(wickets_collection_india.find().sort([("WicketsIndia", pymongo.ASCENDING)]))
for doc in wickets_data_india:
  doc['WicketsIndia'] = float(doc['WicketsIndia'])

average_data_india =list(average_collection_india.find().sort([("AverageIndia",pymongo.ASCENDING)]))
for doc in average_data_india:
    doc['AverageIndia']=float(doc['AverageIndia'])

economy_data_india =list(economy_collection_india.find().sort([("EconomyIndia",pymongo.ASCENDING)]))
for doc in economy_data_india:
    doc['EconomyIndia']=float(doc['EconomyIndia'])

strike_rate_data_india =list(strike_rate_collection_india.find().sort([("StrikeRateIndia",pymongo.ASCENDING)]))
for doc in strike_rate_data_india:
    doc['StrikeRateIndia']=float(doc['StrikeRateIndia'])

dot_balls_data_india =list(dot_balls_collections_india.find().sort([("DotBallsIndia",pymongo.ASCENDING)]))
for doc in dot_balls_data_india:
    doc['DotBallsIndia']=float(doc['DotBallsIndia'])

runs_given_data_india =list(runs_given_collection_india.find().sort([("RunsGivenIndia",pymongo.ASCENDING)]))
for doc in runs_given_data_india:
    doc['RunsGivenIndia']=float(doc['RunsGivenIndia'])




overs_data_ned= list(overs_collection_ned.find().sort([("OversNed", pymongo.ASCENDING)]))
for doc in overs_data_ned:
  doc['OversNed'] = float(doc['OversNed'])

wickets_data_ned = list(wickets_collection_ned.find().sort([("WicketsNed", pymongo.ASCENDING)]))
for doc in wickets_data_ned:
  doc['WicketsNed'] = float(doc['WicketsNed'])

average_data_ned =list(average_collection_ned.find().sort([("AverageNed",pymongo.ASCENDING)]))
for doc in average_data_ned:
    doc['AverageNed']=float(doc['AverageNed'])

economy_data_ned =list(economy_collection_ned.find().sort([("EconomyNed",pymongo.ASCENDING)]))
for doc in economy_data_ned:
    doc['EconomyNed']=float(doc['EconomyNed'])

strike_rate_data_ned=list(strike_rate_collection_ned.find().sort([("StrikeRateNed",pymongo.ASCENDING)]))
for doc in strike_rate_data_ned:
    doc['StrikeRateNed']=float(doc['StrikeRateNed'])

dot_balls_data_ned =list(dot_balls_collections_ned.find().sort([("DotBallsNed",pymongo.ASCENDING)]))
for doc in dot_balls_data_ned:
    doc['DotBallsNed']=float(doc['DotBallsNed'])

runs_given_data_ned =list(runs_given_collection_ned.find().sort([("RunsGivenNed",pymongo.ASCENDING)]))
for doc in runs_given_data_ned:
    doc['RunsGivenNed']=float(doc['RunsGivenNed'])






# Defining the layout of the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP,'https://use.fontawesome.com/releases/v5.7.2/css/all.css'])
layout = html.Div([
    html.H1('SERIES STATISTICS', style={'text-align': 'center', 'font-weight': 'bold','padding-top':'50px','color': 'white'}),
    html.Div([
       html.H1("PAK VS NZ 2018",style={'padding-top':'20px','font-weight':'bold','color':'white','font-size': '20px','background-color':'#013470'}),
     dbc.Button("OVERS", id="show-overs-graph-btn-1",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#23D31F'}),
     dbc.Button("WICKETS", id="show-wickets-graph-btn-1",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#23D31F'}),
     dbc.Button("AVERAGE", id="show-average-graph-btn-1",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#23D31F'}),
     dbc.Button("ECONOMY", id="show-economy-graph-btn-1",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#23D31F'}),
     dbc.Button("STRIKE RATE", id="show-strikerate-graph-btn-1",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#23D31F'}),
     dbc.Button("DOT BALLS", id="show-dotballs-graph-btn-1",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#23D31F'}),
     dbc.Button("RUNS GIVEN", id="show-runsgiven-graph-btn-1",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#23D31F'}),
    html.Div(id="graph-container-1",style={'padding-top':'20px'})
    ],style={'padding-top':'20px','margin': 'auto', 'width': '80%'}),


 html.Div([
    html.H1("ENG VS NZ 2018",style={'padding-top':'20px','font-weight':'bold','color':'white','font-size': '20px','background-color':'#013470'}),
     dbc.Button("OVERS", id="show-overs-graph-btn-2",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002074'}),
     dbc.Button("WICKETS", id="show-wickets-graph-btn-2",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002074'}),
     dbc.Button("AVERAGE", id="show-average-graph-btn-2",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002074'}),
     dbc.Button("ECONOMY", id="show-economy-graph-btn-2",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002074'}),
     dbc.Button("STRIKE RATE", id="show-strikerate-graph-btn-2",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002074'}),
     dbc.Button("DOT BALLS", id="show-dotballs-graph-btn-2",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002074'}),
     dbc.Button("RUNS GIVEN", id="show-runsgiven-graph-btn-2",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002074'}),
     html.Div(id="graph-container-2",style={'padding-top':'20px'})
 ],style={'padding-top':'20px','margin': 'auto', 'width': '80%'}),

html.Div([
    html.H1("BAN VS NZ 2019",style={'padding-top':'20px','font-weight':'bold','color':'white','font-size': '20px','background-color':'#013470'}),
     dbc.Button("OVERS", id="show-overs-graph-btn-3",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
     dbc.Button("WICKETS", id="show-wickets-graph-btn-3",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
     dbc.Button("AVERAGE", id="show-average-graph-btn-3",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
     dbc.Button("ECONOMY", id="show-economy-graph-btn-3",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
     dbc.Button("STRIKE RATE", id="show-strikerate-graph-btn-3",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
     dbc.Button("DOT BALLS", id="show-dotballs-graph-btn-3",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
     dbc.Button("RUNS GIVEN", id="show-runsgiven-graph-btn-3",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
    html.Div(id="graph-container-3",style={'padding-top':'20px'})
 ],style={'padding-top':'20px','margin': 'auto', 'width': '80%'}),


html.Div([
    html.H1("IND VS NZ 2019",style={'padding-top':'20px','font-weight':'bold','color':'white','font-size': '20px','background-color':'#013470'}),
     dbc.Button("OVERS", id="show-overs-graph-btn-4",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
     dbc.Button("WICKETS", id="show-wickets-graph-btn-4",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
     dbc.Button("AVERAGE", id="show-average-graph-btn-4",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
     dbc.Button("ECONOMY", id="show-economy-graph-btn-4",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
     dbc.Button("STRIKE RATE", id="show-strikerate-graph-btn-4",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
     dbc.Button("DOT BALLS", id="show-dotballs-graph-btn-4",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
     dbc.Button("RUNS GIVEN", id="show-runsgiven-graph-btn-4",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
    html.Div(id="graph-container-4",style={'padding-top':'20px'})
 ],style={'padding-top':'20px','margin': 'auto', 'width': '80%'}),



html.Div([
    html.H1("SL VS NZ 2019",style={'padding-top':'20px','font-weight':'bold','color':'white','font-size': '20px','background-color':'#013470'}),
     dbc.Button("OVERS", id="show-overs-graph-btn-5",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002ABC'}),
     dbc.Button("WICKETS", id="show-wickets-graph-btn-5",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002ABC'}),
     dbc.Button("AVERAGE", id="show-average-graph-btn-5",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002ABC'}),
     dbc.Button("ECONOMY", id="show-economy-graph-btn-5",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002ABC'}),
     dbc.Button("STRIKE RATE", id="show-strikerate-graph-btn-5",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002ABC'}),
     dbc.Button("DOT BALLS", id="show-dotballs-graph-btn-5",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002ABC'}),
     dbc.Button("RUNS GIVEN", id="show-runsgiven-graph-btn-5",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#002ABC'}),
    html.Div(id="graph-container-5",style={'padding-top':'20px'})
 ],style={'padding-top':'20px','margin': 'auto', 'width': '80%'}),



html.Div([
    html.H1("IND VS NZ 2020",style={'padding-top':'20px','font-weight':'bold','color':'white','font-size': '20px','background-color':'#013470'}),
     dbc.Button("OVERS", id="show-overs-graph-btn-7",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
     dbc.Button("WICKETS", id="show-wickets-graph-btn-7",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
     dbc.Button("AVERAGE", id="show-average-graph-btn-7",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
     dbc.Button("ECONOMY", id="show-economy-graph-btn-7",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
     dbc.Button("STRIKE RATE", id="show-strikerate-graph-btn-7",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
     dbc.Button("DOT BALLS", id="show-dotballs-graph-btn-7",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
     dbc.Button("RUNS GIVEN", id="show-runsgiven-graph-btn-7",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#3579B9'}),
    html.Div(id="graph-container-7",style={'padding-top':'20px'})
 ],style={'padding-top':'20px','margin': 'auto', 'width': '80%'}),



html.Div([
    html.H1("BAN VS NZ 2021",style={'padding-top':'20px','font-weight':'bold','color':'white','font-size': '20px','background-color':'#013470'}),
     dbc.Button("OVERS", id="show-overs-graph-btn-6",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
     dbc.Button("WICKETS", id="show-wickets-graph-btn-6",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
     dbc.Button("AVERAGE", id="show-average-graph-btn-6",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
     dbc.Button("ECONOMY", id="show-economy-graph-btn-6",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
     dbc.Button("STRIKE RATE", id="show-strikerate-graph-btn-6",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
     dbc.Button("DOT BALLS", id="show-dotballs-graph-btn-6",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
     dbc.Button("RUNS GIVEN", id="show-runsgiven-graph-btn-6",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#005A04'}),
    html.Div(id="graph-container-6",style={'padding-top':'20px'})
 ],style={'padding-top':'20px','margin': 'auto', 'width': '80%'}),


html.Div([
    html.H1("NED VS NZ 2022",style={'padding-top':'20px','font-weight':'bold','color':'white','font-size': '20px','background-color':'#013470'}),
     dbc.Button("OVERS", id="show-overs-graph-btn-8",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#FF6B00'}),
     dbc.Button("WICKETS", id="show-wickets-graph-btn-8",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#FF6B00'}),
     dbc.Button("AVERAGE", id="show-average-graph-btn-8",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#FF6B00'}),
     dbc.Button("ECONOMY", id="show-economy-graph-btn-8",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#FF6B00'}),
     dbc.Button("STRIKE RATE", id="show-strikerate-graph-btn-8",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#FF6B00'}),
     dbc.Button("DOT BALLS", id="show-dotballs-graph-btn-8",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#FF6B00'}),
     dbc.Button("RUNS GIVEN", id="show-runsgiven-graph-btn-8",style={'margin-right': '10px','font-weight':'bold','margin-top':'20px','background-color':'#FF6B00'}),
    html.Div(id="graph-container-8",style={'padding-top':'20px'})
 ],style={'padding-top':'20px','margin': 'auto', 'width': '80%'}),

],style={'text-align':'center','background-color':'#2E4C87'})


# Define the callback for updating the chart
@app.callback(
    Output("graph-container-1", "children"),
    [Input("show-overs-graph-btn-1", "n_clicks"),
     Input("show-wickets-graph-btn-1", "n_clicks"),
     Input("show-average-graph-btn-1", "n_clicks"),
     Input("show-economy-graph-btn-1", "n_clicks"),
     Input("show-strikerate-graph-btn-1", "n_clicks"),
     Input("show-dotballs-graph-btn-1", "n_clicks"),
     Input("show-runsgiven-graph-btn-1", "n_clicks")],
    State("graph-container-1", "children")
)
def update_chart_1(overs_n_clicks, wickets_n_clicks,average_n_click,economy_n_click,strikerate_n_click,dotballs_n_clicks,runsgiven_n_clicks, current_children):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "show-overs-graph-btn-1":
    # Get the data from the 'OVERSPAK18' collection
        data = overs_data_pak
        x = [d["PlayerPak"] for d in data]
        y = [d["OversPak"] for d in data]

    # Define a list of colors
        colors = ['#141462', '#1C6496', '#228BC0', '#31B7E6', '#CCE0F5']

    # Create a list of color values based on the length of the data
        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y, marker=dict(color=color_values))])
        fig.update_layout(title="Total No of Overs Bowled",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')
        

    elif button_id == "show-wickets-graph-btn-1":
    # Get the data from the 'WICKETSPAK18' collection
        data = wickets_data_pak
        x = [d["WicketsPak"] for d in data]
        y = [d["PlayerPak"] for d in data]
        # Define a list of colors
        colors = ['#141462', '#1C6496', '#228BC0', '#31B7E6', '#CCE0F5']

        # Create a list of color values based on the length of the data
        color_values = [colors[i % len(colors)] for i in range(len(x))]


        fig = go.Figure([go.Bar(x=x, y=y, marker=dict(color=color_values), orientation='h')])
        fig.update_layout(title="No of Wickets taken",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')


    
    elif button_id == "show-average-graph-btn-1":
        # Get the data from the 'AVERAGEPAK18' collection
        data = average_data_pak
        x = [d["PlayerPak"] for d in data]
        y = [d["AveragePak"] for d in data]

        # Define a list of colors
        colors = ['#141462', '#1C6496', '#228BC0', '#31B7E6', '#CCE0F5']

        # Create a list of color values based on the length of the data
        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowler's Average",
                          plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-economy-graph-btn-1":
    # Get the data from the 'ECONOMYPAK18' collection
        data = economy_data_pak
        x = [d["PlayerPak"] for d in data]
        y = [d["EconomyPak"] for d in data]
        fig = go.Figure([go.Scatter(x=x, y=y, mode='lines+markers', marker=dict(color='#21218F'))])
        fig.update_layout(title="Bowler's Economy",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')

    
    elif button_id == "show-strikerate-graph-btn-1":
        # Get the data from the 'STRIKERATEPAK18' collection
        data = strike_rate_data_pak
        x = [d["PlayerPak"] for d in data]
        y = [d["StrikeRatePak"] for d in data]

         # Define a list of colors
        colors = ['#141462', '#1C6496', '#228BC0', '#31B7E6', '#CCE0F5']

        # Create a list of color values based on the length of the data
        color_values = [colors[i % len(colors)] for i in range(len(x))]



        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowling Strike Rates",
                          plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-dotballs-graph-btn-1":
    # Get the data from the 'DOTBALLSPAK18' collection
        data = dot_balls_data_pak
        labels = [d["PlayerPak"] for d in data]
        values = [d["DotsBallsPak"] for d in data]
        fig = go.Figure([go.Pie(labels=labels, values=values, hole=0.4,marker=dict(colors=['#0099ff', '#33ccff', '#66ffff', '#99ffcc', '#ccff99', '#ffff66', '#ffcc33', '#ff9933', '#ff6600']))])
        fig.update_layout(title="Dot Balls Bowled",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')


    elif button_id == "show-runsgiven-graph-btn-1":
        # Get the data from the 'RUNSGIVENSPAK18' collection
        data = runs_given_data_pak
        x = [d["PlayerPak"] for d in data]
        y = [d["RunsGivenPak"] for d in data]


         # Define a list of colors
        colors = ['#141462', '#1C6496', '#228BC0', '#31B7E6', '#CCE0F5']

        # Create a list of color values based on the length of the data
        color_values = [colors[i % len(colors)] for i in range(len(x))]


        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Runs Conceded ",
                          plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    else:
        # Return an empty div if no button has been clicked
        return html.Div()

    # Return the graph
    return dcc.Graph(figure=fig)



@app.callback(
    Output("graph-container-2", "children"),
    [Input("show-overs-graph-btn-2", "n_clicks"),
     Input("show-wickets-graph-btn-2", "n_clicks"),
     Input("show-average-graph-btn-2", "n_clicks"),
     Input("show-economy-graph-btn-2", "n_clicks"),
     Input("show-strikerate-graph-btn-2", "n_clicks"),
     Input("show-dotballs-graph-btn-2", "n_clicks"),
     Input("show-runsgiven-graph-btn-2", "n_clicks")],
    State("graph-container-2", "children")
)
def update_chart_2(overs_n_clicks, wickets_n_clicks,average_n_click,economy_n_click,strikerate_n_click,dotballs_n_clicks,runsgiven_n_clicks, current_children):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "show-overs-graph-btn-2":
        # Get the data from the 'OVERSENG18' collection
        data = overs_data_eng
        x = [d["PlayerEng"] for d in data]
        y = [d["OversEng"] for d in data]

        colors = ['#FFB6C1', '#87CEFA', '#98FB98', '#FFD700', '#FFA07A']


        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Total No of Overs Bowled",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-wickets-graph-btn-2":
    # Get the data from the 'WICKETSENG18' collection
        data = wickets_data_eng
        y = [d["PlayerEng"] for d in data]
        x = [d["WicketsEng"] for d in data]

        colors = ['#FFB6C1', '#87CEFA', '#98FB98', '#FFD700', '#FFA07A']


        color_values = [colors[i % len(colors)] for i in range(len(x))]


        fig = go.Figure([go.Bar(x=x, y=y, orientation='h', marker=dict(color=color_values))])
        fig.update_layout(title="Wickets taken",
                      xaxis_title="Number of Wickets",
                      yaxis_title="Player Name",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')



    elif button_id == "show-average-graph-btn-2":
        # Get the data from the 'AVERAGEENG18' collection
        data = average_data_eng
        x = [d["PlayerEng"] for d in data]
        y = [d["AverageEng"] for d in data]

        colors = ['#FFB6C1', '#87CEFA', '#98FB98', '#FFD700', '#FFA07A']


        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowler's Average",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-economy-graph-btn-2":
    # Get the data from the 'ECONOMYENG18' collection
        data = economy_data_eng
        x = [d["PlayerEng"] for d in data]
        y = [d["EconomyEng"] for d in data]
        fig = go.Figure([go.Scatter(x=x, y=y, mode='lines+markers', marker=dict(color='#02875F'))])
        fig.update_layout(title="Bowler's Average",
                       plot_bgcolor='#0C8AF0',
                       paper_bgcolor='#0C8AF0',
                       font_color='white')
    
    elif button_id == "show-strikerate-graph-btn-2":
        # Get the data from the 'STRIKERATEENG18' collection
        data = strike_rate_data_eng
        x = [d["PlayerEng"] for d in data]
        y = [d["StrikeRateEng"] for d in data]


        colors = ['#FFB6C1', '#87CEFA', '#98FB98', '#FFD700', '#FFA07A']


        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowling Strike Rates",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')
        
    elif button_id == "show-dotballs-graph-btn-2":
    # Get the data from the 'DOTBALLSENG18' collection
        data = dot_balls_data_eng
        labels = [d["PlayerEng"] for d in data]
        values = [d["DotBallsEng"] for d in data]
        fig = go.Figure([go.Pie(labels=labels, values=values, hole=0.4,marker=dict(colors=['#4B0082', '#800080', '#8B008B', '#9400D3', '#9932CC', '#BA55D3', '#DA70D6', '#EE82EE', '#FF00FF']))])
        fig.update_layout(title="Dot Balls Bowled",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')


    elif button_id == "show-runsgiven-graph-btn-2":
        # Get the data from the 'RUNSGIVENSENG18' collection
        data = runs_given_data_eng
        x = [d["PlayerEng"] for d in data]
        y = [d["RunsGivenEng"] for d in data]


        colors = ['#FFB6C1', '#87CEFA', '#98FB98', '#FFD700', '#FFA07A']


        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Runs Conceded",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    else:
        # Return an empty div if no button has been clicked
        return html.Div()

    # Return the graph
    return dcc.Graph(figure=fig)





@app.callback(
    Output("graph-container-3", "children"),
    [Input("show-overs-graph-btn-3", "n_clicks"),
     Input("show-wickets-graph-btn-3", "n_clicks"),
     Input("show-average-graph-btn-3", "n_clicks"),
     Input("show-economy-graph-btn-3", "n_clicks"),
     Input("show-strikerate-graph-btn-3", "n_clicks"),
     Input("show-dotballs-graph-btn-3", "n_clicks"),
     Input("show-runsgiven-graph-btn-3", "n_clicks")],
    State("graph-container-3", "children")
)
def update_chart_3(overs_n_clicks, wickets_n_clicks,average_n_click,economy_n_click,strikerate_n_click,dotballs_n_clicks,runsgiven_n_clicks, current_children):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "show-overs-graph-btn-3":
        # Get the data from the 'OVERSBAN19' collection
        data = overs_data_ban
        x = [d["PlayerBan"] for d in data]
        y = [d["OversBan"] for d in data]


        colors = ['#8B4513', '#CD853F', '#D2B48C', '#DEB887', '#F5DEB3']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Total No of Overs",
                         plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-wickets-graph-btn-3":
    # Get the data from the 'WICKETSBAN19' collection
        data = wickets_data_ban
        y = [d["PlayerBan"] for d in data]
        x = [d["WicketsBan"] for d in data]

        colors = ['#8B4513', '#CD853F', '#D2B48C', '#DEB887', '#F5DEB3']

        color_values = [colors[i % len(colors)] for i in range(len(x))]


        fig = go.Figure([go.Bar(x=x, y=y, orientation='h', marker=dict(color=color_values))])
        fig.update_layout(title="Wickets taken",
                      xaxis_title="Number of Wickets",
                      yaxis_title="Player Name",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')


    elif button_id == "show-average-graph-btn-3":
        # Get the data from the 'AVERAGEBAN19' collection
        data = average_data_ban
        x = [d["PlayerBan"] for d in data]
        y = [d["AverageBan"] for d in data]


        colors = ['#8B4513', '#CD853F', '#D2B48C', '#DEB887', '#F5DEB3']

        color_values = [colors[i % len(colors)] for i in range(len(x))]
        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowler's Average",
                          plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-economy-graph-btn-3":
    # Get the data from the 'ECONOMYBAN19' collection
        data = economy_data_ban
        x = [d["PlayerBan"] for d in data]
        y = [d["EconomyBan"] for d in data]
        fig = go.Figure([go.Scatter(x=x, y=y, mode='lines+markers', marker=dict(color='#2E2B1B'))])
        fig.update_layout(title="Bowler's Economy",
                       plot_bgcolor='#0C8AF0',
                       paper_bgcolor='#0C8AF0',
                       font_color='white')
    
    elif button_id == "show-strikerate-graph-btn-3":
        # Get the data from the 'STRIKERATEBAN19' collection
        data = strike_rate_data_ban
        x = [d["PlayerBan"] for d in data]
        y = [d["StrikeRateBan"] for d in data]


        colors = ['#8B4513', '#CD853F', '#D2B48C', '#DEB887', '#F5DEB3']

        color_values = [colors[i % len(colors)] for i in range(len(x))]
        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowling Strike Rates",
                          plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-dotballs-graph-btn-3":
    # Get the data from the 'DOTBALLSBAN19' collection
        data = dot_balls_data_ban
        labels = [d["PlayerBan"] for d in data]
        values = [d["DotBallsBan"] for d in data]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.4,marker=dict(colors=['#FF8C00', '#FFA07A', '#FFB6C1', '#FFC0CB', '#FFDAB9', '#FFE4E1', '#FFDEAD', '#FFA500', '#FF4500']))])
        fig.update_layout(title="Dot Balls Bowled",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')

    elif button_id == "show-runsgiven-graph-btn-3":
        # Get the data from the 'RUNSGIVENSBAN19' collection
        data = runs_given_data_ban
        x = [d["PlayerBan"] for d in data]
        y = [d["RunsGivenBan"] for d in data]

        
        colors = ['#8B4513', '#CD853F', '#D2B48C', '#DEB887', '#F5DEB3']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Runs Conceded",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    else:
        # Return an empty div if no button has been clicked
        return html.Div()

    # Return the graph
    return dcc.Graph(figure=fig)





@app.callback(
    Output("graph-container-4", "children"),
    [Input("show-overs-graph-btn-4", "n_clicks"),
     Input("show-wickets-graph-btn-4", "n_clicks"),
     Input("show-average-graph-btn-4", "n_clicks"),
     Input("show-economy-graph-btn-4", "n_clicks"),
     Input("show-strikerate-graph-btn-4", "n_clicks"),
     Input("show-dotballs-graph-btn-4", "n_clicks"),
     Input("show-runsgiven-graph-btn-4", "n_clicks")],
    State("graph-container-4", "children")
)
def update_chart_4(overs_n_clicks, wickets_n_clicks,average_n_click,economy_n_click,strikerate_n_click,dotballs_n_clicks,runsgiven_n_clicks, current_children):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "show-overs-graph-btn-4":
        # Get the data from the 'OVERSIND19' collection
        data = overs_data_ind
        x = [d["PlayerInd"] for d in data]
        y = [d["OversInd"] for d in data]

        colors = ['#FF69B4', '#FFD700', '#00FFFF', '#FF4500', '#800080']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Total No of Overs Bowled",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-wickets-graph-btn-4":
    # Get the data from the 'WICKETSIND19' collection
        data = wickets_data_ind
        y = [d["PlayerInd"] for d in data]
        x = [d["WicketsInd"] for d in data]

        colors = ['#FF69B4', '#FFD700', '#00FFFF', '#FF4500', '#800080']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y, orientation='h', marker=dict(color=color_values))])
        fig.update_layout(title="Wickets taken",
                      xaxis_title="Number of Wickets",
                      yaxis_title="Player Name",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')



    elif button_id == "show-average-graph-btn-4":
        # Get the data from the 'AVERAGEIND19' collection
        data = average_data_ind
        x = [d["PlayerInd"] for d in data]
        y = [d["AverageInd"] for d in data]

        colors = ['#FF69B4', '#FFD700', '#00FFFF', '#FF4500', '#800080']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowler's Average",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-economy-graph-btn-4":
    # Get the data from the 'ECONOMYIND19' collection
        data = economy_data_ind
        x = [d["PlayerInd"] for d in data]
        y = [d["EconomyInd"] for d in data]
        fig = go.Figure([go.Scatter(x=x, y=y, mode='lines+markers', marker=dict(color='#302225'))])
        fig.update_layout(title="Bowler's Average",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')
    
    elif button_id == "show-strikerate-graph-btn-4":
        # Get the data from the 'STRIKERATEIND19' collection
        data = strike_rate_data_ind
        x = [d["PlayerInd"] for d in data]
        y = [d["StrikeRateInd"] for d in data]

        colors = ['#FF69B4', '#FFD700', '#00FFFF', '#FF4500', '#800080']

        color_values = [colors[i % len(colors)] for i in range(len(x))]
        

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowling Strike Rates",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-dotballs-graph-btn-4":
    # Get the data from the 'DOTBALLSIND19' collection
        data = dot_balls_data_ind
        labels = [d["PlayerInd"] for d in data]
        values = [d["DotBallsInd"] for d in data]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.4,marker=dict(colors=['#00CED1', '#20B2AA', '#2F4F4F', '#3CB371', '#4682B4', '#808080', '#9370DB', '#A52A2A', '#D2691E']))])
        fig.update_layout(title="Dot Balls Bowled",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')

    elif button_id == "show-runsgiven-graph-btn-4":
        # Get the data from the 'RUNSGIVENSIND19' collection
        data = runs_given_data_ind
        x = [d["PlayerInd"] for d in data]
        y = [d["RunsGivenInd"] for d in data]

        colors = ['#FF69B4', '#FFD700', '#00FFFF', '#FF4500', '#800080']

        color_values = [colors[i % len(colors)] for i in range(len(x))]
        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Runs Conceded",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    else:
        # Return an empty div if no button has been clicked
        return html.Div()

    # Return the graph
    return dcc.Graph(figure=fig)




@app.callback(
    Output("graph-container-5", "children"),
    [Input("show-overs-graph-btn-5", "n_clicks"),
     Input("show-wickets-graph-btn-5", "n_clicks"),
     Input("show-average-graph-btn-5", "n_clicks"),
     Input("show-economy-graph-btn-5", "n_clicks"),
     Input("show-strikerate-graph-btn-5", "n_clicks"),
     Input("show-dotballs-graph-btn-5", "n_clicks"),
     Input("show-runsgiven-graph-btn-5", "n_clicks")],
    State("graph-container-5", "children")
)
def update_chart_5(overs_n_clicks, wickets_n_clicks,average_n_click,economy_n_click,strikerate_n_click,dotballs_n_clicks,runsgiven_n_clicks, current_children):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "show-overs-graph-btn-5":
        # Get the data from the 'OVERSSL19' collection
        data = overs_data_sl
        x = [d["PlayerSl"] for d in data]
        y = [d["OversSl"] for d in data]


        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Total No of Overs Bowled",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-wickets-graph-btn-5":
    # Get the data from the 'WICKETSSL19' collection
        data = wickets_data_sl
        y = [d["PlayerSl"] for d in data]
        x = [d["WicketsSl"] for d in data]

        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y, orientation='h', marker=dict(color=color_values))])
        fig.update_layout(title="Wickets taken",
                      xaxis_title="Number of Wickets",
                      yaxis_title="Player Name",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')



    elif button_id == "show-average-graph-btn-5":
        # Get the data from the 'AVERAGESL19' collection
        data = average_data_sl
        x = [d["PlayerSRI"] for d in data]
        y = [d["AverageSL"] for d in data]


        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF']

        color_values = [colors[i % len(colors)] for i in range(len(x))]


        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowler's Average",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-economy-graph-btn-5":
    # Get the data from the 'ECONOMYSL19' collection
        data = economy_data_sl
        x = [d["PlayerLanka"] for d in data]
        y = [d["EconomySL"] for d in data]

        

        fig = go.Figure([go.Scatter(x=x, y=y, mode='lines+markers', marker=dict(color='#305152'))])
        fig.update_layout(title="Bowler's Economy",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')
    
    elif button_id == "show-strikerate-graph-btn-5":
        # Get the data from the 'STRIKERATESL19' collection
        data = strike_rate_data_sl
        x = [d["PlayerSL"] for d in data]
        y = [d["StrikeRateSL"] for d in data]

        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowling Strike Rates",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-dotballs-graph-btn-5":
    # Get the data from the 'DOTBALLSSL19' collection
        data = dot_balls_data_sl
        labels = [d["PlayerSriLanka"] for d in data]
        values = [d["DotBallsSL"] for d in data]
        fig = go.Figure([go.Pie(labels=labels, values=values, hole=0.4,marker=dict(colors=['#7CFC00', '#32CD32', '#228B22', '#006400', '#556B2F', '#8FBC8F', '#2E8B57', '#008080', '#00FFFF']))])
        fig.update_layout(title="Dot Balls Bowled",
                       plot_bgcolor='#0C8AF0',
                       paper_bgcolor='#0C8AF0',
                       font_color='white')


    elif button_id == "show-runsgiven-graph-btn-5":
        # Get the data from the 'RUNSGIVENSSL19' collection
        data = runs_given_data_sl
        x = [d["Players"] for d in data]
        y = [d["RunsGivenSL"] for d in data]

        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Runs Conceded",
                          plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    else:
        # Return an empty div if no button has been clicked
        return html.Div()

    # Return the graph
    return dcc.Graph(figure=fig)



@app.callback(
    Output("graph-container-6", "children"),
    [Input("show-overs-graph-btn-6", "n_clicks"),
     Input("show-wickets-graph-btn-6", "n_clicks"),
     Input("show-average-graph-btn-6", "n_clicks"),
     Input("show-economy-graph-btn-6", "n_clicks"),
     Input("show-strikerate-graph-btn-6", "n_clicks"),
     Input("show-dotballs-graph-btn-6", "n_clicks"),
     Input("show-runsgiven-graph-btn-6", "n_clicks")],
    State("graph-container-6", "children")
)
def update_chart_6(overs_n_clicks, wickets_n_clicks,average_n_click,economy_n_click,strikerate_n_click,dotballs_n_clicks,runsgiven_n_clicks, current_children):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]


    

    if button_id == "show-overs-graph-btn-6":
        # Get the data from the 'OVERSBAN21' collection
        data = overs_data_bangladesh
        x = [d["PlayerBangladesh"] for d in data]
        y = [d["OversBangladesh"] for d in data]

        colors = ['#FF00FF', '#00FFFF', '#FFFF00', '#FF1493', '#00FF00']
        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Total No of Overs Bowled",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-wickets-graph-btn-6":
        # Get the data from the 'WICKETSBAN21' collection
        data = wickets_data_bangladesh
        x = [d["PlayerBangladesh"] for d in data]
        y = [d["WicketsBangladesh"] for d in data]
        colors = ['#FF00FF', '#00FFFF', '#FFFF00', '#FF1493', '#00FF00']
        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=y, y=x, orientation='h', marker=dict(color=color_values))])
        fig.update_layout(title="Wickets taken",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')


    elif button_id == "show-average-graph-btn-6":
        # Get the data from the 'AVERAGEBAN21' collection
        data = average_data_bangladesh
        x = [d["PlayerBangladesh"] for d in data]
        y = [d["AverageBangladesh"] for d in data]
        colors = ['#FF00FF', '#00FFFF', '#FFFF00', '#FF1493', '#00FF00']
        color_values = [colors[i % len(colors)] for i in range(len(x))]
        fig = go.Figure([go.Bar(x=x, y=y, marker=dict(color=color_values))])
        fig.update_layout(title="Bowler's Average",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-economy-graph-btn-6":
    # Get the data from the 'ECONOMYBAN21' collection
        data = economy_data_bangladesh
        x = [d["PlayerBangladesh"] for d in data]
        y = [d["EconomyBangladesh"] for d in data]
        fig = go.Figure([go.Scatter(x=x, y=y, mode='lines+markers', line=dict(color='#25272C'))])
        fig.update_layout(title="Bowler's Economy",
                       plot_bgcolor='#0C8AF0',
                       paper_bgcolor='#0C8AF0',
                       font_color='white')
    
    elif button_id == "show-strikerate-graph-btn-6":
        # Get the data from the 'STRIKERATEBAN21' collection
        data = strike_rate_data_bangladesh
        x = [d["PlayerBangladesh"] for d in data]
        y = [d["StrikeRateBangladesh"] for d in data]

        colors = ['#FF00FF', '#00FFFF', '#FFFF00', '#FF1493', '#00FF00']
        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowling Strike Rates",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-dotballs-graph-btn-6":
    # Get the data from the 'DOTBALLSBan21' collection
        data = dot_balls_data_bangladesh
        labels = [d["PlayerBangladesh"] for d in data]
        values = [d["DotBallsBangladesh"] for d in data]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.4,marker=dict(colors=['#FF5733', '#FFC300', '#DAF7A6', '#FF5733', '#C70039']))])
        fig.update_layout(title="Dot Balls Bowled",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')


    elif button_id == "show-runsgiven-graph-btn-6":
        # Get the data from the 'RUNSGIVENSSL19' collection
        data = runs_given_data_bangladesh
        x = [d["PlayerBangladesh"] for d in data]
        y = [d["RunsGivenBangladesh"] for d in data]

        colors = ['#FF00FF', '#00FFFF', '#FFFF00', '#FF1493', '#00FF00']
        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Runs Conceded",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    else:
        # Return an empty div if no button has been clicked
        return html.Div()

    # Return the graph
    return dcc.Graph(figure=fig)







@app.callback(
    Output("graph-container-7", "children"),
    [Input("show-overs-graph-btn-7", "n_clicks"),
     Input("show-wickets-graph-btn-7", "n_clicks"),
     Input("show-average-graph-btn-7", "n_clicks"),
     Input("show-economy-graph-btn-7", "n_clicks"),
     Input("show-strikerate-graph-btn-7", "n_clicks"),
     Input("show-dotballs-graph-btn-7", "n_clicks"),
     Input("show-runsgiven-graph-btn-7", "n_clicks")],
    State("graph-container-7", "children")
)
def update_chart_7(overs_n_clicks, wickets_n_clicks,average_n_click,economy_n_click,strikerate_n_click,dotballs_n_clicks,runsgiven_n_clicks, current_children):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]


    

    if button_id == "show-overs-graph-btn-7":
        # Get the data from the 'OVERSBAN21' collection
        data = overs_data_india
        x = [d["PlayerIndia"] for d in data]
        y = [d["OversIndia"] for d in data]

        colors = ['#FF7F50', '#FFA500', '#D2691E', '#8B0000', '#A0522D']

        color_values = [colors[i % len(colors)] for i in range(len(x))]


        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Total No of Overs Bowled",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-wickets-graph-btn-7":
        # Get the data from the 'WICKETSBAN21' collection
        data = wickets_data_india
        x = [d["PlayerIndia"] for d in data]
        y = [d["WicketsIndia"] for d in data]


        colors = ['#FF7F50', '#FFA500', '#D2691E', '#8B0000', '#A0522D']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=y, y=x, orientation='h', marker=dict(color=color_values))])
        fig.update_layout(title="Wickets taken",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-average-graph-btn-7":
        # Get the data from the 'AVERAGEBAN21' collection
        data = average_data_india
        x = [d["PlayerIndia"] for d in data]
        y = [d["AverageIndia"] for d in data]


        colors = ['#FF7F50', '#FFA500', '#D2691E', '#8B0000', '#A0522D']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowler's Average",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-economy-graph-btn-7":
    # Get the data from the 'ECONOMYBAN21' collection
        data = economy_data_india
        x = [d["PlayerIndia"] for d in data]
        y = [d["EconomyIndia"] for d in data]
        fig = go.Figure([go.Scatter(x=x, y=y, mode='lines+markers', line=dict(color='#2C1B10'))])
        fig.update_layout(title="Bowler's Economy",
                      plot_bgcolor='#0C8AF0',
                      paper_bgcolor='#0C8AF0',
                      font_color='white')

    
    elif button_id == "show-strikerate-graph-btn-7":
        # Get the data from the 'STRIKERATEBAN21' collection
        data = strike_rate_data_india
        x = [d["PlayerIndia"] for d in data]
        y = [d["StrikeRateIndia"] for d in data]

        colors = ['#FF7F50', '#FFA500', '#D2691E', '#8B0000', '#A0522D']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowling Strike Rates",
                          plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-dotballs-graph-btn-7":
        # Get the data from the 'DOTBALLSBan21' collection
        data = dot_balls_data_india
        labels = [d["PlayerIndia"] for d in data]
        values = [d["DotBallsIndia"] for d in data]
        fig = go.Figure([go.Pie(labels=labels, values=values, hole=0.4,marker=dict(colors=['#0040FF', '#8000FF', '#00FFFF', '#FF00FF', '#FF0080']))])
        fig.update_layout(title="Dot Balls Bowled",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')


    elif button_id == "show-runsgiven-graph-btn-7":
        # Get the data from the 'RUNSGIVENSSL19' collection
        data = runs_given_data_india
        x = [d["PlayerIndia"] for d in data]
        y = [d["RunsGivenIndia"] for d in data]

        colors = ['#FF7F50', '#FFA500', '#D2691E', '#8B0000', '#A0522D']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Runs Conceded",
                         plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    else:
        # Return an empty div if no button has been clicked
        return html.Div()

    # Return the graph
    return dcc.Graph(figure=fig)



@app.callback(
    Output("graph-container-8", "children"),
    [Input("show-overs-graph-btn-8", "n_clicks"),
     Input("show-wickets-graph-btn-8", "n_clicks"),
     Input("show-average-graph-btn-8", "n_clicks"),
     Input("show-economy-graph-btn-8", "n_clicks"),
     Input("show-strikerate-graph-btn-8", "n_clicks"),
     Input("show-dotballs-graph-btn-8", "n_clicks"),
     Input("show-runsgiven-graph-btn-8", "n_clicks")],
    State("graph-container-8", "children")
)
def update_chart_8(overs_n_clicks, wickets_n_clicks,average_n_click,economy_n_click,strikerate_n_click,dotballs_n_clicks,runsgiven_n_clicks, current_children):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]


    

    if button_id == "show-overs-graph-btn-8":
        # Get the data from the 'OVERSBAN21' collection
        data = overs_data_ned
        x = [d["PlayerNed"] for d in data]
        y = [d["OversNed"] for d in data]

        colors = ['#00BFFF', '#ADD8E6', '#87CEFA', '#6495ED', '#1E90FF']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Total No of Overs Bowled",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-wickets-graph-btn-8":
        # Get the data from the 'WICKETSBAN21' collection
        data = wickets_data_ned
        x = [d["PlayerNed"] for d in data]
        y = [d["WicketsNed"] for d in data]

        colors = ['#00BFFF', '#ADD8E6', '#87CEFA', '#6495ED', '#1E90FF']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=y, y=x, orientation='h', marker=dict(color=color_values))])
        fig.update_layout(title="Wickets taken",
                          plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')


    elif button_id == "show-average-graph-btn-8":
        # Get the data from the 'AVERAGEBAN21' collection
        data = average_data_ned
        x = [d["PlayerNed"] for d in data]
        y = [d["AverageNed"] for d in data]

        colors = ['#00BFFF', '#ADD8E6', '#87CEFA', '#6495ED', '#1E90FF']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowler's Average",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-economy-graph-btn-8":
    # Get the data from the 'ECONOMYBAN21' collection
        data = economy_data_ned
        x = [d["PlayerNed"] for d in data]
        y = [d["EconomyNed"] for d in data]
        fig = go.Figure([go.Scatter(x=x, y=y, mode='lines+markers', line=dict(color='#615D6C'))])
        fig.update_layout(title="Bowler's Economy",
                       plot_bgcolor='#0C8AF0',
                       paper_bgcolor='#0C8AF0',
                       font_color='white')

    elif button_id == "show-strikerate-graph-btn-8":
        # Get the data from the 'STRIKERATEBAN21' collection
        data = strike_rate_data_ned
        x = [d["PlayerNed"] for d in data]
        y = [d["StrikeRateNed"] for d in data]

        colors = ['#00BFFF', '#ADD8E6', '#87CEFA', '#6495ED', '#1E90FF']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Bowling Strike Rates",
                           plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    elif button_id == "show-dotballs-graph-btn-8":
        # Get the data from the 'DOTBALLSBan21' collection
        data = dot_balls_data_ned
        labels = [d["PlayerNed"] for d in data]
        values = [d["DotBallsNed"] for d in data]
        fig = go.Figure([go.Pie(labels=labels, values=values,marker=dict(colors=['#30274D', '#694F5D', '#8B6B7B', '#B0838D', '#C99DA3', '#DEBEBE', '#EFEFEF', '#FFFFFF']), hole=0.4)])
        fig.update_layout(title="Dot Balls Data",
                          plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')


    elif button_id == "show-runsgiven-graph-btn-8":
        # Get the data from the 'RUNSGIVENSSL19' collection
        data = runs_given_data_ned
        x = [d["PlayerNed"] for d in data]
        y = [d["RunsGivenNed"] for d in data]


        colors = ['#00BFFF', '#ADD8E6', '#87CEFA', '#6495ED', '#1E90FF']

        color_values = [colors[i % len(colors)] for i in range(len(x))]

        fig = go.Figure([go.Bar(x=x, y=y,marker=dict(color=color_values))])
        fig.update_layout(title="Runs Conceded",
                          plot_bgcolor='#0C8AF0',
                          paper_bgcolor='#0C8AF0',
                          font_color='white')

    else:
        # Return an empty div if no button has been clicked
        return html.Div()


    return dcc.Graph(figure=fig)
# Start the app
