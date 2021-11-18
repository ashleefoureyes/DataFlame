import dash_core_components as dcc
import dash_html_components as html
import dash_table

# Import Bootstrap components
import dash_bootstrap_components as dbc

# Import custom data.py
import data.data_load as dta
from assets.styles import (DROPDOWN_STYLE)

# Import data from data.py file
teams_df = dta.teams



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
    className="team-menu",
)

