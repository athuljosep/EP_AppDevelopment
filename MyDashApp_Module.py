# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:47:14 2022

@author: ninad
"""

# Importing Desired Modules
import numpy as np
import pandas as pd
import os
import shutil


# My App Module

def CreateTimeVector(TimeDuration, TimeStep):
    
    TimeVector = np.arange(0, TimeDuration, TimeStep)
    
    TimeVector = np.reshape(TimeVector,(TimeVector.shape[0],1))
    
    return TimeVector

def CreateSine(TimeVector, A, F, P):
    
    Sine = A*np.sin(2*np.pi*F*TimeVector+np.radians(P))
    
    return Sine
    
def Compute_with_Sines(TimeVector, Sine1, Sine2, Computation_Option):
    
    # omputing new Sine Wave
    
    if (Computation_Option == 1): # Addition
    
        Sine_New = Sine1 + Sine2
    
    elif (Computation_Option == 2): # Subtraction
    
        Sine_New = Sine1 - Sine2
    
    elif (Computation_Option == 3): # Multiplication
    
        Sine_New = Sine1 * Sine2
        
    # Creating a Combined Table for Graphing purposes
    Combined_Array = np.hstack((TimeVector, Sine1, Sine2, Sine_New))
    
    Sines_DF = pd.DataFrame(Combined_Array, columns = ['Time','Sine_1','Sine_2','Sine_New'])
    
    return Sines_DF



def create_simulation_folder(simName_FilePath, IDF_FilePath, Weather_FilePath):
    # Create the main folder
    os.makedirs(simName_FilePath, exist_ok=True)
    
    # Create the Temporary Folder inside the main folder
    temp_folder = os.path.join(simName_FilePath, "Temporary Folder")
    os.makedirs(temp_folder, exist_ok=True)
    
    # Copy the IDF file to the Temporary Folder
    if os.path.isfile(IDF_FilePath):
        shutil.copy(IDF_FilePath, temp_folder)
    else:
        print(f"IDF file not found: {IDF_FilePath}")
    
    # Copy the Weather file to the Temporary Folder
    if os.path.isfile(Weather_FilePath):
        shutil.copy(Weather_FilePath, temp_folder)
    else:
        print(f"Weather file not found: {Weather_FilePath}")
    
    print(f"Files copied to {temp_folder}")


