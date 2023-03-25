import numpy as np
import pandas as pd
from csv import writer

def append_to_csv(csvpath, data):
    with open(csvpath, 'a') as appendObj:
        append = writer(appendObj)
        append.writerow(data)


def data_clean():
    df=pd.read_csv("Sleep_Efficiency.csv")
    df.head()
    df.rename(columns = {'Wakeup time':'Wakeup_time', 'Sleep duration':'Sleep_duration ',"Sleep efficiency":"Sleep_efficiency",
                     "REM sleep percentage":"REM_sleep_percentage","Deep sleep percentage":"Deep_sleep_percentage",
                     "Light sleep percentage":"Light_sleep_percentage","Caffeine consumption":"Caffeine_consumption",
                     "Alcohol consumption":"Alcohol_consumption","Smoking status":"Smoking_status","Exercise frequency":"Exercise_frequency"}, inplace = True)
    #df.info()
    #df.head()

