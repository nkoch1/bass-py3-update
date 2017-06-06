# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

def string_eval(string):
    """
    Converts a string to a float, if possible. Otherwise, returns a string.
    Parameters
    ----------
    string : str,
    Returns
    -------
    string : str
    num : float
    """
    try:
        num = float(string)
        return num
    except ValueError:
        return string
    
Data = {}
Settings = {}
Results ={}

Settings['folder']= 'C:\\Users\nils\bass-py3-update' #input('Full File Path to Folder containing file: ')
Settings['Label'] = 'rat34_ECG.txt' #input('File Name: ')
Settings['Output Folder'] = 'C:\\Users\nils\bass-py3-update\output' #input('Full File Path to Output Folder: ')
Settings['Settings File'] = r'C:\\Users\nils\bass-py3-update\rat34_Settingsnk.csv'

#The following settings are temporarily set perminently to this. In the future, file type will be selectable
Settings['Graph LCpro events'] = False
Settings['File Type'] = 'Plain' #'LCPro', 'ImageJ', 'SIMA', 'Plain', 'Morgan'
Settings['Milliseconds'] = False

settings_temp = pd.read_csv(Settings['Settings File'], index_col=0, header=0, sep='\t')

exclusion_list = ['plots folder', 'folder',
                  'Sample Rate (s/frame)', 'Output Folder',
                  'Baseline', 'Baseline-Rolling', 'Settings File', 'Time Scale',
                  'Label', 'File Type', 'HDF Key', 'HDF Channel']
settings_temp = settings_temp.iloc[:,0]
for key, val in settings_temp.iteritems():

    if key in exclusion_list:
        continue
    else:
        #print(key, val
        Settings[key] = string_eval(val)

        if val == 'True':
            Settings[key] = True
        if val == 'False':
            Settings[key] = False
            
