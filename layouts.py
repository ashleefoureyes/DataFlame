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

# # Main application menu
# app_menu = html.Div(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(
#                     html.H6(
#                         style={"text-align": "center"},
#                         children="Select Team:",
#                     ),
#                 ),
#                 dbc.Col(
#                     dcc.Dropdown(
#                         style={
#                             "text-align": "center",
#                         },
#                         id="team-dropdown",
#                         clearable=False,
#                     ),
#                 ),
#             ],
#         ),
#     ],
#     className="menu",
# )

# Team menu dropdown to be used on team analysis and player analysis pages
team_menu = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H6(
                        children="Select Team:",
                    ),
                    width="2"
                ),
                dbc.Col(
                    dcc.Dropdown(
                        style=DROPDOWN_STYLE,
                        id="team-dropdown",
                        options=[{'label': i, 'value': i} for i in teams_df],
                        clearable=False,
                    ),

                ),
            ],
        ),
    ],
    className="menu",
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
                    width="2"
                ),
                dbc.Col(
                    dcc.Dropdown(
                        style=DROPDOWN_STYLE,
                        id="player-dropdown",
                        clearable=False,
                    ),

                ),
            ],
        ),
        # dbc.Row(
        #     dbc.Col(
        #         dash_table.DataTable(
        #             id="player_profile",
        #             style_as_list_view=True,
        #             editable=False,
        #             style_table={
        #                 "overflowY": "scroll",
        #                 "width": "100%",
        #                 "minWidth": "100%",
        #             },
        #             style_header={"backgroundColor": "#f8f5f0", "fontWeight": "bold"},
        #             style_cell={"textAlign": "center", "padding": "8px"},
        #         ),
        #     ),
        #     justify="center",
        # ),
        html.Br(),
    ],
    className="menu",
)

'''
PLAYER LAYOUT
'''
shot_stats_collapse = html.Div(
    [
        dbc.Button(
            "Open collapse",
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
    ]
)

'''
PLAYER PAGE LAYOUT AND COMPONENTS
'''
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
                        html.H4("Sarah Nurse", className="card-title"),
                        html.A(
                            "Put some player info here",
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
    html.Div(id='container')
])

# STATS COLLAPSE
shot_stats_collapse = html.Div(
    [
        dbc.Button(
            "Open collapse",
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
    ]
)

# Player Page Layout
player_page = html.Div([
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(player_card),
                width=6,
            ),
            dbc.Col(
                dbc.Card(player_card),
                width=6,
            ),
        ]
    ),
    html.Br(),
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(arena_layout),
                    className="g-0 d-flex align-items-left card-styled"
                ),
            )
        ]
    )
])
