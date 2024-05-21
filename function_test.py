import os
import MyDashApp_Module as AppFuncs

os.chdir("C:/Users/athul.p/Documents/GitHub/plotly-works")

simName = "Simulation2"
simName_FilePath = os.path.join(os.getcwd(), simName)
IDF_FilePath = "C:/Users/athul.p/Documents/GitHub/plotly-works/Files_to_copy/ASHRAE901_OfficeSmall_STD2013_Seattle.idf"
Weather_FilePath = "C:/Users/athul.p/Documents/GitHub/plotly-works/Files_to_copy/USA_WA_Seattle-Tacoma.Intl.AP.727930_TMY3.epw"
print(f"working directory is {simName_FilePath}")

AppFuncs.create_simulation_folder(simName_FilePath, IDF_FilePath, Weather_FilePath)