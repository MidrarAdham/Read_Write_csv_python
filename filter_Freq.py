import pandas as pd
import csv

data = pd.read_csv("F_resp.csv",usecols=[1])

data.to_csv('just_freq.csv',index=False)