import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import pandas as pd
import pymongo
import dash_bootstrap_components as dbc
import plotly.graph_objs as go






client = pymongo.MongoClient('mongodb://localhost:27017/')# Connecting to the MongoDB
db = client['AnalyzingDataset']
collection = db['Player_Average_Prediction']
future_data_collection=db['FUTUREDATA']

data = pd.DataFrame(list(collection.find()))# Loading the  data from MongoDB collection into a pandas DataFrame

# Defining the Dash app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,
                                      'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'])


# Defining the UI layout of the app
layout = html.Div([
  
   html.Div([
  html.H1("PLAYER COMPARISON SECTION", style={'text-align': 'center', 'font-weight': 'bold','color': 'white'})
], style={'padding-top': '50px'}),
html.H1("PLAYER PERFORMANCE (2022-PRESENT)", style={'font-size': '25px', 'text-align': 'center', 'font-weight': 'bold','color': 'black','padding-top':'20px'}),
dbc.Input(id='input-box', type='text', placeholder='Enter player name (Ex: Search for names like AF MILNE, TG SOUTHEE ...)',style={'margin-left':'350px', 'width': '50%','justify-content': 'center'}),
    dbc.Button('SEARCH', id='button', style={'margin-top': '20px','text-align': 'center', 'font-weight': 'bold', 'display': 'inline-block', 'justify-content': 'center','margin-left': '690px'}),
    html.Div(id='output-container2',style={'color': 'black'}),
  
    html.Div([
        html.Div([
            html.H3("ENTER YOUR PLAYER'S AVERAGE VALUE:",style={'font-size': '25px', 'font-weight': 'bold','color': 'white'}),
            dbc.Input(id='avg-input', type='text', value=0, style={'margin': 'auto','width': '600px'}),
        ], style={'padding': '20px', 'text-align': 'center', 'display': 'inline-block', 'vertical-align': 'top'}),
        
        html.Div([
            html.H3("ENTER THE NUMBER OF MATCHES PLAYED BY THE PLAYER:",style={'font-size': '25px', 'font-weight': 'bold', 'color': 'white'}),
            dbc.Input(id='matches-input', type='text', value=0, style={'margin': 'auto','width': '600px'}),
        ], style={'padding': '20px', 'text-align': 'center', 'display': 'inline-block', 'vertical-align': 'top'}),
        
        html.Div([
            dbc.Button('RUN SCAN', id='submit-button', style={'margin-top': '20px','font-weight': 'bold','width': '600px', 'display': 'inline-block'}),
        ], style={'text-align': 'center', 'display': 'inline-block', 'vertical-align': 'top'}),
        
    ], style={'padding': '20px','text-align': 'center'}),
    
    html.Div(id='output-containerP', children=[
        dcc.Interval(id='interval-component', interval=500, n_intervals=0),
        html.Div([
            html.H2('Table', style={'text-align': 'center'}),
            dcc.Graph(
                id='table-graph',
                figure={},
                style={'backgroundColor': '#3579B9','margin-right':'100px'}
            ),
        ], style={'margin-right':'100px','padding': '20px ', 'width': '50%'}),
    ])

],style={ 'background-color': '#838790','color': 'white'})


@app.callback(
    dash.dependencies.Output('output-container2', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')]
)
def search_player(n_clicks, player_name):
    if player_name:
     
        records = future_data_collection.find({'Player': player_name})   # Searching for records with the given player name
        
   
        df = pd.DataFrame(records, columns=['Year','Opponent','Matches', 'Bowling_Style', 'Runs_Conceded', 'Overs', 'Wickets'])     # Converting records to a pandas dataframe
        
        # If dataframe is empty, display an alert message
        if df.empty:
            alert = dbc.Alert("Oops! no record relating to that Name is found, Be careful with the spellings, upper case and lower case of the Names you enter ", color="warning")
            return alert
        
        # Generating HTML table from dataframe
        table = dbc.Table.from_dataframe(
            df, 
            striped=True, 
            bordered=True, 
            hover=True,
            responsive=True,
            className='table-sm',
        )
        
        # Return HTML table
        return table
    else:
        return ''
    
#Defining the callback function to initiate the selecting the optimum player using K-NN Algorithm 
@app.callback(
    Output('output-containerP', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('avg-input', 'value'),
     State('matches-input', 'value')]
)
def update_graph(n_clicks, avg_value, num_matches):   # Initializing output_msg with default message
   
    output = html.Div("No Matching Players is Found yet.", style={'text-align': 'center', 'height': '600px'})
    
    
    all_players = list(collection.find({}, {'_id': 0})) # Getting all players from the MongoDB collection
        
    if len(all_players) == 0:
        output = html.Div("No players found in the database.")
    else:
        matching_player = None
        min_distance = float('inf')

        # Loop for over all players to find the one closest to input values
        for p in all_players:
            avg_diff = abs(float(p['Average']) - float(avg_value))
            matches_diff = abs(int(p['Matches']) - int(num_matches)) if p['Matches'] is not None else float('inf')

            distance = (avg_diff**2 + matches_diff**2)**0.5
            
            if distance < min_distance:
                db_player = collection.find_one({'Player': p['Player']})
                
                # Checking if the matching player's details have been updated in the MongoDB collection
                if db_player:
                    db_avg_diff = abs(float(db_player['Average']) - float(avg_value))
                    db_matches_diff = abs(int(db_player['Matches']) - int(num_matches)) if db_player['Matches'] is not None else float('inf')
                    db_distance = (db_avg_diff**2 + db_matches_diff**2)**0.5

                    
                    if db_distance <= distance:
                        matching_player = db_player
                        min_distance = db_distance

                else:
                    matching_player = p
                    min_distance = distance
            

            
       
            # Generating data for table and bar chart figures for the matching player
            table_data = [['Player', matching_player['Player']], ['Average', matching_player['Average']], ['Matches', matching_player['Matches']]]
           
            # Creating figure for table
            table_fig = go.Figure(data=[go.Table(header=dict(values=['Attribute', 'Value']),
                                                 cells=dict(values=list(zip(*table_data)),
                                                 font=dict(size=18),
                                                 height=40))], layout=dict(paper_bgcolor='#2E4C87',plot_bgcolor='#2E4C87'))


            # Creating wheel animation layout
            wheel_layout = {
                'width': '100%',
                'height': '300px',
                'margin': 'auto',
                'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center'
            }

            # Wrapping the pie chart in a div with wheel animation layout
            output = html.Div([
                html.H1("Performance Statistics", style={'margin-top':'40px','text-align': 'center', 'color': 'white','font-weight':'bold'}),
                
                dcc.Graph(
                    figure=table_fig,
                   style={'width': '50%', 'height': '300%', 'display': 'block', 'margin': 'auto'}
                ),
                html.H2(matching_player['Player'], style={'text-align': 'center', 'font-weight': 'bold', 'margin-top': '50px'}),
                html.Div([
                    html.I(className='fa fa-spinner fa-spin fa-5x fa-fw', style={'color': 'white'})
                ], style=wheel_layout)
            ],style={'padding':'100px'})
        
    return output
