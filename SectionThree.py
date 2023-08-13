from turtle import pd
import dash
import dash_bootstrap_components as dbc
from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from pymongo import MongoClient
import time
import plotly.graph_objs as go
import plotly.express as px
import pymongo
import pandas as pd



client = MongoClient('mongodb://localhost:27017/') # Connecting to the MongoDB and relevant collection
db = client['AnalyzingDataset']
collection = db['FUTUREDATA']


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP]) # Creating  a Dash app


layout = html.Div([                         # Defining the layout of the app
html.H1('NEW PLAYER RECORDS (SERIES STATISTICS) ', style={'font-weight':'bold','text-align':'center'}),

html.Div([
  html.Div([
   html.H1(" ENTER THE SPECIFIC YEAR",style={'font-size':'20px','font-weight':'bold','text-align': 'left','margin-top': '20px','color': 'white'}),
    dbc.Input(id='year-input', type='text', placeholder=" Year",required=True)
  ], style={'display': 'flex', 'flex-direction': 'column'}),

html.Div([
   html.H1(" ENTER THE NUMBER OF MATCHES PLAYED",style={'font-size':'20px','font-weight':'bold','text-align': 'left','margin-top': '20px','color': 'white'}),
    dbc.Input(id='matches-input', type='text', placeholder=" Matches Played",required=True)
  ], style={'display': 'flex', 'flex-direction': 'column'}),



  html.Div([
    html.H1(" ENTER THE NAME OF THE OPPOSITION TEAM",style={'font-size':'20px','font-weight':'bold','text-align': 'left','margin-top': '20px','color': 'white'}),
    dbc.Input(id='opponent-input', type='text', placeholder=" Country Name",required=True)
  ], style={'display': 'flex', 'flex-direction': 'column'}),

  html.Div([
    html.H1(" ENTER THE PLAYER NAME",style={'font-size':'20px','font-weight':'bold','text-align': 'left','margin-top': '20px','color': 'white'}),
    dbc.Input(id='player-input', type='text', placeholder="Player Name...",required=True)
  ], style={'display': 'flex', 'flex-direction': 'column'}),


html.Div([
    html.H1(" ENTER THE BOWLING STYLE OF THE BOWLER",style={'font-size':'20px','font-weight':'bold','text-align': 'left','margin-top': '20px','color': 'white'}),
    dbc.Input(id='bowling_style-input', type='text', placeholder=" Ex: Spin or Seam",required=True)
  ], style={'display': 'flex', 'flex-direction': 'column'}),

  html.Div([
   html.H1(" ENTER THE NUMBER OF RUNS CONCEDED BY THE BOWLER",style={'font-size':'20px','font-weight':'bold','text-align': 'left','margin-top': '20px','color': 'white'}),
    dbc.Input(id='runs-input', type='text', placeholder=" Runs Conceded by the Bowler",required=True)
  ], style={'display': 'flex', 'flex-direction': 'column'}),

  html.Div([
   html.H1(" ENTER THE NUMBER OF OVERS BOWLED BY THE BOWLER",style={'font-size':'20px','font-weight':'bold','text-align': 'left','margin-top': '20px','color': 'white'}),
    dbc.Input(id='overs-input', type='text', placeholder="Overs Bowled",required=True)
  ], style={'display': 'flex', 'flex-direction': 'column'}),

  html.Div([
     html.H1(" ENTER THE NUMBER WICKETS TAKEN BY THE BOWLER",style={'font-size':'20px','font-weight':'bold','text-align': 'left','margin-top': '20px','color': 'white'}),
    dbc.Input(id='wickets-input', type='text', placeholder="Wickets Taken",required=True)
  ], style={'display': 'flex', 'flex-direction': 'column',"margin-top": "10px"}),

 html.Div([
    dbc.Button('UPDATE THE COLLECTION', id='submit-button', n_clicks=0, disabled=True, style={'margin-right': '10px','background-color':'green'}),
], style={'display': 'flex', 'justify-content': 'center', 'margin-top': '20px'}),
  
  html.Br(),
  
  html.Div(id='output'), # Output div for the results
  html.Div(id='player-stats',style={'padding-top':'20px'}),

   

html.Div([
    html.Div(id='current-data', style={'padding-top':'20px', 'display': 'flex', 'align-items': 'center','padding':'60px'}),#Div to display the processed data in a form of a table
    dbc.Button('REFRESH THE COLLECTION', id='refresh-button', n_clicks=0, style={ 'display': 'flex', 'align-items': 'center'})
]),


 

]),

 
   
], style={'padding': '20px','background-color':'#2E4C87','color':'white','padding':'70px'})

