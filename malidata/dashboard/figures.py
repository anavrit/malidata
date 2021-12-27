import numpy as np
import pandas as pd
import plotly.graph_objs as go
from .connect_database import conn


def uhc_figure(indicator, country_list):

    # Extracting graph data from the database
    uhc = pd.read_sql(f"SELECT iso3, year, value, upper, lower FROM gpw13 WHERE indicator={indicator}", conn)
    uhc = uhc[uhc['iso3'].isin(country_list)]
    iso = pd.read_sql(f"SELECT id, iso3 FROM iso3", conn)
    iso = iso[iso['id'].isin(country_list)]
    iso3_list = iso['iso3'].unique()

    title_df = pd.read_sql(f"SELECT medium_name FROM indicator WHERE id={indicator}", conn)
    title = title_df['medium_name'][0]


    # Creating line chart
    uhc_fig = go.Figure()

    for i in range(len(iso3_list)):
        name = iso3_list[i]
        trace_id = iso.loc[iso['iso3']==name, 'id'].unique()[0]
        x = uhc.loc[uhc['iso3']==trace_id, 'year'].unique()
        x_rev = x[::-1]
        y = uhc.loc[uhc['iso3']==trace_id,'value'].values.tolist()
        y_upper = uhc.loc[uhc['iso3']==trace_id, 'upper'].values.tolist()
        y_lower = uhc.loc[uhc['iso3']==trace_id, 'lower'].values.tolist()
        y_lower = y_lower[::-1]

        uhc_fig.add_trace(
            go.Scatter(
                x=x, y=y,
                line_color='rgba(0, 100, 80)',
                name=name,
            )
        )
    uhc_fig.update_xaxes(tickangle=270, title_text='Year', title_standoff = 15, ticks='outside', showline=True, linecolor='black', mirror=True)
    uhc_fig.update_yaxes(showline=True, linecolor='black', ticks='outside', tickson='boundaries', mirror=True)
    uhc_fig.update_layout(hovermode="x unified",
                          xaxis=dict(tickmode='linear'),
                          margin=dict(l=30, r=30, t=80, b=20),
                          paper_bgcolor='rgba(0,0,0,0)',
                          plot_bgcolor='rgba(0,0,0,0)',
                          title={
                            'text': title,
                            'y': 0.9,
                            'x': 0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'
                          },
                          font_family="Sans-serif",
                          font_color="black",
                          title_font_family="Arial",
                          title_font_color='black')
    uhc_fig.update_traces(mode='lines+markers')
    return uhc_fig
