# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 13:06:14 2022

@author: ninad
"""

# Importing Required Modules
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import dash_daq as daq

# Importing User-Defined Modules
import MyDashApp_Module as AppFuncs

# Instantiate our App and incorporate BOOTSTRAP theme Stylesheet
# Themes - https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes
# Themes - https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/
# hackerthemes.com/bootstrap-cheatsheet/

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

# App Layout using Dash Bootstrap

app.layout = dbc.Container([
    

    # Row 1
    dbc.Row([
        
        dbc.Col([
            
            html.H1("EP Generation", 
                    className = 'text-center text-primary mb-4')
            
            ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12
        
        ], justify = "center", align = "center"),

    
    dbc.Row([
        

        dbc.Col([
            
            # Database selection
            dcc.RadioItems(
                id = 'database_selection',
                labelStyle = {'display': 'block'},
                options = [
                    {'label' : "Our Database", 'value' : 1},
                    {'label' : "Your Files", 'value' : 2}
                    ]  ,
                    value = 1,
                    className = "mb-2"
            ),
            
            html.Br(),

            # Version selection
            dcc.Dropdown(['8.0.0','9.0.0','22.0.0','23.0.0'], '9.0.0', id='version-selection'),

            html.Br(),

            # Time-step selection
            html.Div([
                dbc.Stack([
                    html.Label("Time Step:",
                        className = 'text'), 
                    daq.NumericInput(id='time-step', className = 'ms-auto',
                        value=5,
                    ),
                ],
                direction="horizontal",
                ),
            ] ),



            

            

            html.Br(),

            ], xs = 12, sm = 12, md = 4, lg = 4, xl = 4), # width = 12
        
        
    
        dbc.Col([
            html.H3("Schedules",
                    className = 'text-center')
            ], xs = 12, sm = 12, md = 4, lg = 4, xl = 4),

        dbc.Col([
            html.H3("Building Type",
                    className = 'text-center')
            ], xs = 12, sm = 12, md = 4, lg = 4, xl = 4),
        
        ], justify = "center", align = "center"),


    # Break Row
    dbc.Row([
        
        dbc.Col([
            
            html.Br()
            
            ], width = 12),
        
        ]),  
    
    
    # Row 
    dbc.Row([
        
        dbc.Col([
            
            html.Button('Generate', id = 'Button_1', 
                        className = "btn btn-primary btn-lg col-12") ,
            
            ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12
        
        ], justify = "center", align = "center"),   

  
    
    
], fluid = False)


# App Callbacks - Providing Functionality

@app.callback(    
    Output(component_id = 'SineGraph', component_property = 'value'),
    Input(component_id = 'Button_1', component_property = 'n_clicks'),

    State(component_id = 'database-selection', component_property = 'value'),
    State(component_id = 'version-selection', component_property = 'value'),
    State(component_id = 'time-step', component_property = 'value'),
    
    prevent_initial_call = False)

def CreateOutput():
    
    output = 1

    return output
    
# Running the App
 
if __name__ == '__main__': 
    app.run_server(port=4050)