import dash
from dash import html
from dash import dcc
import pymongo
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from dash import dash_table
import dash_html_components as html



client = pymongo.MongoClient('mongodb://localhost:27017/')# Connection to the MongoDB database


db = client['AnalyzingDataset']
collection = db['Player_Average_Prediction']# Selecting the specific database and collection from MongoDB


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,'https://use.fontawesome.com/releases/v5.7.2/css/all.css'])# Defining the Dash app layout




   



layout = html.Div([         # Defining the layout of the app
   
  
html.Div(id='page-content'),
    html.H1('UPDATE SECTION', style={'text-align': 'center', 'font-weight': 'bold','padding-top':'50px','color': 'white'}),
    html.Div([
        html.H1("INSERT STATS IN TO THE COLLECTION (CAREER PERFORMANCE STATISTICS)",style={'font-size':'20px','text-align': 'left', 'font-weight': 'bold','margin-top': '10px','color': 'white'}),
        html.H1(" Player Name",style={'font-size':'20px','text-align': 'left','margin-top': '20px','color': 'white'}),
        dbc.Input(id="player_input", placeholder="Player",required=True),
        html.H1("Matches Played",style={'font-size':'20px','text-align': 'left','margin-top': '20px','color': 'white'}),
        dbc.Input(id="matches_input", placeholder="Matches", required=True),
        html.H1("Wickets Taken by the Player",style={'font-size':'20px','text-align': 'left','margin-top': '20px','color': 'white'}),
        dbc.Input(id="wickets_input", placeholder="Wickets", required=True, min=0),
        html.H1("Runs Conceded by the Player",style={'font-size':'20px','text-align': 'left','margin-top': '20px','color': 'white'}),        
        dbc.Input(id="runs_given_input", placeholder="Runs Given", required=True, min=0),
        html.H1("Bowling Type (i.e Spin or Seam)",style={'font-size':'20px','text-align': 'left','margin-top': '20px','color': 'white'}),        
        dbc.Input(id="bowling_type_input", placeholder="Bowling Style", required=True),
        html.H1("Role in the Team (i.e Part-Timer or Main Bowler)",style={'font-size':'20px','text-align': 'left','margin-top': '20px','color': 'white'}),
        dbc.Input(id="role_input", placeholder="Role", required=True, style={"margin-top": "10px", "margin-bottom": "10px"}),
        dbc.Button("Update the Collection", id="submit", disabled=True, style={"margin-right": "10px"}),
        dbc.Button("Clear", id="clear-button", style={"background-color": "#050B14"}),
        html.Div(id="output-message",style={'font-size':'20px','width':'267px', 'font-weight': 'bold','color': 'white','background-color':'green'}), # Adding a Div component with the ID "output-message"
        html.Div([    
        html.H1("View Collection (Player Stats in New Zealand from 2018-Present)", style={'font-size':'20px','text-align': 'left', 'font-weight': 'bold','margin-top': '10px','color': 'white'}),    
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

    ],style={'padding': '80px'}),# Defining the table component to display the data from the collection
  
],style={'background-color': '#2E4C87'})





@app.callback(                  #Defining a callback function to validate the input fields based on all filled fields
    Output('submit', 'disabled'),
    Input('player_input', 'value'),
    Input('matches_input', 'value'),
    Input('wickets_input', 'value'),
    Input('runs_given_input', 'value'),
    Input('bowling_type_input', 'value'),
    Input('role_input', 'value')
)
def update_submit2_button2(player, matches, wickets, runs_given, bowling_type, role):
    if player and matches and wickets and runs_given and bowling_type and role:
        return False
    else:
        return True








@app.callback(                              # Defining a single callback function to handle both updating the database and displaying the data in a table
    [Output('output-message', 'children'),
     Output('table', 'data')],
    [Input('submit', 'n_clicks')],
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
        
        if wickets is not None and runs is not None:  # Calculating the average of a player with the inserted
            average = float(runs) / float(wickets)
        else:
            average = 0.0

     
        new_data = {                           
        # Inserting the data into the collection
            'Player': player,
            'Matches': matches,
            'Wickets': wickets,
            'Runs Given': runs,
            'Average': average,
            'Bowling Type': type,
            'Role': role
        }
        collection.insert_one(new_data)
        
       
        data = list(collection.find())# Retrieving the data from the database and convert the 'Average' field to a numeric value
        for d in data:
            d['Average'] = float(d['Average'])


        table = [  # Creating an HTML table to display the data
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

        
      
        ctx = dash.callback_context       # Checking if this callback was triggered by the submit button
        if ctx.triggered[0]['prop_id'] == 'submit-button.n_clicks':
            return 'Collection is Updated!.', table
        else:
            return '', table



@app.callback(                      # Defining a new callback function to clear the input fields
    [Output('player_input', 'value'),
     Output('matches_input', 'value'),
     Output('wickets_input', 'value'),
     Output('runs_given_input', 'value'),
     Output('bowling_type_input', 'value'),
     Output('role_input', 'value')],
    [Input('clear-button', 'n_clicks')]
)
def clear_inputs(n_clicks):
    if n_clicks is not None:
        return '', '', '', '', '', ''
    else:
        return dash.no_update


