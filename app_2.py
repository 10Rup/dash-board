from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
# import dash_design_kit as ddk # need licence for using this
import dash_bootstrap_components as dbc

res_data = pd.read_csv("result_data.csv")

# print(res_data)

app = Dash(__name__)

app.layout=dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(options=list(res_data.columns),id='column-selector',value="")
        ], width=4)
    ]),
    dbc.Row([
        
        dash_table.DataTable(data=res_data.to_dict('records'), page_size=12)        
    ]),

    dbc.Row([
        dcc.Graph(id='bar-graph',
            figure=px.bar(data_frame=res_data, x='coursename', y='stu_cnt', color='trsemcode', title="Course wise semester wise data"))
    ]),

    dbc.Row([
        dcc.Graph(figure=px.scatter(data_frame=res_data, x='coursecd', y='stu_cnt',
                                    color='semname',size='stu_cnt'))
    ])
])

if __name__=="__main__":
    app.run(debug=True)