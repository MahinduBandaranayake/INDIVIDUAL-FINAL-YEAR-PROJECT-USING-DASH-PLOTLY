import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pymongo
from dash.dependencies import Input, Output


# Connecting to the MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["AnalyzingDataset"]
players = db["Players"]
past_players = db["Past_players"]
scores=db["Scores"]
past_scores=db["Past_Scores"]
ratings=db["Rating"]
past_ratings=db["Past_Rating"]
predictions=db["Predictions"]
past_predictions=db["Past_Predictions"]
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_folder='/pages/assets')

# Defining callback function to display data
@app.callback(
    Output(component_id='data-display-1', component_property='children'),
    Input(component_id='data-button-1', component_property='n_clicks')
)
def display_data(n_clicks):
    if n_clicks:
        # Retrieving data from MongoDB
        record_data = list(players.find())
        past_record_data = list(past_players.find())

        # Formatting data as a string
        records_str = "\n".join([str(record) for record in record_data])
        past_records_str = "\n".join([str(record) for record in past_record_data])
        data_str = f"Records:\n{records_str}\n\nPast Records:\n{past_records_str}"

        # Returning the data string
        return data_str
    else:
        return ''
@app.callback(
    Output(component_id='data-display-2', component_property='children'),
    Input(component_id='data-button-2', component_property='n_clicks')
)
def display_data_2(n_clicks):
    if n_clicks:
        # Retrieving data from MongoDB
        score_data = list(scores.find())
        past_score_data = list(past_scores.find())

        # Formatting data as a string
        scores_str = "\n".join([str(score) for score in score_data])
        past_scores_str = "\n".join([str(score) for score in past_score_data])
        data_str = f"Scores:\n{scores_str}\n\nPast Scores:\n{past_scores_str}"

        # Return the data string
        return data_str
    else:
        return ''

@app.callback(
    Output(component_id='data-display-3', component_property='children'),
    Input(component_id='data-button-3', component_property='n_clicks')
)
def display_data_3(n_clicks):
    if n_clicks:
        # Retrieving data from MongoDB
        rating_data = list(ratings.find())
        past_rating_data = list(past_ratings.find())

        # Formatting data as a string
        ratings_str = "\n".join([str(rating) for rating in rating_data])
        past_ratings_str = "\n".join([str(rating) for rating in past_rating_data])
        data_str = f"Ratings:\n{ratings_str}\n\nPast Ratings:\n{past_ratings_str}"

        # Returning the data string
        return data_str
    else:
        return ''

@app.callback(
    Output(component_id='data-display-4', component_property='children'),
    Input(component_id='data-button-4', component_property='n_clicks')
)
def display_data_4(n_clicks):
    if n_clicks:
        # Retrieving data from MongoDB
        prediction_data = list(predictions.find())
        past_prediction_data = list(past_predictions.find())

        # Formatting data as a string
        predictions_str = "\n".join([str(prediction) for prediction in prediction_data])
        past_predictions_str = "\n".join([str(prediction) for prediction in past_prediction_data])
        data_str = f"Predictions:\n{predictions_str}\n\nPast Predictions:\n{past_predictions_str}"

        # Returning the data string
        return data_str
    else:
        return ''
    

    

