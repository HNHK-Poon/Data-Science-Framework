import pandas as pd
import numpy as np
import os
from data_clean import * 

print(os.listdir("data/google_apps"))
df = pd.read_csv("/home/yapws/Documents/Peter/Data-Science-Framework/data/google_apps/googleplaystore.csv")
plot = get_RawProfile(df)

