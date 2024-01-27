import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

airline_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv')

app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('Airline Performance Dashboard', style={'text-align':'center','font-size':40}),
                                
                                html.Div(['Input Year : ', dcc.Input(id='input-year', value='2010',
                                                                     type='number', style={'height':'50px','font-size':35})],
                                        style={'font-size':40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='line-plot'))
                                ])

@app.callback(Output(component_id='line-plot', component_property='figure'),
              Input(component_id='input-year',component_property='value'))

def get_graph(entered_year):
    ''' Function for Callback It automatically calls when there is some changes'''
    df = airline_data[airline_data['Year'] == int(entered_year)]
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

    fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker={'color':'green'}))
    fig.update_layout(title = 'Month vs Average Flight Delay Time',
                      xaxis_title='Month', yaxis_title='ArrDelay')
    return fig

if __name__ == '__main__':
    app.run()