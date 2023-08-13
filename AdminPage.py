import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
from pymongo import MongoClient
import dash_bootstrap_components as dbc
import dash_table
import pymongo



client = MongoClient('mongodb://localhost:27017/')
db = client['AnalyzingDataset']
collection = db['Player_Average_Prediction']

futuredata_collection=db["FUTUREDATA"]

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,'https://use.fontawesome.com/releases/v5.7.2/css/all.css'])# Creation of a Dash app




layout = html.Div([# Defining the layout to enable a UI for deletion
  
html.H1('REVISE SECTION', style={'font-weight':'bold','text-align':'center','padding-top': '50px','color': 'white'}),
    dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('DELETE PLAYER RECORD FROM CAREER PERFORMANCE STATISTICS', className='mt-3',style={'text-align':'center','padding-top':'20px','color':'white','font-weight':'bold','font-size':'20px'}))
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Input(id='input-player-name', type='text', placeholder='Enter player name (Ex: Type Player Names such as Cde Grandhomme, Lockie Ferguson etc...)', className='form-control mb-2',style={'padding':'20px'}),
            
            html.Button('DELETE', id='delete-button', className='btn btn-danger mr-2'),
            
        ], width={'size': 6, 'offset': 3})
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='output-message-2', className='mt-3'))
    ]),
    dbc.Row([
        dbc.Col(html.Br())
    ]),
  

    
]),
 dbc.Row([
        dbc.Col(html.H1("DELETE NEW ENTRIES FROM NEW RECORDS",style={'text-align':'center','padding-top':'20px','color':'white','font-weight':'bold','font-size':'20px'}))
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Select the specific Player:",style={'padding-top':'20px','color':'white','font-weight':'bold','font-size':'20px'}),
            dcc.Dropdown(
                id='player-dropdown',
                options=[{'label': player['Player'], 'value': player['Player']} for player in futuredata_collection.find()],
                placeholder='Select a player...'
            )
        ], width=6, className='offset-3')
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Select the specific Year:",style={'padding-top':'20px','color':'white','font-weight':'bold','font-size':'20px'}),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': year, 'value': year} for year in futuredata_collection.distinct('Year')],
                placeholder='Select a year...'
            )
        ], width=6, className='offset-3 mt-3')
    ]),
    dbc.Row([
        dbc.Col(dbc.Button("DELETE RECORD", id='delete-button2', color='danger', className='mt-3'), width=6, className='offset-3')
    ]),
    dbc.Row([
        dbc.Col(id='output-messageDATA', width=6, className='offset-3')
    ])
    
], style={'background-color': '#2E4C87', 'height': '100vh'})





def delete_future_data(player_name, year):# Defining the function to delete a record
    query = {'Player': player_name, 'Year': year}#Defining paramters to check and identify
   
    result = futuredata_collection.delete_one(query) #Collecting the identified details to delete in an array
  
    if result.deleted_count > 0:  #Exception handling 
        return dbc.Alert(f'{result.deleted_count} record relating to the player {player_name} in the year {year} has been deleted', color='success', className='mt-3')
    else:
        return dbc.Alert(f'No record found for player {player_name} in the year {year}.', color='warning', className='mt-3')



@app.callback(# Defining the app callback to delete a record
    Output('output-messageDATA', 'children'),
    Input('delete-button2', 'n_clicks'),
    State('player-dropdown', 'value'),
    State('year-dropdown', 'value')
)
def delete_record_callback2(n_clicks, player_name, year): # Checking if the selected player exists in the collection
    if n_clicks:

        query = {'Player': player_name}#Defining paramters to check and identify
        player_data = futuredata_collection.find_one(query)
        if player_data:                                         #Exception handling
            return delete_future_data(player_name, year)
        else:
            return dbc.Alert(f'Player {player_name} not found in the collection.', color='warning', className='mt-3')











def delete_record(player_name):# Defining the delete function
    query = {'Player': player_name}#Defining paramters to check and identify
    result = collection.delete_one(query)
    if result.deleted_count > 0:                #Exception handling
        return dbc.Alert(f'{result.deleted_count} Record relating to the  Player {player_name} is Deleted', color='danger', className='mt-3')
    else:
        return dbc.Alert(f'Oops there is no such record found for that player, Please make sure of the Spellings (Upper case and Lower case) {player_name}.', color='warning', className='mt-3')


@app.callback(# Defineing the app callback to delete the record
    Output('output-message-2', 'children'),
    Input('delete-button', 'n_clicks'),
    State('input-player-name', 'value')
)
def delete_record_callback(n_clicks, player_name):
    if n_clicks:
        return delete_record(player_name)



