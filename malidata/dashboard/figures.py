import numpy as np
import pandas as pd
import plotly.graph_objs as go
from .connect_database import conn


def uhc_figure(indicator):
    # Extracting graph data from the database
    uhc = pd.read_sql(f"SELECT year, value, lower, upper FROM gpw13 WHERE indicator={indicator} AND iso3=115", conn)
    iso = pd.read_sql("SELECT iso3 FROM iso3 WHERE id=115", conn)
    name = iso['iso3'][0]
    title_df = pd.read_sql(f"SELECT medium_name FROM indicator WHERE id={indicator}", conn)
    title = title_df['medium_name'][0]
    x = uhc['year'].values.tolist()
    x_rev = x[::-1]
    y = uhc['value'].values.tolist()
    y_upper = uhc['upper'].values.tolist()
    y_lower = uhc['lower'].values.tolist()

    uhc_fig = go.Figure()
    uhc_fig.add_trace(go.Scatter(
        x=x+x_rev,
        y=y_upper+y_lower,
        fill='toself',
        fillcolor='rgba(0,100,80,0.2)',
        line_color='rgba(255,255,255,0)',
        showlegend=False,
        name=name,
    ))
    uhc_fig.add_trace(
        go.Scatter(
            x=x, y=y,
            line_color='rgba(0,100,80)',
            name=name,
        )
    )
    uhc_fig.update_xaxes(tickangle=270, title_text='Year', title_standoff = 15, ticks='outside', showline=True, linecolor='black', mirror=True)
    uhc_fig.update_yaxes(showline=True, linecolor='black', ticks='outside', mirror=True)
    uhc_fig.update_traces(mode='markers+lines',
                          marker=dict(size=6,
                                      line=dict(width=1, color='white')))
    uhc_fig.update_layout(hovermode="x unified",
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
    return uhc_fig
