# Import Bootstrap from Dash
import os

import dash_bootstrap_components as dbc
import dash_html_components as html

# TODO double check this configuration
app_name = os.getenv("DASH_APP_PATH", "/dataFlame")
DATAFLAME_LOGO = "/assets/dataFlameLogo3.png"

def nav_bar():
    nav = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=DATAFLAME_LOGO, height="50px")),
                            dbc.Col(dbc.NavbarBrand("dataFlame", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href=f"{app_name}",
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(
                        [dbc.NavItem(dbc.NavLink("Game Analysis", href=f"{app_name}/game")),
                         dbc.NavItem(dbc.NavLink("Player Analysis", href=f"{app_name}/player")),
                         dbc.NavItem(dbc.NavLink("Predictive", href=f"{app_name}/predictive"))],
                        className="ms-auto",
                        navbar=True,
                    ),
                    id="navbar-collapse2",
                    navbar=True,
                ),
            ],

        ),
        class_name="mb-5",
        color="#C8102E",

    )

    return nav

