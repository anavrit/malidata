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
    return str(f"{data['population'][0]:,}"), return_style['uhc-btn-1'], return_style['uhc-btn-2'], return_style['uhc-btn-3']