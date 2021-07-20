#!/usr/bin/python

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



MICROORGANISM = 10000000 # CFU/ml
MILK_FAT = 0.15 # milk fat percent
PROTEINS = 0.027 # m/m milk proteins
ACIDITY = 0.006 # titratble acidity


def second_process():
	pass

def init_process():

    reading_file = pd.read_csv("data/milk_grading.csv")

    ph_values = reading_file["pH"] # pH columng for analysis
    temperature_values = reading_file["Temprature"] # variation temperature


    """
    Producing yogurt requires milk to acidify, wehereupon curs are
    formed. This acidification process, which has to be rapid in
    industrial settings, largegly depens on the growth and the activity
    of bacteria that produce lactic acid by fermenting lactose. The
    association between the two yogurt lactic acid bacteria (LAB)
    Streptococcus Thermophilus and lactobacillus bulgarius is regarded
    as a procooperation because it's befeicial for both species, but
    each bacterium can grow alone in milk. Tis protocooperation has
    industrial importance because it can improve yogurt¿s properties,
    such as the texture, the acidification rate and the flavor.

    """

    dilusion_vases = 100 # in ml
    cfu = 100000 # cfu/ml

    # the inoculation was for 
    incoluation = 0.01 # 1% percent

    for x in range(10):
        continue



def presenting_bacteria_growth():

    """bacteria = pd.read_csv("data/growth_curve.csv")
    plt.figure(figsize=(12,7))
    sns.scatterplot(x ="time", y = "growth_log", data = bacteria)
    plt.show()"""

    curve = pd.read_csv("data/growth_curve.csv")

    # presenting the growth and time
    plt.figure(figsize=(7,7))
    sns.scatterplot(data= curve)

    # As we can see, the growth was stoped at the 15h from the start
    # that's mean, that there are a lapse that the bacteria stop their
    # growth .
    plt.figure(figsize=(12,7))
    sns.scatterplot(x = "time", y = "growth_log", data = curve)


    # bar plot of growth
    plt.figure(figsize=(12,7))
    sns.barplot(x = "time", y = "growth_log", data = curve)




# this simultaion is taking in mind, the several changes through
# the time in range of 0 to 24 hours

def making_growth_simulation():

    # loading datasets.
    curve = pd.read_csv("data/growth_curve.csv")
    strep = pd.read_csv("data/streptococcus.csv")
    lact = pd.read_csv("data/lactobacillus.csv")


    # get the real value percent of growth through hours
    def getting_relevants_values():
        return [float(sum(curve[curve["time"] == x]["growth_log"].to_numpy())/4) for x in curve["time"].unique()]

    growth = getting_relevants_values()
    growth = [float("{0:.2f}".format(x)) for x in growth]
    stack_percent = [float("{0:.2f}".format((growth[x] / growth[x-1]))) for x in range(1, len(growth))]

    # in each parameter of values relevant hours, we make simuilation of growth using its percent
    def simulate_growing(datacurve: list, process_values: list, dataset_element: list ):

        hours = datacurve["time"].unique()
        data = {}
        for x in range(1,len(hours)):
            data["%s_%s_hours"%(hours[x-1],hours[x])] = [float("{0:.2f}".format(i*process_values[x-1])) for i in dataset_element["ufc/ml"].to_numpy()]

        return data

    # making for each dataset
    strep_values = simulate_growing(curve, stack_percent, strep)
    lact_values = simulate_growing(curve, stack_percent, lact)

    # conncat every value to its respective dataset and finally 
    # conver into csv file the new elemnts in the dataset
    for x in strep_values:
        strep[x] = np.array(strep_values[x])

    for x in lact_values:
        lact[x] = np.array(lact_values[x])


    strep.to_csv("data/growth_strep.csv", index= False)
    lact.to_csv("data/growth_lact.csv", index= False)




def evaluation_dataset():
    data = pd.read_csv("data/growth_lact.csv")
    
    plt.figure(figsize = (12,7))
    # sns.heatmap(strep.corr(method = "pearson"), annot = True, linewidths=.5)
    sns.scatterplot(x= "pH_initial_", y = "ufc/ml", data = data)
    plt.show()
    # print(strep.describe())


def main():

    evaluation_dataset()
    
if __name__ == "__main__":
    main()



