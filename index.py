# import dash and bootstrap components
import dash
import dash_bootstrap_components as dbc

import os
import data.data_load as dta
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import callbacks

from components.figures.arena_plot import *

from layouts import (
    team_menu,
    player_menu,
    shot_stats_collapse,
    arena_layout,
    player_page_header,
    player_page
)

from components.navigation_bar import nav_bar
from app import app

# Import server for deployment
from app import svr as server


app_name = os.getenv("DASH_APP_PATH", "/dataFlame")

# Set layout variables
nav = nav_bar()

header = dbc.Row(
    dbc.Col(
        html.Div(
            [
                html.H2(children="Hockey Data"),
                html.H3(children="A Visualization of Women's Hockey Data"),
            ]
        )
    ),
    className="banner",
)

content = html.Div([dcc.Location(id="url"), html.Div(id="page-content")])
container = dbc.Container([content], className="dataflame-content")

# Home callback, set and return
# Connect pages to container
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname in [app_name, app_name + "/"]:
        return html.Div(
            [
                dcc.Markdown(
                    """
                        ### Home Page, todo
                    """
                )
            ],
            className="home",
        )
    elif pathname.endswith("/game"):
        return team_menu
    elif pathname.endswith("/player"):
        return player_page_header, player_page
    elif pathname.endswith("/predictive"):
        return app_menu, predictive_menu
    else:
        return "ERROR 404: Page not found!"


# Main index function to call all layout variables
def index():
    layout = html.Div([nav, container])
    return layout


# Set layout to index function
app.layout = index()

# Call app server
if __name__ == "__main__":
    # set to false when deploying app
    app.run_server(debug=True)