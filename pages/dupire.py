import dash
from dash import html, dcc, Input, Output, State, callback

dash.register_page(__name__, name='Dupire', path='/dupire')

layout = html.Div([])

