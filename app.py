# import dash and bootstrap components
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SANDSTONE],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)


app.title = "dataflame - Hockey Data Tool"
# set app server
svr = app.server
app.config.suppress_callback_exceptions = True