# Defining a variable to store the last timestamp
last_timestamp = 0



#Defining the  callback for the button click event
@app.callback(
    Output('submit-button', 'disabled'),
    Input('year-input', 'value'),
    Input('matches-input', 'value'),
    Input('opponent-input', 'value'),
    Input('player-input', 'value'),
    Input('bowling_style-input', 'value'),
    Input('runs-input', 'value'),
    Input('overs-input', 'value'),
    Input('wickets-input', 'value')
)
def update_submit_button(year, matches_played, opponent_team, player_name, bowling_style, runs_conceded, overs_bowled, wickets_taken):
    if not all([year, matches_played, opponent_team, player_name, bowling_style, runs_conceded, overs_bowled, wickets_taken]):
        return True
    else:
        return False

# Defining the callback function to calculate and display player stats
@app.callback(Output('output', 'children'),
              Output('player-stats', 'children'),
              Input('submit-button', 'n_clicks'),
              State('year-input', 'value'),
              State('matches-input', 'value'),
              State('opponent-input', 'value'),
              State('player-input', 'value'),
              State('bowling_style-input', 'value'),
              State('runs-input', 'value'),
              State('overs-input', 'value'),
              State('wickets-input', 'value'))
def insert_data(n_clicks, year,matches, opponent, player,style, runs, overs, wickets):
    global last_timestamp
    if n_clicks is not None and n_clicks > 0:
        data = {'Year': year,
                'Matches':matches,
                'Opponent': opponent,
                'Player': player,
                'Bowling_Style':style,
                'Runs_Conceded': runs,
                'Overs': overs,
                'Wickets': wickets,
                'Timestamp': time.time()}  # Adding a timestamp to the data
        collection.insert_one(data)
        last_timestamp = data['Timestamp']  # Updating the last timestamp

       # Recalculating player stats
        if runs is not None and wickets is not None and int(wickets) > 0:
            avg = int(runs) / int(wickets)
        else:
            avg = None


        if overs is not None and runs is not None and float(overs) != 0:
            economy = float(runs) / float(overs)
        else:
            economy = None

        if overs is not None and wickets is not None and wickets != 0:
            overs_float = float(overs)
            wickets_int = int(wickets)
            balls = int(overs_float * 6) + (overs_float % 1 * 10)  # Converting overs to balls
            balls += wickets_int % 1 * 6  # Adding the remaining balls after wickets
            overs = int(balls / 6) + (balls % 6) / 10  # Converting back to overs with decimal points
            
            if wickets_int>0:
                strike_rate = balls / wickets_int
            else:
                strike_rate=None
        else:
            overs = None
            strike_rate = None




        labels1 = ['Average', 'Economy', 'Strike Rate']
        values1 = [avg, economy, strike_rate]

        fig = go.Figure()
        fig.add_trace(go.Bar(x=labels1, y=values1,marker=dict(
        color=['#1F2937', '#334155', '#4B5563'],
        line=dict(
            color='#FFFFFF',
            width=1
        )
    )))

        fig.update_layout(
            plot_bgcolor='#0C8AF0',
            paper_bgcolor='#0C8AF0',
            font_color='white',
            xaxis_title='Metrics',
            yaxis_title='Values'
        )

        bar_chart1 = dcc.Graph(figure=fig)

       
    

  
        # Returning success message and new pie charts
        return 'UPDATED THE CURRENT COLLECTION!', html.Div([html.H3('Last record:'),bar_chart1])
    else:
        return '', None
    




