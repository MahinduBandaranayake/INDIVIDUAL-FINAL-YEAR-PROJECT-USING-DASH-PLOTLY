import dash
from dash import dcc
from dash import html
import pymongo
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import seaborn as sns
from plotly.subplots import make_subplots
import numpy as np


# Connect to MongoDB and get data
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["AnalyzingDataset"]

overs_collection_pak = db["OVERSPAK18"]
wickets_collection_pak = db["WICKETSPAK18"]
average_collection_pak = db["AVERAGEPAK18"]
economy_collection_pak = db["ECONOMYPAK18"]
strike_rate_collection_pak = db["STRIKERATEPAK18"]
dot_balls_collection_pak = db["DOTBALLSPAK18"]
runs_given_collection_pak = db["RUNSGIVENPAK18"]




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
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP,'https://use.fontawesome.com/releases/v5.7.2/css/all.css'])
app.layout = html.Div([
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
],style={'text-align':'center','background-color':'#2E4C87'})


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
