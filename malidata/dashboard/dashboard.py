import dash
from dash import dcc, html
from .dash_layout import html_layout

def init_dashboard(server):
    dash_app = dash.Dash(
        server = server,
        routes_pathname_prefix = "/dashboard/",
    )
    dash_app.index_string = html_layout

    dash_app.layout = html.Div([

    ])
    return dash_app.server
