import pandas as pd
import numpy as np
import pandas_profiling as prof

def get_RawProfile(df):
    return prof.ProfileReport(df)
