import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv')

data = df.sample(n=500,random_state=42)

fig = px.pie(data, values='Flights', names='DistanceGroup', 
             title='Distance group proportion by flights')

app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('Airline Dashboard', style={'text-align':'center','color':'black','font-size':40}),
                                html.P('Proportion of distance group (250 mile distance interval group by flights.',style={'textAlign':'center','color':'#F57241'}), dcc.Graph(figure=fig)
                                ])

if __name__ == '__main__':
    app.run_server()