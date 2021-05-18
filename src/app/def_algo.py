import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

dataset = pd.read_csv("CoCoAnDa_Daten/19_06_25_DHB_Goal.csv")
#dataset = dataset.dropna()

le = LabelEncoder()
dataset["player_name"] = le.fit_transform(dataset["player_name"])   
dataset.rename(columns={'player_name':'player_id'}, inplace=True)

print(dataset)

def def_algo(dataset):

    return dataset


def ang_algo(dataset):

    return dataset
