import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State
from pages.AdminPage import layout as admin_layout,delete_record_callback,delete_record_callback2
from pages.StartingPage import layout as starting_page_layout,display_data
from pages.Rating import layout as rating_layout, update_prediction_output,update_correlation_matrix,update_player_performance
from pages.SectionOne import layout as section_one_layout,update_table,display_ground_statistics
from pages.Selection import layout as selection_layout,update_graph,search_player
from pages.Insertion import layout as insertion_layout,update_data,clear_inputs,update_submit2_button2
from pages.Series import layout as series_layout,update_chart_8,update_chart_7,update_chart_6,update_chart_5,update_chart_4,update_chart_3,update_chart_2,update_chart_1
from pages.SectionThree import layout as section_three_layout,insert_data,display_current_data,update_submit_button


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP,'https://use.fontawesome.com/releases/v5.7.2/css/all.css'], suppress_callback_exceptions=True)

navbar = dbc.Navbar(
    [
        dbc.NavItem(dbc.NavLink("E-ANALYTICA", href="#"), style={"margin-left": "10px"}),
       dbc.NavItem(dbc.NavLink("Overview", href="/pages/StartingPage"),style={'font-size':'12px',"margin-left": "110px"}),
        dbc.NavItem(dbc.NavLink("History", href="/pages/SectionOne"),style={'font-size':'12px',"margin-left": "110px"}),
        dbc.NavItem(dbc.NavLink("Entries", href="/pages/SectionThree"),style={'font-size':'12px',"margin-left": "110px"}),
        dbc.NavItem(dbc.NavLink("Records", href="/pages/Series"),style={'font-size':'12px',"margin-left": "110px"}),
        dbc.NavItem(dbc.NavLink("Preference", href="/pages/Selection"), style={'font-size':'12px',"margin-left": "110px"}),
        dbc.NavItem(dbc.NavLink("Predictions", href="/pages/Rating"), style={'font-size':'12px',"margin-left": "110px"}),
        dbc.NavItem(dbc.NavLink("Modernize", href="/pages/Insertion"), style={'font-size':'12px',"margin-left": "110px"}),
         dbc.NavItem(dbc.NavLink("Administration", href="/pages/AdminPage"), style={'font-size':'12px',"margin-left": "110px",'hover':'white'}),
  
      
    ],
    color="#0C8AF0",
  
    sticky="top",
    style={"font-size": "18px", "background-color": "#013470"}
)

navbar_link_style = {
    "color": "white",
    "font-weight": "bold"
}

navbar_active_style = {
    "color": "black",
    "font-weight": "bold",
    "background-color": "#0C8AF0",
    "border-radius": "4px"
}

navbar_hover_style = {
    "color": "black",
    "font-weight": "bold",
    "background-color": "#0C8AF0",
    "border-radius": "4px"
}

for nav_item in navbar.children:
    if isinstance(nav_item, dbc.NavItem):
        nav_item.children.style = navbar_link_style
        nav_item.active_style = navbar_active_style
        nav_item.children.hover_style = navbar_hover_style



