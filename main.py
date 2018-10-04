import pandas as pd
import numpy as np
import os
from data_clean import * 

print(os.listdir("data/Telco"))
#df = pd.read_csv("data/Telco/WA_Fn-UseC_-Telco-Customer-Churn.csv", parse_dates=True, encoding='UTF-8')
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'],columns=['one', 'two', 'three'])
df['four'] = 'bar'
df['five'] = df['one'] > 0
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
plot = get_RawProfile(df)
df = clean_missing(df, "fill", 999)
print(df.head())

