import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Input, Output, State
from pymongo import MongoClient
from bson.objectid import ObjectId
from dash import dash_table
from dash.dash_table import Format
import plotly.graph_objs as go



client = MongoClient('mongodb://localhost:27017/') #Defining the connection string to the database
db = client['AnalyzingDataset']
collections = {                                    #Retrievig data from each and every collection in the database
    "mspakvsnz18": db["MSPAKVSNZ18"],
    "msbanvsnz19": db["MSBANVSNZ19"],
    "msbanvsnz2021": db["MSBANVSNZ2021"],
    "msengvsnz18": db["MSENGVSNZ18"],
    "msindvsnz19": db["MSINDVSNZ19"],
    "msindvsnz20": db["MSINDVSNZ20"],
    "msnedvsnz22": db["MSNEDVSNZ22"],
    "msslvsnz19": db["MSSLVSNZ19"],

    "bl2018pak": db["BL2018PAK"],
    "bl2018eng": db["BL2018ENG"],
    "bl2019ban": db["BL2019BAN"],
    "bl2019ind": db["BL2019IND"],
    "bl2019sl": db["BL2019SL"],
    "bl2020ind": db["BL2020IND"],
    "bl2021ban": db["BL2021BAN"],
    "bl2022ned": db["BL2022NED"]
}


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,
                                      'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css']) #Defining the dash app



#Creating the UI Layout to connect the database collection to the button click events
  
layout = html.Div([    
     html.H1("PAST RECORDS",style={'text-align': 'center', 'font-weight': 'bold','color': 'white'}),
      html.H1("MATCH SUMMARIES (2018-2022)",style={'font-size':'20px','text-align': 'center', 'font-weight': 'bold','color': 'white','margin-top':'35px'}),
              html.Div([        dbc.Button('2018 PAK vs NZ', id='pak-nz-2018-button', n_clicks=0, style={'margin-right': '5px'}), 
                               
dbc.Button('2018 ENG vs NZ', id='eng-nz-2018-button', n_clicks=0,  style={'margin-right': '5px'}), 
dbc.Button('2019 BAN vs NZ', id='ban-nz-2019-button', n_clicks=0, style={'margin-right': '5px'}),        
dbc.Button('2019 IND vs NZ', id='ind-nz-2019-button', n_clicks=0, style={'margin-right': '5px'}),
dbc.Button('2019 SL vs NZ',  id='sl-nz-2019-button', n_clicks=0, style={'margin-right': '5px'}),    
dbc.Button('2021 BAN vs NZ', id='ban-nz-2021-button', n_clicks=0, style={'margin-right': '5px'}),       
dbc.Button('2020 IND vs NZ', id='ind-nz-2020-button', n_clicks=0, style={'margin-right': '5px'}),       
dbc.Button('2022 NED vs NZ', id='ned-nz-2022-button', n_clicks=0, style={'margin-right': '5px'}),       
   ],style={'text-align': 'center'}),
html.Div([        html.Div(id='table-container')    
          ],style={'padding':'60px','margin-left':'510px','color': 'white',}),


html.Div([
html.H1("BOWLERS PLAYER LIST BASED ON THE ABOVE SERIES OF MATCHES (2018-2022)",style={'font-size':'20px','text-align': 'center', 'font-weight': 'bold','color': 'white'}),
              html.Div([        
dbc.Button('2018 NZ LIST-1', id='2018-list-pak-button', n_clicks=0, style={'margin-right': '5px'}), 
                               
dbc.Button('2018 NZ  LIST-2', id='2018-list-eng-button', n_clicks=0,  style={'margin-right': '5px'}), 
dbc.Button('2019  NZ LIST-1  ', id='2019-list-ban-button', n_clicks=0, style={'margin-right': '5px'}),        
dbc.Button('2019 NZ LIST-2', id='2019-list-ind-button', n_clicks=0, style={'margin-right': '5px'}),
dbc.Button('2019 NZ LIST-3 ',  id='2019-list-sl-button', n_clicks=0, style={'margin-right': '5px'}),        
dbc.Button('2021 NZ LIST ', id='2021-list-ban-button', n_clicks=0, style={'margin-right': '5px'}),       
dbc.Button('2020 NZ LIST ', id='2020-list-ind-button', n_clicks=0, style={'margin-right': '5px'}),       
dbc.Button('2022 NZ LIST ', id='2022-list-ned-button', n_clicks=0, style={'margin-right': '5px'}),       
   ],style={'text-align': 'center'}),
html.Div([        html.Div(id='table-container')    
          ],style={'margin-top':'65px','padding':'65px','color': 'white','height':'400px','width':'550px','border-radius':'5px','border': '2px solid white','margin-left':'450px' }),
html.H1("PERFORMANCE LEVEL IN EACH GROUND (2018-Present)",style={'font-size':'20px','text-align': 'center', 'font-weight': 'bold','color': 'white','margin-top':'35px'}),
html.Div([
    dbc.Button('Show Ground Statistics', id='show-ground-statistics', n_clicks=0, className='mr-2')
],style={'text-align': 'center','padding':'20px'}),
html.Div(id='ground-statistics')
]),




],style={ 'background-color': '#2E4C87','padding':'40px'})








#Defining a function to query the database collection to and list the table headers and populate the row values in order


def display_data(collection_name):
    collection = db[collection_name]
    data = list(collection.find())
    table_header = [html.Thead(html.Tr([html.Th(k) for k in data[0].keys() if k != '_id']))] if data else []
    table_rows = []
    for row in data:
        table_row = []
        for key, val in row.items():
            if key != '_id':
                table_row.append(val)
        table_rows.append(html.Tr([html.Td(val) for val in table_row]))
    table = table_header + [html.Tbody(table_rows)]
    return html.Table(table)


