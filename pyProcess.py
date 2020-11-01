import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def correct_data(ufo_data): #correct datetime, fillna, title(),str.upper(), to_numeric
    ufo_data['datetime'] = pd.to_datetime(ufo_data['datetime'], errors='coerce')
    ufo_data.insert(1, 'year', ufo_data['datetime'].dt.year)
    ufo_data['year'] = ufo_data['year'].fillna(0).astype(int)
    ufo_data['city'] = ufo_data['city'].str.title()
    ufo_data['state'] = ufo_data['state'].str.upper()
    ufo_data['latitude'] = pd.to_numeric(ufo_data['latitude'], errors='coerce')
    ufo_data = ufo_data.rename(columns={'longitude ':'longitude'})


#some feature engineering
def grep_year(x): #1- Sight year 2- Date the posted year
    x = x.split(" ")[0]
    x = x.split("/")[2]
    x = int(x)
    return x
    # df["Sight-Year"] = df['datetime'].apply(grep_year)
    # df["Date-Posted-Year"] = df['date posted'].apply(grep_year)

def conv_season(x):
    x = int(x.split("/")[0])
    
    if x in range(3,6):
        return "Spring"
    if x in range(6,9):
        return "Summer"
    if x in range(9,12):
        return "Autumn"
    if x == 12 or x == 1 or x == 2:
        return "Winter"
    #df["Season"] = df['datetime'].apply(conv_season)

def check_datetime(df): #check if they are datetime!
    data = [pd.to_datetime(df[x]) if df[x].astype(str).str.match(r'\d{4}-\d{2}-\d{2} \d{2}\:\d{2}\:\d{2}').all() else df[x] for x in df.columns]
    return data
