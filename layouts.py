import dash_core_components as dcc
import dash_html_components as html
import dash_table

import plotly.graph_objs as go

# Import Bootstrap components
import dash_bootstrap_components as dbc

# Import custom data.py
import data.data_load as dta
from assets.styles import (DROPDOWN_STYLE)

# Import data from data.py file
teams_df = dta.teams

from components.figures.arena_plot import *

# Team menu dropdown to be used on team analysis and player analysis pages
team_menu = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H6(
                        children="Select Team:",
                    ),
                    width="2",
                    className="centered-col"
                ),
                dbc.Col(
                    dcc.Dropdown(
                        style=DROPDOWN_STYLE,
                        id="team-dropdown",
                        options=[{'label': i, 'value': i} for i in teams_df],
                        clearable=False,
                    ),
                    className="centered-col"
                ),
            ],
            className="dropdown-row"
        ),
    ],
    className="menu",
)

'''
PLAYER PAGE LAYOUT AND COMPONENTS
'''
player_header = dbc.Row(
    dbc.Col(
        html.Div(
            [
                html.Div(children="Player Insight", className="player-page-header"),
            ],
        ),
        width="3",
    ),
)

# Player menu dropdown
player_menu = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H6(
                        children="Select Player:",
                    ),
                    width="2",
                    className="centered-col"
                ),
                dbc.Col(
                    dcc.Dropdown(
                        style=DROPDOWN_STYLE,
                        id="player-dropdown",
                        clearable=False,
                    ),
                    className="centered-col"
                ),
            ],
            className="dropdown-row"
        ),
        html.Br(),
    ],
    className="menu",
)

# Player Summary Card
player_card = [
    dbc.Row(
        [
            dbc.Col(
                dbc.CardImg(
                    src="/assets/player_placeholder.jpeg",
                    className="img-fluid rounded-start",

                ),
                className="col-md-4",
            ),
            dbc.Col(
                dbc.CardBody(
                    [
                        html.H4(id="player-title", className="card-title"),
                        html.A(
                            "GENERAL PLAYER INFO PLACEHOLDER",
                            className="card-text",
                        ),
                    ]
                ),
            ),
        ],
        className="g-0 d-flex align-items-center card-styled",

    )]

# ARENA LAYOUT
arena_layout = html.Div([
    html.Div(
        [
            html.Div(
                [
                    dcc.Graph(
                        id="player-shooting-figure",
                        config={"displaylogo": False})
                ],
            ),
        ],
        className="row"),
])

# Outline for graph card body
graph_card = dbc.CardBody(
    [
        html.A(
            "PLACEHOLDER RIGHT NOW",
            className="card-text",
        ),
    ],
    className="g-0 d-flex align-items-center card-styled"
)

# STATS COLLAPSE
# loading shot data for visual, change this to relevant data when complete
shot_stats_collapse = dbc.CardBody(
    [
        dbc.Button(
            "Show shot details",
            id="collapse-shots-btn",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                    [
                        dash_table.DataTable(
                            id="player_profile",
                            style_as_list_view=True,
                            editable=False,
                            style_table={
                                "overflowY": "scroll",
                                "width": "100%",
                                "minWidth": "100%",
                            },
                            style_header={"backgroundColor": "#f8f5f0", "fontWeight": "bold"},
                            style_cell={"textAlign": "center", "padding": "8px"},
                        ),
                    ]
                )
            ),
            id="collapse-shots-card",
            is_open=False,
        ),
    ],
    className="card-styled",
)

# Player menu content

player_page_header = html.Div(
    children=[
        player_header,
        team_menu,
        player_menu
    ],
    className="player-page-menu"
)

# Player page content layout
player_page = html.Div(
    id="player-page",
    style={"display":"none"},
    children=[
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                    [
                        html.Div(children="PLAYER OVERVIEW", className="section-header"),
                    ],
                    )
                )
            ]

        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(player_card),
                    width=6,
                ),
                dbc.Col(
                    dbc.Card(graph_card),
                    width=6,
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                    [
                        html.Div(children="SHOT OVERVIEW", className="section-header"),
                    ],
                    )
                )
            ]

        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(arena_layout),
                        className="g-0 d-flex align-items-left card-styled"
                    ),
                ),
                dbc.Col(
                    dbc.Card(shot_stats_collapse),
                )
            ],
        ),
    ],
)
