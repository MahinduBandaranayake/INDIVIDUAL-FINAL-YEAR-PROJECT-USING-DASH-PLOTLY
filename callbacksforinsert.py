from http import client
import dash
from dash import html
from dash import dcc
import pymongo
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from dash import dash_table
import dash_html_components as html

client = pymongo.MongoClient("mongodb://localhost:27017/")


db = client['AnalyzingDataset']
collection = db['Player_Average_Prediction']
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,'https://use.fontawesome.com/releases/v5.7.2/css/all.css'])
app.layout = html.Div([
   
  
html.Div(id='page-content'),
    html.H1('UPDATE SECTION', style={'text-align': 'center', 'font-weight': 'bold','padding-top':'50px','color': 'white'}),
    html.Div([
        html.H1("INSERT STATS IN TO THE COLLECTION (CAREER PERFORMANCE STATISTICS)",style={'font-size':'20px','text-align': 'left', 'font-weight': 'bold','margin-top': '10px','color': 'white'}),
        html.H1(" Player Name",style={'font-size':'20px','text-align': 'left','margin-top': '20px','color': 'white'}),
        dbc.Input(id="player_input", placeholder="Player"),
        html.H1("Matches Played",style={'font-size':'20px','text-align': 'left','margin-top': '20px','color': 'white'}),
        dbc.Input(id="matches_input", placeholder="Matches"),
        html.H1("Wickets Taken by the Player",style={'font-size':'20px','text-align': 'left','margin-top': '20px','color': 'white'}),
        dbc.Input(id="wickets_input", placeholder="Wickets"),
        html.H1("Runs Conceded by the Player",style={'font-size':'20px','text-align': 'left','margin-top': '20px','color': 'white'}),        
        dbc.Input(id="runs_given_input", placeholder="Runs Given"),
        html.H1("Bowling Type (i.e Spin or Seam)",style={'font-size':'20px','text-align': 'left','margin-top': '20px','color': 'white'}),        
        dbc.Input(id="bowling_type_input", placeholder="Bowling Style"),
        html.H1("Role in the Team (i.e Part-Timer or Main Bowler)",style={'font-size':'20px','text-align': 'left','margin-top': '20px','color': 'white'}),
        dbc.Input(id="role_input", placeholder="Role", style={"margin-top": "10px", "margin-bottom": "10px"}),
        dbc.Button("Update the Collection", id="submit-button", style={"margin-right": "10px"}),
        dbc.Button("Clear", id="clear-button", style={"background-color": "#050B14"}),
        html.Div(id="output-message",style={'font-size':'20px','width':'267px', 'font-weight': 'bold','color': 'white','background-color':'green'}), # Add a Div component with the ID "output-message"
        html.Div([    
        html.H1("View Collection (Player Stats in New Zealand from 2018-2022)", style={'font-size':'20px','text-align': 'left', 'font-weight': 'bold','margin-top': '10px','color': 'white'}),    
        dash_table.DataTable(        id='table',        columns=[            {'name': 'Player', 'id': 'Player'},            {'name': 'Matches', 'id': 'Matches'},            {'name': 'Wickets', 'id': 'Wickets'},            {'name': 'Runs Given', 'id': 'Runs Given'},            {'name': 'Average', 'id': 'Average'},            {'name': 'Bowling Type', 'id': 'Bowling Type'},            {'name': 'Role', 'id': 'Role'}        ],
        data=[],
        style_cell={
            'textAlign': 'center',
            'font_family': 'Helvetica',
            'font_size': '14px',
            'padding': '10px',
            'height': 'auto',
            'minWidth': '0px', 'maxWidth': '180px',
            'whiteSpace': 'normal',
            'border': '1px solid grey',
            'backgroundColor': 'white'
        },
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold',
            'border': '1px solid grey',
            'textAlign': 'center',
            'padding': '10px',
            'font_family': 'Helvetica',
            'font_size': '16px'
        },
        style_data_conditional=[            {                'if': {'row_index': 'odd'},                'backgroundColor': 'white'            }        ]
    )
])

    ],style={'padding': '80px'}),# Define the table component to display the data from the collection
  
],style={'background-color': '#2E4C87'})



@app.callback(
    [Output('output-message', 'children'),
     Output('table', 'data')],
    [Input('submit-button', 'n_clicks')],
    [State('player_input', 'value'),
     State('matches_input', 'value'),
     State('wickets_input', 'value'),
     State('runs_given_input', 'value'),
     State('bowling_type_input', 'value'),
     State('role_input', 'value')],
    [State('table', 'data')]
)
def update_data(n_clicks, player, matches, wickets, runs, type, role, table_data):
    if n_clicks is None:
        return '', table_data
    else:
        # Calculate the average
        if wickets is not None and runs is not None:
            average = float(runs) / float(wickets)
        else:
            average = 0.0

        
        # Insert the data into the collection
        new_data = {
            'Player': player,
            'Matches': matches,
            'Wickets': wickets,
            'Runs Given': runs,
            'Average': average,
            'Bowling Type': type,
            'Role': role
        }
        collection.insert_one(new_data)
        
       # Retrieve the data from the database and convert the 'Average' field to a numeric value
        data = list(collection.find())
        for d in data:
            d['Average'] = float(d['Average'])

# Create an HTML table to display the data
        table = [
        {
        'Player': d['Player'],
        'Matches': d['Matches'],
        'Wickets': d['Wickets'],
        'Runs Given': d['Runs Given'],
        'Average': round(d['Average'], 2),
        'Bowling Type': d['Bowling Type'],
        'Role': d['Role']
    } for d in data
]

        
       