@app.callback(Output('current-data', 'children'),
              [Input('refresh-button', 'n_clicks'),
            ])
def display_current_data(n_clicks):
        if n_clicks is not None:
    # Querying the MongoDB collection
            cursor = collection.find({})
            data = [{'Year': doc['Year'],
             'Matches': doc.get('Matches'),
             'Opponent': doc['Opponent'],
             'Player': doc['Player'],
             'Bowling Style': doc.get('Bowling_Style'),
             'Runs Conceded': doc['Runs_Conceded'],
             'Overs': doc['Overs'],
             'Wickets': doc['Wickets']} for doc in cursor]
        else:
            data = []




        
        for row in data:
            if row['Wickets'] is not None and int(row['Wickets']) > 0:
                row['Average'] = int(row['Runs Conceded']) / int(row['Wickets'])
            else:
                    row['Average'] = None


            if row['Overs'] and row['Runs Conceded'] and row['Overs'] != '0':
                row['Economy'] = float(row['Runs Conceded']) / float(row['Overs'])
            else:
                row['Economy'] = None


            if row['Wickets'] is not None and int(row['Wickets']) > 0 and row['Overs'] is not None and row['Overs'] != 0:
                balls = int(float(row['Overs']) * 6 + (float(row['Overs']) % 1 * 10))
                balls += int(row['Wickets']) % 1 * 6
                row['Strike Rate'] = balls / int(row['Wickets'])
            else:
                row['Strike Rate'] = None

            # Calculating Lemmer's Bowling Performance for each row
     
            if row['Wickets'] is not None:
                lbp = (int(row['Wickets']) * 25) - (float(row['Runs Conceded']) * float(row['Economy']))
                row['Overall Bowling Performance'] = lbp
            else:
                row['Overall Bowling Performance'] = None

       



        # Create a table with the current data
        table = html.Table([
            html.Thead(html.Tr([
                html.Th('Year', className='bg-primary text-white'),
                 html.Th('Matches', className='bg-primary text-white'),
                html.Th('Opponent', className='bg-primary text-white'),
                html.Th('Player', className='bg-primary text-white'),
                html.Th('Bowling Style', className='bg-primary text-white'),
                html.Th('Runs Conceded', className='bg-primary text-white'),
                html.Th('Overs', className='bg-primary text-white'),
                html.Th('Wickets', className='bg-primary text-white'),
                html.Th('Average', className='bg-primary text-white'),
                html.Th('Economy', className='bg-primary text-white'),
                html.Th('Strike Rate', className='bg-primary text-white'),
                html.Th('Overall Bowling Performance', className='bg-primary text-white')
            ])),
            html.Tbody([
                html.Tr([
                    html.Td(row['Year'], className='text-center', style={'color': 'white'}),
                    html.Td(row['Matches'], className='text-center', style={'color': 'white'}),
                    html.Td(row['Opponent'], style={'color': 'white'}),
                    html.Td(row['Player'], style={'color': 'white'}),
                     html.Td(row['Bowling Style'], style={'color': 'white'}),
                    html.Td(row['Runs Conceded'], className='text-center', style={'color': 'white'}),
                    html.Td(row['Overs'], className='text-center', style={'color': 'white'}),
                    html.Td(row['Wickets'], className='text-center', style={'color': 'white'}),
                    html.Td(f"{row['Average']:.2f}" if row['Average'] is not None else '', className='text-center', style={'color': 'white'}),
                    html.Td(f"{row['Economy']:.2f}" if row['Economy'] is not None else '', className='text-center', style={'color': 'white'}),
                    html.Td(f"{row['Strike Rate']:.2f}" if row['Strike Rate'] is not None else '', className='text-center', style={'color': 'white'}),
                    html.Td(f"{row['Overall Bowling Performance']:.2f}" if row['Overall Bowling Performance'] is not None else '', className='text-center', style={'color': 'white'})
                ]) for row in data
            ])
        ], className='table table-striped table-bordered')
        
        # Return the table
        return table
        
 