# Modifying the layout to include a button and a container for the displayed data
layout = html.Div(
    [
        html.Div(
    [
         dbc.Button(
            'Players',
            id='data-button-1',
            n_clicks=0,
            style={
                'margin-top':'45px',
                'margin-left':'50px',
                'background-color': '#1E3D6C',
                'width':'100px'
            }
        ),
        dbc.Popover(
            [
                dbc.PopoverHeader("Players Names"),
                dbc.PopoverBody(id="data-display-1"),
            ],
            id="popover",
            is_open=False,
            target="data-button-1",
            trigger="hover"
        ),
        
       dbc.Button(
            'Scores',
            id='data-button-2',
            n_clicks=0,
            style={
                'margin-top':'45px',
                'margin-left':'30px',
                'background-color': '#1E3D6C',
                'width':'100px'
            }
        ),
        dbc.Popover(
            [
                dbc.PopoverHeader("Team Totals"),
                dbc.PopoverBody(id="data-display-2"),
            ],
            id="popover",
            is_open=False,
            target="data-button-2",
            trigger="hover"
        ),
        
      dbc.Button(
            'Ratings',
            id='data-button-3',
            n_clicks=0,
            style={
                'margin-top':'45px',
                'margin-left':'30px',
                'background-color': '#1E3D6C',
                'width':'100px'
            }
        ),
        dbc.Popover(
            [
                dbc.PopoverHeader("Player Ratings"),
                dbc.PopoverBody(id="data-display-3"),
            ],
            id="popover",
            is_open=False,
            target="data-button-3",
            trigger="hover"
        ),
        
        dbc.Button(
            'Predictions',
            id='data-button-4',
            n_clicks=0,
            style={
                'margin-top':'45px',
                'margin-right':'30px',
                'background-color': '#1E3D6C',
                'width':'100px'
            }
        ),
        dbc.Popover(
            [
                dbc.PopoverHeader("Predicting Player Performance"),
                dbc.PopoverBody(id="data-display-4"),
            ],
            id="popover",
            is_open=False,
            target="data-button-4",
            trigger="hover"
        ),
    ],
 
    style={
        'background-color': '#0C8AF0',
        'display': 'flex',
        'justify-content': 'space-between',
        'padding':'30px'
    }
)
,
        html.Div(
            [
                html.Img(src="https://th.bing.com/th/id/OIP.SgZZABddXYCD8f-ED3mF4wHaE7?w=264&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7", className="fern",style={'border-radius': '20px'}),
            ],
            style={'background-color': '#0C8AF0','text-align':'center','margin-top':'45px','border-radius': '30px'},
        ),
        html.Div(
            [
                html.H1("Vision", style={"color": "white",'font-weight':'bold','font-size':'25px','margin-left':'20px','margin-top':'45px'}),
                html.H3(
                    "Enhance the productivity in Game Plan",
                    style={"color": "white",'font-size':'25px','margin-left':'20px'},
                ),
            ],
            className="header",style={'margin-top':'30px','font-size':'25px','margin-left':'20px'}
        ),
        html.Div(
            [
                html.H1("Mission", style={"color": "white",'font-weight':'bold','font-size':'25px','margin-left':'20px'}),
                html.H3(
                    "Descriptive Analysis and Statistical Measurements",
                    style={"color": "white",'font-size':'25px','margin-left':'20px'},
                ),
            ],
            className="header",style={'margin-left':'20px','font-size':'25px','margin-top':'30px'}
        ),
        html.Div(
            [
                dbc.Navbar(
                    [
                        dbc.NavItem(dbc.NavLink("Team : New Zealand ", href="https://www.nzc.nz/cricketnation"),style={"color":"white","margin-left":"40px","font-weight": "bold"}),
                        dbc.NavItem(dbc.NavLink("cricdev@gmail.com", href="https://www.google.com/search?client=firefox-b-d&q=gmail+login"),style={"color":"white","margin-left":"40px"}),
                        dbc.NavItem(dbc.NavLink("Espncricinfo", href="https://www.google.com/search?client=firefox-b-d&q=espncricinfo"),style={"color":"white","margin-left":"40px"}),
                        
                        dbc.NavItem(
                            html.A("+94 771654140", href="#", style={"color": "white", "text-decoration": "none", "font-weight": "bold"}),
                            style={"color":"white",'background-color':'#000000',"margin-left":"40px"},
                        ),
                    ],
                    className="navbar",
                    color="#000000",
                    dark=True,
                    fixed="bottom",
                   
                )
            ],
            className="footer"
        ),





        
    ],
    style={'background-color': '#0C8AF0','margin-top':'auto','height':'800px',}
)