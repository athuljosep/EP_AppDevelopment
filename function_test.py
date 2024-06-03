# This function helps to test individual functionalities

import os
import MyDashApp_Module as AppFuncs

buildingType_selection = "Commercial_Prototypes"
FolderName = os.path.join("../../Data/", buildingType_selection)
# FilePath = os.path.join(os.getcwd(), FolderName)
FilePath = os.path.join(os.getcwd(), "../../Data/", buildingType_selection)
print(FilePath)

a = AppFuncs.list_contents(FilePath)
print(a)