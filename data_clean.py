import pandas as pd
import numpy as np
import pandas_profiling as prof
import webbrowser
import os
import matplotlib.pyplot as plt
import missingno as msno

def get_RawProfile(df):
    profile = prof.ProfileReport(df)
    profile.to_file(outputfile="myoutputfile.html")
    parent_path = os.getcwd()
    path = parent_path + "/myoutputfile.html"
    chrome_path = '/usr/bin/google-chrome %s'
    webbrowser.get(chrome_path).open(path)
    #msno.matrix(df)
    return prof.ProfileReport(df)

def clean_missing(df,mode="drop",value=0, axis=0):
    if mode == "drop":
        return df.dropna(inplace=True, axis=axis)
    elif mode == "fill":
        return df.fillna(value)
    else:
        print("Wrong mode: only (drop / fill)")

def clean_missing_pro(df, columns_to_fill, values_to_fill, axis=0):
    typ = type(values_ro_fill)
    if typ == "list":
        if len(columns_to_fill) != len(values_to_fill):
            raise ValueError('Size or columns and value to fill is not same.')
        for i,col in enumerate(columns_to_fill):
            df[col] = df[col].fillna(values_to_fill[i])
    elif typ == "str" or typ == "int" or typ == "float" :
        for col in columns_to_fill:
            df[col] = df[col].fillna(values_to_fill)
    else:
        raise ValueError("Not a proper filling type.")

    return df.dropna(inplace=True, axis=axis)
        
                
    