#Defining the callback function to connect the relevant database collection to the relevant button


@app.callback(
    Output('table-container', 'children'),
    [Input('pak-nz-2018-button', 'n_clicks'),
     Input('ban-nz-2019-button', 'n_clicks'),
     Input('sl-nz-2019-button', 'n_clicks'),
     Input('eng-nz-2018-button', 'n_clicks'),
     Input('ind-nz-2019-button', 'n_clicks'),
     Input('ban-nz-2021-button', 'n_clicks'),
     Input('ind-nz-2020-button', 'n_clicks'),
     Input('ned-nz-2022-button', 'n_clicks'),
     Input('2018-list-pak-button', 'n_clicks'),
     Input('2018-list-eng-button', 'n_clicks'),
     Input('2019-list-ban-button', 'n_clicks'),
     Input('2019-list-ind-button', 'n_clicks'),
     Input('2021-list-ban-button', 'n_clicks'),
     Input('2020-list-ind-button', 'n_clicks'),
     Input('2022-list-ned-button', 'n_clicks'),
     Input('2019-list-sl-button', 'n_clicks')
     ],
)
def update_table(pak_nz_2018_btn, ban_nz_2019_btn, sl_nz_2019_btn,eng_nz_2018_btn,ind_nz_2019_btn,ban_nz_2021_btn,ind_nz_2020_btn,ned_nz_2022_btn,pak_bowling_2018_btn, ban_bowling_2019_btn, sl_bowling_2019_btn,eng_bowling_2018_btn,ind_bowling_2019_btn,ban_bowling_2021_btn,ind_bowling_2020_btn,ned_bowling_2022_btn):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = ''
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    collection_name = ''  # Initializing each variable
    
    if button_id == 'pak-nz-2018-button':
        collection_name = 'MSPAKVSNZ18'
    elif button_id == 'ban-nz-2019-button':
        collection_name = 'MSBANVSNZ19'
    elif button_id == 'sl-nz-2019-button':
        collection_name = 'MSSLVSNZ19'
    elif button_id == 'eng-nz-2018-button':
        collection_name = 'MSENGVSNZ18'
    elif button_id == 'ind-nz-2019-button':
        collection_name = 'MSINDVSNZ19'
    elif button_id == 'ban-nz-2021-button':
        collection_name = 'MSBANVSNZ2021'
    elif button_id == 'ind-nz-2020-button':
        collection_name = 'MSINDVSNZ20'
    elif button_id == 'ned-nz-2022-button':
        collection_name = 'MSNEDVSNZ22'
    elif button_id == '2018-list-pak-button':
        collection_name = 'BL2018PAK'
    elif button_id == '2018-list-eng-button':
        collection_name = 'BL2018ENG'
    elif button_id == '2019-list-ban-button':
        collection_name = 'BL2019BAN'
    elif button_id == '2019-list-ind-button':
        collection_name = 'BL2019IND'
    elif button_id == '2021-list-ban-button':
        collection_name = 'BL2021BAN'
    elif button_id == '2020-list-ind-button':
        collection_name = 'BL2020IND'
    elif button_id == '2022-list-ned-button':
        collection_name = 'BL2022NED'
    elif button_id == '2019-list-sl-button':
        collection_name = 'BL2019SL'
    if collection_name:
        return display_data(collection_name)
    
    return ''

#Definig a function to query the database to connect the relevant collection to retrieve the ground state information and enabling 
#them depict through charts


def get_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['AnalyzingDataset']
    collection = db['GROUNDSTATS']
    data = collection.find({})
    return data
def create_bar_chart():
    data = get_data()
    runs_seamers = []
    runs_spinners = []
    wickets_seamers = []
    wickets_spinners = []
    seam_average = []
    spin_average = []
    grounds = []

    for d in data:
        #print(d.keys())
        #print(data[0]['Wickets'])


        runs_seamers.append(d['Runs Conceded (Seamers)'])
        runs_spinners.append(d['Runs Conceded (Spinners)'])
        wickets_seamers.append(d['Wickets (Seamers)'])  # corrected key
        wickets_spinners.append(d['Wickets (Spinners)'])
        seam_average.append(d['Seam Average'])
        spin_average.append(d['Spin Average'])
        grounds.append(d['Ground'])

    fig = go.Figure(data=[
    go.Bar(name='Runs Conceded (Seamers)', x=grounds, y=runs_seamers, marker=dict(color='#133E56')),
    go.Bar(name='Runs Conceded (Spinners)', x=grounds, y=runs_spinners, marker=dict(color='#3D6983')),
    go.Bar(name='Wickets (Seamers)', x=grounds, y=wickets_seamers, marker=dict(color='#2A353A')),
    go.Bar(name='Wickets (Spinners)', x=grounds, y=wickets_spinners, marker=dict(color='#0A2737')),
    go.Bar(name='Seam Average', x=grounds, y=seam_average, marker=dict(color='#1F1F76')),
    go.Bar(name='Spin Average', x=grounds, y=spin_average, marker=dict(color='#3E3E61'))
])

    fig.update_layout(
        title='Ground Statistics',
        xaxis_title='Grounds',
        yaxis_title='Value',
      plot_bgcolor='#CACACA',
        paper_bgcolor='#2E4C87',
        font_color='white'
    )

    return fig

@app.callback(
    Output('ground-statistics', 'children'),
    [Input('show-ground-statistics', 'n_clicks')]
)
def display_ground_statistics(n_clicks):
    if n_clicks > 0:
        fig = create_bar_chart()
        return dcc.Graph(figure=fig)
    else:
        return html.Div("Click the button to display the statistics",style={'text-align': 'center','color':'white'})
