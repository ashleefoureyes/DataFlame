from dash.dependencies import Input, Output

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_table
from app import app
import data.data_load as dta
import logging
from dash import Input, Output, State, html

from components.figures.arena_plot import *

players_df = dta.players
total_df = dta.df


# Callback to player dropdown menu
@app.callback(
    Output("player-dropdown", "options"),
    [Input("team-dropdown", "value")],
)
def update_player_dropdown(team):
    players_team_df = dta.dynamic_players(team)
    players_df = players_team_df["Player"]
    names = [{'label': i, 'value': i} for i in players_df]

    # Return names of players belonging to selected team
    return names


# Load Player Profile
# Callback to Player profile datatable
@app.callback(
    [Output("player_profile", "data"), Output("player_profile", "columns"),
     Output("player-shooting-figure", "figure")],
    [Input("player-dropdown", "value")],
)
def update_player_page(player):
    player_dets = dta.shot_details(player)
    shooting_df = dta.shot_details_for_plot(player)
    shots_df = dta.load_shooting_df(shooting_df)
    figure = plot_shooting_graph(shots_df)

    # Return player profile to datatable
    return player_dets.to_dict("records"), [{"name": x, "id": x} for x in player_dets], figure


# Show player page when player is selected
@app.callback(
    Output("player-page", "style"),
    [Input("player-dropdown", "value")]
)
def update_player_visibility(player):
    if (player):
        return {"display": "block"}
    return {"display": "none"}


# Toggle visibilty of data table
@app.callback(
    Output("collapse-shots-card", "is_open"),
    [Input("collapse-shots-btn", "n_clicks")],
    [State("collapse-shots-card", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
