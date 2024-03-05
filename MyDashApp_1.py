"""
Created on Tue Jan 30 15:32:25 2024

@author: Athul Jose P
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

    dbc.Row([
        html.H1("Buildings Data Analysis", className = 'text-center text-primary mb-4')
    ]),

    dcc.Tabs([
        
        # EP Generation Tab
        dcc.Tab(label='EP Generation', className = 'text-center text-primary mb-4', children=[
           
            # Row 1
            dbc.Row([
                
                # Column 1
                dbc.Col([
                    
                    html.Br(),

                    # Box 1 C1
                    # Database selection
                    dcc.RadioItems(
                        id = 'database_selection',
                        labelStyle = {'display': 'block'},
                        options = [
                            {'label' : " Our Database", 'value' : 1},
                            {'label' : " Your Files", 'value' : 2}
                            ]  ,
                        value = '',
                        className = 'ps-4 p-3',
                        style = {
                            'width': '100%',
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            }
                        ),
                    
                    html.Br(),

                    # Box 2 C1
                    html.Div([

                        # Upload IDF file
                        dcc.Upload(['Upload IDF file'],
                            className = 'center',
                            style = {
                                'width': '90%',
                                'height': '40px',
                                'lineHeight': '40px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin-left': '5%',
                                'margin-top': '5%'
                                }),

                        # Upload EPW file
                        dcc.Upload(['Upload EPW file'],
                            className = 'center',
                            style = {
                                'width': '90%',
                                'height': '40px',
                                'lineHeight': '40px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin': '5%',
                                }),

                        
                        # Version selection
                        dbc.Stack([
                            html.Label("Energy Plus Version:",
                                className = 'text'),
                            dcc.Dropdown(['8.0.0','9.0.0','22.0.0','23.0.0'], '',
                                id='version_selection',
                                style = {
                                    'width':'60%',
                                    'margin-left':'8%'
                                }),
                            ],direction="horizontal",
                            style = {
                                'width': '90%',
                                'margin': '5%',
                                }),

                        ],id = 'upload_files',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            #'display':'none'
                            }),

                    html.Br(),

                    # Box 3 C1
                    html.Div([

                        # Time-step selection
                        dbc.Stack([
                            html.Label("Time Step:",
                                className = 'text'), 
                            daq.NumericInput(id = 'time-step', 
                                value = 5,
                                style = {
                                    'margin-left':'28%'
                                    }),
                            ],direction = "horizontal",
                            style = {
                                'margin': '5%',
                                }),
                        
                        # Simulation reporting frequency selection
                        dbc.Stack([
                            html.Label("Simulation Reporting Frequency:",
                                className = 'text'), 
                            dcc.Dropdown(['timestep','hourly','detailed','daily','monthly','runperiod','environment','annual'], '',
                                id = 'simReportFreq_selection',
                                style = {
                                    'width':'70%',
                                    'margin':'2%'
                                    }),
                            ],direction = "horizontal",
                            style = {
                                #'width': '90%',
                                'margin': '5%',
                                }), 

                        ],id = 'simulation_details',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            },),

                    ], xs = 12, sm = 12, md = 4, lg = 4, xl = 4), # width = 12
                

                # Column 2
                dbc.Col([

                    html.Br(),

                    # Box 1 C2
                    html.Div([
                        html.H3("Schedules",
                            className = 'text-center mt-1'),
                        html.H6("People",
                            className = 'ms-2'),
                        html.H6("Equipment",
                            className = 'ms-2'),
                        html.H6("Light",
                            className = 'ms-2'),
                        html.H6("Exterior Light",
                            className = 'ms-2'),
                        html.H6("Heat/Cool Setpoint",
                            className = 'ms-2'),
                        ],id = 'schedules',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            },),
                    
                    html.Br(),

                    # Box 2 C2
                    html.Div([
                        html.Button('Generate Variables',
                            id = 'Button_1', 
                            className = "btn btn-secondary btn-lg col-12",
                            style = {
                                'width':'90%',
                                'margin':'5%'
                                },),

                        dcc.Dropdown(['var 1','var 2','var 3'], '',
                            id = 'variable_selection',
                            style = {
                                'width':'95%',
                                'margin-left':'2.5%',
                                'margin-bottom':'5%'
                                }),
                        
                        ],id = 'generate_variables',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            },),

                    html.Br(),

                    # Box 3 C2
                    html.Div([

                        dcc.Checklist([' Simulation Variables',' EIO',' IDF Object Records'],'',
                            id = 'download_selection',
                            style = {
                                'width':'95%',
                                'margin':'5%',
                            }),
                        
                        ],id = 'download_variables',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            },),

                            ], xs = 12, sm = 12, md = 4, lg = 4, xl = 4,),


                # Column 3
                dbc.Col([
                    
                    html.Br(),

                    # Box 1 C3
                    html.Div([

                        # Building type selection
                        html.Label("Building Type",
                            className = 'text-left ms-4 mt-1'),
                        dcc.Dropdown(['Commercial','Manufactured','Residential'], 'Commercial',
                            id='buildingType_selection',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',   
                                }),

                        # IDF type selection
                        html.Label("IDF Type",
                            className = 'text-left ms-4'),
                        dcc.Dropdown(['ASHRAE','IECC'], 'IECC',
                            id = 'idfType_selection',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',   
                                }),

                        # IDF year selection
                        html.Label("IDF Year",
                            className = 'text-left ms-4'),
                        dcc.Dropdown(['2012','2013','2015','2016','2018','2019'], '2013',
                            id='idfYear_selection',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',   
                                }),

                        # Building selection
                        html.Label("Building",
                            className = 'text-left ms-4'),
                        dcc.Dropdown(['ApartmentHighRise','Hospital','HotelLarge','HotelSmall','OfficeLarge','OfficeMedium','OfficeSmall'], 'OfficeSmall',         
                            id = 'building_selection',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',   
                                }),

                        # Location selection
                        html.Label("Location",
                            className = 'text-left ms-4'),
                        dcc.Dropdown(['Albuquerque','Atlanta','Buffalo','Denver','ElPaso','Fairbanks','GreatFalls','Honululu','InternationalFalls','NewYork','PortAngeles','Rochester','SanDiego','Seattle','Tampa','Tucson'], '',
                            id = 'location_selection',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',
                                'margin-bottom': '3%',   
                                },),

                        ],id = 'building_details',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            }),

                    html.Br(),
                    
                    # Box 2 C3
                    html.Div([

                        html.Button('Generate Data',
                            id = 'Button_2', 
                            className = "btn btn-secondary btn-lg col-12",
                            style = {
                                'width':'90%',
                                'margin':'5%'
                                },),

                        html.Button('Download Files',
                            id = 'Button_3', 
                            className = "btn btn-primary btn-lg col-12",
                            style = {
                                'width':'90%',
                                'margin-left':'5%',
                                'margin-bottom':'5%'
                                },),
                        
                        ],id = 'final_download',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            },),

                    ], xs = 12, sm = 12, md = 4, lg = 4, xl = 4,),
                
                ], justify = "center", align = "center"),  
            
        ]),
        
#################################################################################################
        
# # # # # #  Aggregation Tab # # # # # # # # #

#################################################################################################
        
        
        dcc.Tab(label = 'Aggregation', className = 'text-center text-primary mb-4', children = [

            dbc.Row([
                
                # First Column
                dbc.Col([
                    
                    # Input selection
                    dcc.RadioItems(
                    id = 'input_selection',
                    labelStyle = {'display': 'block'},
                    options = [
                        {'label' : " Continue Session", 'value' : 1},
                        {'label' : " Upload Files", 'value' : 2}
                        ]  ,
                    value = '',
                    className = 'ps-4 p-3',
                    style = {
                        'width': '100%',
                        'borderWidth': '1px',
                        'borderStyle': 'solid',
                        'borderRadius': '5px',
                        }
                    ),

                    html.Br(),

                    # Box 2 C1
                    html.Div([

                        # Upload Pickled Variable file
                        dcc.Upload(['Upload Pickled Variable file'],
                            className = 'center',
                            style = {
                                'width': '90%',
                                'height': '40px',
                                'lineHeight': '40px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin-left': '5%',
                                'margin-top': '5%'
                                }),

                        # Upload EIO file
                        dcc.Upload(['Upload EIO file'],
                            className = 'center',
                            style = {
                                'width': '90%',
                                'height': '40px',
                                'lineHeight': '40px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin': '5%',
                                }),


                        ],id = 'upload_aggr_files',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            #'display':'none'
                            }),

                    html.Br(),

                    # Aggregation Variables
                    html.Div([
                        dcc.RadioItems(
                            id = 'aggr_variable_selection',
                            labelStyle = {'display': 'block'},
                            options = [
                                {'label' : " Preselected Variables", 'value' : 1},
                                {'label' : " Custom Variables", 'value' : 2}
                                ]  ,
                            value = '',
                            className = 'ps-4 p-3',
                        ),

                        dcc.Dropdown(['Var1','Var2','Var3'], '',
                            id='aggr_variables',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',
                                'margin-bottom': '2.5%'
                                }),

                    ],id = 'aggr_variable_details',
                    hidden = True,
                    style = {
                        'borderWidth': '1px',
                        'borderStyle': 'solid',
                        'borderRadius': '5px',
                        },)

                ], xs = 12, sm = 12, md = 6, lg = 6, xl = 6,),

                # Second Column
                dbc.Col([
                    
                    # Box 1 C2
                    html.Div([

                        # Zone selection
                        html.Label("Zone Lists",
                            className = 'text-left ms-4 mt-1'),
                        dcc.Dropdown(['Zone list 1','Zone list 2','Zone list 3'], '',
                            id='zone_selection',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',   
                                }),

                        dcc.RadioItems(
                            id = 'aggregate_to',
                            labelStyle = {'display': 'block'},
                            options = [
                                {'label' : " Aggregate to one", 'value' : 1},
                                {'label' : " Custom Aggregation", 'value' : 2}
                                ]  ,
                            value = '',
                            className = 'ps-4 p-3',
                        ),

                        dcc.Dropdown(['Set 1','Set 2','Set 3'], '',
                            id='custom_aggr_variables',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',
                                #'margin-bottom': '2.5%'
                                }),

                        # Zone selection
                        html.Label("Type of Aggregation",
                            className = 'text-left ms-4 mt-1'),
                        dcc.Dropdown(['Type 1','Type 2','Type 3'], '',
                            id='type_selection',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%', 
                                'margin-bottom': '2.5%'  
                                }),

                    ],id = 'aggr_details',
                    hidden = True,
                    style = {
                        'borderWidth': '1px',
                        'borderStyle': 'solid',
                        'borderRadius': '5px',
                        },),


                    html.Br(),

                    # Box 2 C2
                    html.Div([


                        html.Button('Aggregate',
                            id = 'Button_4', 
                            className = "btn btn-secondary btn-lg col-12",
                            style = {
                                'width':'90%',
                                'margin':'5%'
                                },),

                        html.Button('Download',
                            id = 'Button_5', 
                            className = "btn btn-primary btn-lg col-12",
                            style = {
                                'width':'90%',
                                'margin-left':'5%',
                                'margin-bottom':'5%'
                                },),

                    ],id = 'aggr_download',
                    hidden = True,
                    style = {
                        'borderWidth': '1px',
                        'borderStyle': 'solid',
                        'borderRadius': '5px',
                        },)

                ], xs = 12, sm = 12, md = 6, lg = 6, xl = 6,)

                ])
            ])    
        
    ])

], fluid = False)

# App Callbacks - Providing Functionality

@app.callback(    
    Output(component_id = 'upload_files', component_property = 'hidden'),
    Output(component_id = 'simulation_details', component_property = 'hidden'),
    Output(component_id = 'schedules', component_property = 'hidden'),
    Output(component_id = 'generate_variables', component_property = 'hidden'),
    Output(component_id = 'download_variables', component_property = 'hidden'),
    Output(component_id = 'building_details', component_property = 'hidden'),
    Output(component_id = 'final_download', component_property = 'hidden'),
    Output(component_id = 'upload_aggr_files', component_property = 'hidden'),
    Output(component_id = 'aggr_variable_details', component_property = 'hidden'),
    Output(component_id = 'aggr_details', component_property = 'hidden'),
    Output(component_id = 'aggr_download', component_property = 'hidden'),
    #Input(component_id = 'Button_1', component_property = 'n_clicks'),
    #Input(component_id = 'Button_2', component_property = 'n_clicks'),
    #Input(component_id = 'Button_3', component_property = 'n_clicks'),

    Input(component_id = 'database_selection', component_property = 'value'),
    Input(component_id = 'version_selection', component_property = 'value'),
    Input(component_id = 'location_selection', component_property = 'value'),
    Input(component_id = 'simReportFreq_selection', component_property = 'value'),
    Input(component_id = 'variable_selection', component_property = 'value'),
    Input(component_id = 'download_selection', component_property = 'value'),
    Input(component_id = 'input_selection', component_property = 'value'),
    Input(component_id = 'aggr_variable_selection', component_property = 'value'),
    Input(component_id = 'type_selection', component_property = 'value'),
    
    #State(component_id = 'time-step', component_property = 'value'),
    #State(component_id = 'buildingType-selection', component_property = 'value'),

    prevent_initial_call = False)

def CreateOutput(database_selection, version_selection, location_selection, simReportFreq_selection, variable_selection, download_selection, input_selection, aggr_variable_selection, type_selection):
    
    # Tab 1 - EP Generation
    C1B3 = True
    C2B1 = True
    C2B2 = True
    C2B3 = True 
    C3B2 = True
    
    if database_selection == 1: # Our Database
        C1B2 = True
        C3B1 = False
        if location_selection == '':
            C1B3 = True
        else:
            C1B3 = False
         
    elif database_selection == 2: # Your Files
        C1B2 = False
        C3B1 = True
        if version_selection == '':
            C1B3 = True
        else:
            C1B3 = False

    else:
        C1B2 = True
        
        C3B1 = True
    
    if C1B3 == False and simReportFreq_selection != '':
        C2B1 = False
        C2B2 = False

    if C2B2 == False and variable_selection != '':
        C2B3 = False

    if C2B3 == False and download_selection != '':
        C3B2 = False

###########################################################
    # Tab 2 - Aggregation

    AC1B2 = True
    AC1B3 = True
    AC2B1 = True
    AC2B2 = True 

    if input_selection == 1: # Continue session
        AC1B3 = False

    elif input_selection == 2: # Upload files
        AC1B2 = False
    
    if aggr_variable_selection != '':
        AC2B1 = False

    if type_selection != '':
        AC2B2 = False

    return C1B2, C1B3, C2B1, C2B2, C2B3, C3B1, C3B2, AC1B2, AC1B3, AC2B1, AC2B2 
# Running the App
 
if __name__ == '__main__': 
    app.run_server(port=4050)