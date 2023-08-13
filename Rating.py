import dash
from dash import dcc
from dash import html
import pandas as pd
from pymongo import MongoClient
import pymongo
from sklearn.linear_model import LinearRegression
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import mean_squared_error, r2_score
import plotly.graph_objs as go
import dash_bootstrap_components as dbc





def generate_prediction_chart(predicted_average, player_name):  #Defining the callback function to generate the chart relating to visualize the predicted average in a guage chart
    chart = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=predicted_average,
            title={'text': f"Predicted Average for {player_name}"},
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [0, 10], 'tickmode': 'array', 'tickvals': [0, 2, 4, 6, 8, 10]},
                'steps': [
                    {'range': [0, 4], 'color': "red"},
                    {'range': [4, 8], 'color': "orange"},
                    {'range': [8, 10], 'color': "green"}
                ],
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                    'value': predicted_average
                }
            },
        )
    )


    if player_name == 'Player 1':       # Setting the chart colors based on the selected player
        chart.update_traces(marker=dict(colors=['red', 'gray']))
    elif player_name == 'Player 2':
        chart.update_traces(marker=dict(colors=['blue', 'gray']))
    elif player_name == 'Player 3':
        chart.update_traces(marker=dict(colors=['orange', 'green']))


  
    return dbc.Container(     # Returning the chart wrapped in a Bootstrap container
        dbc.Row(
            dbc.Col(
                dcc.Graph(id='prediction-chart', figure=chart),
                width=12
            )
        ),
        fluid=True,
        className='my-4'
    )


client = pymongo.MongoClient('mongodb://localhost:27017/')# Connection string to the MongoDB database which draws the data from the relevant collection


db = client['AnalyzingDataset']
collection = db['Player_Average_Prediction']# Selecting the database and collection
latest_document = collection.find_one(sort=[("timestamp_field", pymongo.DESCENDING)]) #Enabling the timestamp to retrieve the latest details from the collection 

data = pd.DataFrame(list(collection.find()))# Fetching the data in to pandas dataframe 


seam_data = data[data['Bowling Type'] == 'Seam'] # Preparing the data for regression analysis
spin_data = data[data['Bowling Type'] == 'Spin']
seam_X = seam_data[['Matches', 'Wickets', 'Runs Given']]
spin_X = spin_data[['Matches', 'Wickets', 'Runs Given']]
seam_y = seam_data['Average']
spin_y = spin_data['Average']


seam_model = LinearRegression()# Train the linear regression models
seam_model.fit(seam_X, seam_y)
spin_model = LinearRegression()
spin_model.fit(spin_X, spin_y)



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,
                                      'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'])# Defining the Dash app layout


options = [{'label': player, 'value': player} for player in data['Player'].dropna()]



layout = html.Div([             #Defining the UI layout to make user interactions
   html.Div([
    html.H1('PREDICTIONS', style={'text-align': 'center', 'font-weight': 'bold','color': 'white'}),
   ], style={'padding-top': '50px'}),
   
    html.Div([
    html.Div([
        html.H3('SELECT A PARTICULAR PLAYER FROM BELOW', style={'font-size': '20px', 'font-weight': 'bold', 'margin-top': '20px','color': 'white'}),
        dcc.Dropdown(
            id='player-dropdown',
            options=options,
            value=data['Player'].iloc[0]
        ),
    ], style={'padding': '20px'}),
    html.Div([
    html.H3('SELECT A DEFAULT VALUE FOR NUMBER OF MATCHES',style={'font-size': '20px', 'font-weight': 'bold', 'margin-top': '20px','color': 'white'}),
        dcc.Dropdown(
            id='match-dropdown',
            options=[
                {'label': 'Increase matches by 3', 'value': 3},
                {'label': 'Increase matches by 5', 'value': 5}
            ],
            value=3,
            style={'margin-right': '10px'}
        ),
    ], style={'padding': '20px'}),
    html.Div([
        html.H3('DEFINE CUSTOM VALUES FOR NUMBER OF MATCHES',style={'font-size': '20px', 'font-weight': 'bold', 'margin-top': '20px','color': 'white'}),
        dcc.Input(
            id='custom-match-input',
            type='number',
            min=1,
            max=1000,
            step=1,
            placeholder='Enter number of matches...',
            style={'margin-bottom': '70px'}
            
        ),
        html.Div(id='prediction-output')
    ], style={'padding': '20px'}),
    
    html.Div([
        html.Div([
            html.H3(f"Seam Model R-squared (Accuracy of the Output)-Verification Purpose : {seam_model.score(seam_X, seam_y):.2f}",style={'font-size': '20px', 'margin-top': '20px','color': 'white'}) #Depicting the correlation R squared value just to make sure the validity of the prediction
        ], className="four columns"),
        html.Div([
            html.H3(f"Spin Model R-squared (Accuracy of the Output)-Verification Purpose : {spin_model.score(spin_X, spin_y):.2f}",style={'font-size': '20px', 'margin-top': '20px','color': 'white'})
        ], className="four columns")
    ], style={'padding': '20px'},className="row"),
    dcc.Graph(id='correlation-matrix',style={
        'padding-left': '22px',
        'padding-right': '22px',
        'marginBottom': 50, 'marginTop': 25
    }),
    dcc.Graph(id='scatter-plot',style={
        'padding-left': '22px',
        'padding-right': '22px'
    })

    ], style={'padding': '65px'}),
],style={ 'background-color': '#2E4C87'})




