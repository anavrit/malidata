import dash
from dash import dcc, html
from .dash_layout import html_layout
import dash_bootstrap_components as dbc

def init_dashboard(server):
    dash_app = dash.Dash(
        server = server,
        routes_pathname_prefix = "/dashboard/",
        external_stylesheets=[dbc.themes.BOOTSTRAP],
    )
    dash_app.index_string = html_layout

    dash_app.layout = dbc.Container(
        
    )
    return dash_app.server
