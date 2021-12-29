import numpy as np
import pandas as pd
import plotly.graph_objs as go
from .connect_database import conn
from .colors import colors, fillcolors
import textwrap

def uhc_figure(indicator, country_list):

    # Extracting graph data from the database
    uhc = pd.read_sql(f"SELECT iso3, year, value, upper, lower FROM gpw13 WHERE indicator={indicator}", conn)
    uhc = uhc[uhc['iso3'].isin(country_list)]
    uhc[['value', 'lower', 'upper']] = uhc[['value', 'lower', 'upper']].round(2)
    iso = pd.read_sql(f"SELECT id, iso3 FROM iso3", conn)
    iso = iso[iso['id'].isin(country_list)]

    title_df = pd.read_sql(f"SELECT long_names FROM long_name WHERE id={indicator}", conn)
    title = title_df['long_names'][0]
    split_text = textwrap.wrap(title, width=80)


    # Creating line chart
    uhc_fig = go.Figure()

    for id in country_list:
        name = iso.loc[iso['id']==id, 'iso3'].values.tolist()[0]
        x = uhc.loc[uhc['iso3']==id, 'year'].unique()
        y = uhc.loc[uhc['iso3']==id, 'value'].values.tolist()
        y_upper = uhc.loc[uhc['iso3']==id, 'upper'].values.tolist()
        y_lower = uhc.loc[uhc['iso3']==id, 'lower'].values.tolist()
        uhc_fig.add_trace(go.Scatter(
            x=x,
            y=y_upper,
            line=dict(color=colors[name], width=0.1),
            marker=dict(size=0),
            showlegend=False,
            hoverinfo="skip",
        ))
        uhc_fig.add_trace(
            go.Scatter(
                x=x, y=y,
                mode='lines+markers',
                line=dict(color=colors[name], width=1),
                fill='tonexty',
                fillcolor=fillcolors[name],
                name=name,
            ))
        uhc_fig.add_trace(go.Scatter(
            x=x,
            y=y_lower,
            line=dict(color=colors[name], width=0.1),
            marker=dict(size=0),
            fill='tonexty',
            fillcolor=fillcolors[name],
            showlegend=False,
            hoverinfo="skip",
        ))

    uhc_fig.update_xaxes(tickangle=270, title_text='Year', title_standoff = 15, ticks='outside', showline=True, linecolor='black', mirror=True)
    uhc_fig.update_yaxes(showline=True, linecolor='black', ticks='outside', tickson='boundaries', mirror=True)
    uhc_fig.update_layout(hovermode="x unified",
                          xaxis=dict(tickmode='linear'),
                          margin=dict(l=30, r=30, t=50, b=20),
                          paper_bgcolor='rgba(20,143,119,0.1)',
                          plot_bgcolor='white',
                          title={
                            'text': '<br>'.join(split_text),
                            'y': 0.95,
                            'x': 0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'
                          },
                          font_family="Sans-serif",
                          font_color="black",
                          title_font_family="Arial",
                          )
    return uhc_fig