# Defining the layout of the app
app.layout = html.Div([

   dcc.Location(id='url', refresh=False, pathname='/pages/StartingPage'),
    navbar,
    html.Div(id='page-content',style={'margin-top': '0px'})
    
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/pages/AdminPage':
        return admin_layout
    
    elif pathname == '/pages/SectionOne':
        return section_one_layout
    elif pathname == '/pages/Selection':
        return selection_layout
    elif pathname == '/pages/Rating':
        return rating_layout
    elif pathname == '/pages/Insertion':
        return insertion_layout
    elif pathname == '/pages/StartingPage':
        return starting_page_layout
    elif pathname == '/pages/Series':
        return series_layout
    elif pathname == '/pages/SectionThree':
        return section_three_layout

app.callback(
    dash.dependencies.Output('output-container2', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])(search_player)


app.callback(
    Output('submit', 'disabled'),
    Input('player_input', 'value'),
    Input('matches_input', 'value'),
    Input('wickets_input', 'value'),
    Input('runs_given_input', 'value'),
    Input('bowling_type_input', 'value'),
    Input('role_input', 'value'))(update_submit2_button2)



app.callback(
    Output('submit-button', 'disabled'),
    Input('year-input', 'value'),
    Input('matches-input', 'value'),
    Input('opponent-input', 'value'),
    Input('player-input', 'value'),
    Input('bowling_style-input', 'value'),
    Input('runs-input', 'value'),
    Input('overs-input', 'value'),
    Input('wickets-input', 'value'))(update_submit_button)



app.callback(
    Output('output-messageDATA', 'children'),
    Input('delete-button2', 'n_clicks'),
    State('player-dropdown', 'value'),
    State('year-dropdown', 'value'))(delete_record_callback2)

app.callback(
    Output('output-message-2', 'children'),
    Input('delete-button', 'n_clicks'),
    State('input-player-name', 'value'))(delete_record_callback)




app.callback(Output('current-data', 'children'),
              [Input('refresh-button', 'n_clicks'),
               ])(display_current_data)


app.callback(Output('output', 'children'),
              Output('player-stats', 'children'),
              Input('submit-button', 'n_clicks'),
              State('year-input', 'value'),
               State('matches-input', 'value'),
              State('opponent-input', 'value'),
              State('player-input', 'value'),
              State('bowling_style-input', 'value'),
              State('runs-input', 'value'),
              State('overs-input', 'value'),
              State('wickets-input', 'value'))(insert_data)

app.callback(
    Output("graph-container-1", "children"),
    [Input("show-overs-graph-btn-1", "n_clicks"),
     Input("show-wickets-graph-btn-1", "n_clicks"),
     Input("show-average-graph-btn-1", "n_clicks"),
     Input("show-economy-graph-btn-1", "n_clicks"),
     Input("show-strikerate-graph-btn-1", "n_clicks"),
     Input("show-dotballs-graph-btn-1", "n_clicks"),
     Input("show-runsgiven-graph-btn-1", "n_clicks")],
    State("graph-container-1", "children"))(update_chart_1)

app.callback(
    Output("graph-container-2", "children"),
    [Input("show-overs-graph-btn-2", "n_clicks"),
     Input("show-wickets-graph-btn-2", "n_clicks"),
     Input("show-average-graph-btn-2", "n_clicks"),
     Input("show-economy-graph-btn-2", "n_clicks"),
     Input("show-strikerate-graph-btn-2", "n_clicks"),
     Input("show-dotballs-graph-btn-2", "n_clicks"),
     Input("show-runsgiven-graph-btn-2", "n_clicks")],
    State("graph-container-2", "children"))(update_chart_2)


app.callback(
    Output("graph-container-3", "children"),
    [Input("show-overs-graph-btn-3", "n_clicks"),
     Input("show-wickets-graph-btn-3", "n_clicks"),
     Input("show-average-graph-btn-3", "n_clicks"),
     Input("show-economy-graph-btn-3", "n_clicks"),
     Input("show-strikerate-graph-btn-3", "n_clicks"),
     Input("show-dotballs-graph-btn-3", "n_clicks"),
     Input("show-runsgiven-graph-btn-3", "n_clicks")],
    State("graph-container-3", "children"))(update_chart_3)


app.callback(
    Output("graph-container-4", "children"),
    [Input("show-overs-graph-btn-4", "n_clicks"),
     Input("show-wickets-graph-btn-4", "n_clicks"),
     Input("show-average-graph-btn-4", "n_clicks"),
     Input("show-economy-graph-btn-4", "n_clicks"),
     Input("show-strikerate-graph-btn-4", "n_clicks"),
     Input("show-dotballs-graph-btn-4", "n_clicks"),
     Input("show-runsgiven-graph-btn-4", "n_clicks")],
    State("graph-container-4", "children"))(update_chart_4)


app.callback(
    Output("graph-container-5", "children"),
    [Input("show-overs-graph-btn-5", "n_clicks"),
     Input("show-wickets-graph-btn-5", "n_clicks"),
     Input("show-average-graph-btn-5", "n_clicks"),
     Input("show-economy-graph-btn-5", "n_clicks"),
     Input("show-strikerate-graph-btn-5", "n_clicks"),
     Input("show-dotballs-graph-btn-5", "n_clicks"),
     Input("show-runsgiven-graph-btn-5", "n_clicks")],
    State("graph-container-5", "children"))(update_chart_5)


app.callback(
    Output("graph-container-6", "children"),
    [Input("show-overs-graph-btn-6", "n_clicks"),
     Input("show-wickets-graph-btn-6", "n_clicks"),
     Input("show-average-graph-btn-6", "n_clicks"),
     Input("show-economy-graph-btn-6", "n_clicks"),
     Input("show-strikerate-graph-btn-6", "n_clicks"),
     Input("show-dotballs-graph-btn-6", "n_clicks"),
     Input("show-runsgiven-graph-btn-6", "n_clicks")],
    State("graph-container-6", "children"))(update_chart_6)


app.callback(
    Output("graph-container-7", "children"),
    [Input("show-overs-graph-btn-7", "n_clicks"),
     Input("show-wickets-graph-btn-7", "n_clicks"),
     Input("show-average-graph-btn-7", "n_clicks"),
     Input("show-economy-graph-btn-7", "n_clicks"),
     Input("show-strikerate-graph-btn-7", "n_clicks"),
     Input("show-dotballs-graph-btn-7", "n_clicks"),
     Input("show-runsgiven-graph-btn-7", "n_clicks")],
    State("graph-container-7", "children"))(update_chart_7)





app.callback(
    Output("graph-container-8", "children"),
    [Input("show-overs-graph-btn-8", "n_clicks"),
     Input("show-wickets-graph-btn-8", "n_clicks"),
     Input("show-average-graph-btn-8", "n_clicks"),
     Input("show-economy-graph-btn-8", "n_clicks"),
     Input("show-strikerate-graph-btn-8", "n_clicks"),
     Input("show-dotballs-graph-btn-8", "n_clicks"),
     Input("show-runsgiven-graph-btn-8", "n_clicks")],
    State("graph-container-8", "children"))(update_chart_8)





app.callback(
    Output('ground-statistics', 'children'),
    [Input('show-ground-statistics', 'n_clicks')])(display_ground_statistics)




app.callback(Output('prediction-output','children'),
              [Input('player-dropdown','value'),
               Input('match-dropdown','value'),
               Input('custom-match-input','value')])(update_prediction_output)

app.callback(Output('correlation-matrix','figure'),
              [Input('player-dropdown','value')])(update_correlation_matrix)

app.callback(Output('scatter-plot','figure'),
              [Input('player-dropdown','value')])(update_player_performance)



app.callback(
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
     Input('2019-list-sl-button', 'n_clicks')])(update_table)

app.callback(
    Output('output-containerP', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('avg-input', 'value'),
     State('matches-input', 'value')])(update_graph)



app.callback(
    Output(component_id='data-display', component_property='children'),
    Input(component_id='data-button', component_property='n_clicks'))(display_data)













app.callback(
    [Output('output-message', 'children'),
     Output('table', 'data')],
    [Input('submit', 'n_clicks')],
    [State('player_input', 'value'),
     State('matches_input', 'value'),
     State('wickets_input', 'value'),
     State('runs_given_input', 'value'),
     State('bowling_type_input', 'value'),
     State('role_input', 'value')],
    [State('table', 'data')])(update_data)

app.callback(
    [Output('player_input', 'value'),
     Output('matches_input', 'value'),
     Output('wickets_input', 'value'),
     Output('runs_given_input', 'value'),
     Output('bowling_type_input', 'value'),
     Output('role_input', 'value')],
    [Input('clear-button', 'n_clicks')])(clear_inputs)

if __name__ == '__main__':
    app.run_server(debug=True)
