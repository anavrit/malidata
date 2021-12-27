import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from .dash_layout import html_layout
from .app_layout import layout
from .figures import uhc_figure
import dash_bootstrap_components as dbc
from .connect_database import conn

def init_dashboard(server):
    dash_app = dash.Dash(
        server = server,
        routes_pathname_prefix = "/dashboard/",
        external_stylesheets=[dbc.themes.BOOTSTRAP],
    )

    dash_app.index_string = html_layout
    dash_app.layout = layout

    @dash_app.callback(
        [Output('uhc-billion', 'children'),
         Output('uhc-btn-1', 'outline'),
         Output('uhc-btn-2', 'outline'),
         Output('uhc-btn-3', 'outline')],
        [Input('uhc-btn-1', 'children'),
         Input('uhc-btn-1', 'n_clicks'),
         Input('uhc-btn-2', 'children'),
         Input('uhc-btn-2', 'n_clicks'),
         Input('uhc-btn-3', 'children'),
         Input('uhc-btn-3', 'n_clicks')]
    )
    def uhc_billion(child1, n1, child2, n2, child3, n3):
        inputs = ['uhc-btn-1', 'uhc-btn-2', 'uhc-btn-3']
        ctx = dash.callback_context
        if not ctx.triggered:
            button_id = 'uhc-btn-1'
            year = int(child1)
        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            if button_id == inputs[0]:
                year = int(child1)
            elif button_id == inputs[1]:
                year = int(child2)
            else:
                year = int(child3)
        data = pd.read_sql(f"SELECT population FROM billions WHERE year={year} AND billion='UHC'", conn)
        return_style = {id: False if id == button_id else True for id in inputs}
        return str('{:,}'.format(data['population'][0]).replace(',', ' ')), return_style['uhc-btn-1'], return_style['uhc-btn-2'], return_style['uhc-btn-3']

    @dash_app.callback(
        [Output('hep-billion', 'children'),
         Output('hep-btn-1', 'outline'),
         Output('hep-btn-2', 'outline'),
         Output('hep-btn-3', 'outline')],
        [Input('hep-btn-1', 'children'),
         Input('hep-btn-1', 'n_clicks'),
         Input('hep-btn-2', 'children'),
         Input('hep-btn-2', 'n_clicks'),
         Input('hep-btn-3', 'children'),
         Input('hep-btn-3', 'n_clicks')]
    )
    def hep_billion(child1, n1, child2, n2, child3, n3):
        inputs = ['hep-btn-1', 'hep-btn-2', 'hep-btn-3']
        ctx = dash.callback_context
        if not ctx.triggered:
            button_id = 'hep-btn-1'
            year = int(child1)
        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            if button_id == inputs[0]:
                year = int(child1)
            elif button_id == inputs[1]:
                year = int(child2)
            else:
                year = int(child3)
        data = pd.read_sql(f"SELECT population FROM billions WHERE year={year} AND billion='HEP'", conn)
        return_style = {id: False if id == button_id else True for id in inputs}
        return str('{:,}'.format(data['population'][0]).replace(',', ' ')), return_style['hep-btn-1'], return_style['hep-btn-2'], return_style['hep-btn-3']

    @dash_app.callback(
        [Output('hpp-billion', 'children'),
         Output('hpp-btn-1', 'outline'),
         Output('hpp-btn-2', 'outline'),
         Output('hpp-btn-3', 'outline')],
        [Input('hpp-btn-1', 'children'),
         Input('hpp-btn-1', 'n_clicks'),
         Input('hpp-btn-2', 'children'),
         Input('hpp-btn-2', 'n_clicks'),
         Input('hpp-btn-3', 'children'),
         Input('hpp-btn-3', 'n_clicks')]
    )
    def hpp_billion(child1, n1, child2, n2, child3, n3):
        inputs = ['hpp-btn-1', 'hpp-btn-2', 'hpp-btn-3']
        ctx = dash.callback_context
        if not ctx.triggered:
            button_id = 'hpp-btn-1'
            year = int(child1)
        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            if button_id == inputs[0]:
                year = int(child1)
            elif button_id == inputs[1]:
                year = int(child2)
            else:
                year = int(child3)
        data = pd.read_sql(f"SELECT population FROM billions WHERE year={year} AND billion='HPP'", conn)
        return_style = {id: False if id == button_id else True for id in inputs}
        return str('{:,}'.format(data['population'][0]).replace(',', ' ')), return_style['hpp-btn-1'], return_style['hpp-btn-2'], return_style['hpp-btn-3']

    @dash_app.callback(
        Output('uhc-line-plot', 'figure'),
        [Input('uhc-dropdown', 'value')]
    )
    def uhc_line_plot(indicator):
        return uhc_figure(indicator)

    return dash_app.server
