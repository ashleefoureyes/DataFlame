from dash.dependencies import Input, Output

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_table
from app import app
import data.data_load as dta


# Import dataframes
teams_df = dta.teams
players_df = dta.players


# @app.callback(
#     [
#         Output("team-dropdown", "options"),
#
#     ]
# )