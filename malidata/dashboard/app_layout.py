import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from .connect_database import conn

layout = dbc.Container([
    html.Div([
        html.H3('Thirteenth General Programme of Work, 2019-2023'),
    ], style={'textAlign': 'center', 'color': '#2E86C1', 'marginTop': '10px', 'marginBottom': '20px'}),
    html.Div([
        html.H4('Tracking Progress in the Triple Billion Targets'),
    ], style={'textAlign': 'center', 'color': 'white', 'backgroundColor': '#2E86C1', 'marginBottom': '20px',
              'height': '50px', 'line-height': '50px', 'paddingTop': '10px'}),
    dbc.Row(
        [
            dbc.Col(dbc.Card([
                    dbc.CardBody(
                        [
                            dbc.CardHeader([
                                html.H4("Universal Health Coverage"),
                            ], style={'textAlign': 'center', 'paddingTop': '15px', 'backgroundColor': '#D1F2EB', 'color': '#148F77'}),
                            html.H2("44 300", className="card-title", id="uhc-billion",
                                    style={'textAlign': 'center', 'marginTop': '15px'}),
                            html.Hr(),
                            html.P(
                                "Additional number of people benefiting from UHC in Mali compared to 2018, tracked via 15 indicators on coverage of essential health services and financial hardship.",
                                className="card-text",
                            ),
                            html.Hr(),
                            dbc.Button("2019", color="primary", className="me-1", id="uhc-btn-1", n_clicks=0),
                            dbc.Button("2023", outline=True, color="secondary", className="me-1", id="uhc-btn-2", n_clicks=0),
                            dbc.Button("2025", outline=True, color="secondary", className="me-1", id="uhc-btn-3", n_clicks=0),
                            html.Br(), html.Br(),
                            dbc.CardFooter([
                                html.Span("Source:", style={'font-weight': 'bold'}),
                                " WHO data and preliminary projections, 2021. ",
                                dbc.CardLink("Learn more", href="https://portal.who.int/triplebillions/Home/FAQ")
                            ]),
                        ]),
            ], color="success", outline=True), width=4),
            dbc.Col(dbc.Card([
                    dbc.CardBody(
                        [
                            dbc.CardHeader([
                                html.H4("Health Emergencies Protection"),
                            ], style={'textAlign': 'center', 'paddingTop': '15px', 'backgroundColor': '#2874A6', 'color': 'white'}),
                            html.H2("711 500", className="card-title", id="hep-billion",
                                    style={'textAlign': 'center', 'marginTop': '15px'}),
                            html.Hr(),
                            html.P(
                                "Additional number of people better protected from health emergencies in Mali compared to 2018, tracked via six indicators.",
                                className="card-text",
                            ),
                            html.Hr(),
                            dbc.Button("2019", color="primary", className="me-1", id="hep-btn-1", n_clicks=0),
                            dbc.Button("2023", outline=True, color="secondary", className="me-1", id="hep-btn-2", n_clicks=0),
                            dbc.Button("2025", outline=True, color="secondary", className="me-1", id="hep-btn-3", n_clicks=0),
                            html.Br(), html.Br(),
                            dbc.CardFooter([
                                html.Span("Source:", style={'font-weight': 'bold'}),
                                " WHO data and preliminary projections, 2021. ",
                                dbc.CardLink("Learn more", href="https://portal.who.int/triplebillions/Home/FAQ")
                            ]),
                        ]),
            ], color="success", outline=True), width=4),
            dbc.Col(dbc.Card([
                    dbc.CardBody(
                        [
                            dbc.CardHeader([
                                html.H4("Healthier Populations"),
                            ], style={'textAlign': 'center', 'paddingTop': '15px', 'backgroundColor': '#76448A', 'color': 'white'}),
                            html.H2("-241 800", className="card-title", id="hpp-billion",
                                    style={'textAlign': 'center', 'marginTop': '15px'}),
                            html.Hr(),
                            html.P(
                                "Additional number of people enjoying better health and well-being in Mali compared to 2018, tracked via 16 SDG indicators.",
                                className="card-text",
                            ),
                            html.Hr(),
                            dbc.Button("2019", color="primary", className="me-1", id="hpp-btn-1", n_clicks=0),
                            dbc.Button("2023", outline=True, color="secondary", className="me-1", id="hpp-btn-2", n_clicks=0),
                            dbc.Button("2025", outline=True, color="secondary", className="me-1", id="hpp-btn-3", n_clicks=0),
                            html.Br(), html.Br(),
                            dbc.CardFooter([
                                html.Span("Source:", style={'font-weight': 'bold'}),
                                " WHO data and preliminary projections, 2021. ",
                                dbc.CardLink("Learn more", href="https://portal.who.int/triplebillions/Home/FAQ")
                            ]),
                        ]),
            ], color="success", outline=True), width=4)
        ]),
        html.Br(), html.Br(),
        html.Div([
            html.H4('Indicators of Universal Health Coverage'),
        ], style={'textAlign': 'center', 'color': '#148F77', 'backgroundColor': '#D1F2EB', 'marginBottom': '20px',
                  'height': '50px', 'line-height': '50px', 'paddingTop': '10px'}),
])
