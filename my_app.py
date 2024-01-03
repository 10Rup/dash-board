from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
# import dash_design_kit as ddk # need licence for using this
import dash_bootstrap_components as dbc



# data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# styling
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']




# NORMAL DASHBOARD EXAMPLE
# app = Dash(__name__)
# app.layout = html.Div([
    # html.Div(children="hello!.."),
    # html.Hr(),
    # dcc.RadioItems(options = ['pop','lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-items'),
    # dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    # dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
# ])


# DASHBOARD WITH STYLE
# app = Dash(__name__, external_stylesheets=external_stylesheets)
# app.layout = html.Div([
#     html.Div(className='row', children='The Dashboard',
#              style={'textAlign':'center', 'color':'blue','fontSize':50}),
#     html.Hr(),
#     html.Div(className='row',children=[
#         dcc.RadioItems(options = ['pop','lifeExp', 'gdpPercap'], value='lifeExp', inline=True, id='controls-and-radio-items')
#     ] ),
#     html.Div(className='row', children=[
#         html.Div(className='six columns', children=[
#             dash_table.DataTable(data=df.to_dict('records'), page_size=11,
#                                  style_table={'overflowX':'auto'})
#         ]),

#         html.Div(className="six columns", children=[
#             dcc.Graph(figure={}, id='control-graph-output')
#         ])
#     ])
    
# ])

# bootstrap theme
external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)


app.layout=dbc.Container([
    dbc.Row([
        html.Div(children="Dashboard with Bootstrap",className="text-primary text-centre fs-3")
    ]),
    dbc.Row([
        dcc.RadioItems(options=[{'label':x, 'value':x} for x in ['pop','lifeExp', 'gdpPercap']],
                    value='lifeExp',
                    inline=True,
                    id='boot-radio-button')

        
        
    ]),

    dbc.Row([
        dbc.Col([
            dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
        ], width=6),

        dbc.Col([
            dcc.Graph(figure={}, id='update-graph-data')
        ], width=6)
        
    ]),


])


# For normal or style Dashboard
# @callback(
#     Output(component_id='control-graph-output',component_property='figure'),
#     Input(component_id='controls-and-radio-items', component_property='value')
# )
# def update_graph(value_selected):
#     fig =px.histogram(df, x='continent', y=value_selected, histfunc='avg')
#     return fig




# For Bootstrap Dashboard
@callback(
    Output(component_id='update-graph-data', component_property='figure'),
    Input(component_id='boot-radio-button', component_property='value')
)
def updade_boot_graph(radio_choice):
    fig = px.histogram(df, x='continent', y=radio_choice, histfunc='avg')
    return fig

if __name__ =='__main__':
    app.run(debug=True)