@app.callback(                      # Defining the callback function for the predicted average with increased number of matches (when the value in matches increases, it should deviate the average value)
    dash.dependencies.Output('prediction-output', 'children'),
    [dash.dependencies.Input('player-dropdown', 'value'),
     dash.dependencies.Input('match-dropdown', 'value'),
     dash.dependencies.Input('custom-match-input', 'value')]
)
def update_prediction_output(player_name, match_increase, custom_match_input):
    if custom_match_input is None:
        num_matches = float(data[data['Player'] == player_name]['Matches'])
        num_matches += match_increase
    else:
        num_matches = custom_match_input
  
    player_data = data[(data['Player'] == player_name) & (data['Bowling Type'] == 'Seam')]  # Getting the data for the selected player
    if len(player_data) > 0:
        wickets = float(player_data.iloc[0]['Wickets'])
        runs_given = float(player_data.iloc[0]['Runs Given'])
    else:
        wickets = 0.0
        runs_given = 0.0


    predicted_average = seam_model.predict([[num_matches, wickets, runs_given]])[0]    # Predicting the average for the increased number of matches

   
  # Creating a speedometer chart
    chart = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=predicted_average,
        title={'text': f"Predicted Average for {player_name}", 'font': {'color': 'white'}},
        number={'font': {'color': 'white'}},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'visible': False},
            'steps': [
                {'range': [0, 4], 'color': "red"},
                {'range': [4, 8], 'color': "orange"},
                {'range': [8, 10], 'color': "green"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': predicted_average
            }
        }
      
    )
    
)
    chart.update_layout(
    plot_bgcolor='black',  # setting the background color of the plot
    paper_bgcolor='#2E4C87',  # setting the background color of the paper

)

    # Setting the chart colors based on the selected player
    if player_name == 'Player 1':
        chart.update_traces(marker=dict(colors=['red', 'gray']))
    elif player_name == 'Player 2':
        chart.update_traces(marker=dict(colors=['blue', 'gray']))
    elif player_name == 'Player 3':
        chart.update_traces(marker=dict(colors=['orange', 'green']))


    # Returning the chart wrapped in a Bootstrap container
    return dbc.Container(
        dbc.Row(
            dbc.Col(
                dcc.Graph(id='prediction-chart', figure=chart),
                width=12
            )
        ),
        fluid=True,
        className='my-4'
    )

#Defining the callback function for the correlation matrix graph
@app.callback(
dash.dependencies.Output('correlation-matrix', 'figure'),
[dash.dependencies.Input('player-dropdown', 'value')]
)
def update_correlation_matrix(player):
  
    player_data = data[['Player', 'Wickets', 'Runs Given', 'Average']]  # Getting the data for all players
    player_data['Average'] = pd.to_numeric(player_data['Average'])

   
    corr_matrix = player_data[['Average', 'Wickets']].corr() # Calculating the correlation matrix using the corr's keyword
    
    if corr_matrix.isna().sum().sum() > 0:
       
        fig = go.Figure() # Handling the case where correlation matrix is empty
        fig.update_layout(title=f'Correlation Matrix for all the players')
        return fig
    
    # Creating the heatmap
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=['Wickets Taken'],
        y=['Average'],
        colorscale='RdBu',
        zmin=-1,
        zmax=1,
        colorbar=dict(title='Correlation')
    ))
    
    # Setting the layout
    fig.update_layout(
        title=f'Correlation Matrix Heat Map for Average and Wickets',
        xaxis=dict(title='Players'),
        yaxis=dict(title='Players'),
        plot_bgcolor='#CACACA',
        paper_bgcolor='#2E4C87',
        font_color='white'
    )
    
    return fig






@app.callback(              # Defining the callback function for the scatter plot graph
    dash.dependencies.Output('scatter-plot', 'figure'),
    [dash.dependencies.Input('player-dropdown', 'value')]
)

def update_player_performance(player):     # Getting the data for the selected player and all other players

    player_data = data[data['Player'] == player][['Matches', 'Wickets', 'Runs Given', 'Average']]
    other_data = data[data['Player'] != player][['Matches', 'Wickets', 'Runs Given', 'Average']]
    player_data['Average'] = pd.to_numeric(player_data['Average'])
    other_data['Average'] = pd.to_numeric(other_data['Average'])
    
    # Creating the scatter plot for the selected player depiction and the other players
    fig = px.scatter_3d(
        other_data,
        x='Matches',
        y='Wickets',
        z='Runs Given',
        color='Average',
        size='Average',
        hover_data=['Average'],
       
    )
    
    fig.add_trace(
        go.Scatter3d(
            x=player_data['Matches'],
            y=player_data['Wickets'],
            z=player_data['Runs Given'],
            
            mode='markers',
            marker=dict(
                color='blue',
                size=10
            ),
            name='Selected Player',
            text=player_data['Average'],
            hovertemplate='Matches: %{x}<br>Wickets Taken: %{y}<br>Runs Given: %{z}<br>Average: %{text}<br><b>Selected Player</b>',
        )
    )
    
    # Setting the layout
    fig.update_layout(
        title=f'Performance of {player} among Other Players',
        scene=dict(
            xaxis=dict(title='Matches'),
            yaxis=dict(title='Wickets Taken'),
            zaxis=dict(title='Runs Given')
        ),
        plot_bgcolor='#CACACA',
        paper_bgcolor='#2E4C87',
        font_color='white'
    )
    
    return fig
