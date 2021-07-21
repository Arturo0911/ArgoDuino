#!/usr/bin/Python3

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pprint import pprint


def init_simulation(file_name: str):
    dataset= pd.read_csv("data/"+file_name)
    return dataset

# print(init_simulation("streptococcus_variant.csv"))

def checking_column():

    strep = init_simulation("streptococcus_variant.csv")
    stack_names = ["MEDIUM" if x >= 5.0 else "HIGH" for x in strep["ph_acidification"]]
    strep["acid_category"] = np.array(stack_names)
    
    strep.to_csv("strep_test.csv", index = False)

checking_column()

def ploting_charts():
    strep = pd.read_csv("strep_test.csv")

    plt.figure(figsize=(12,7))
    sns.scatterplot(x = "ufc/ml", y = "20_24_hours", hue = "acid_category", data = strep)
    plt.show()

ploting_charts()




