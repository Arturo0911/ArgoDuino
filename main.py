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


def growth_bacteria_simulation(ph_val, family):
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


def main():
    # init_process()

    # bacteria = pd.read_csv("data/data_train.csv")
    # lact_bac = bacteria[bacteria["Organisms"] == "37_lactobacillus_delbrueckii_bacteria"]
    # stre_bac = bacteria[bacteria["Organisms"] == "38_streptococcus_thermophilus_bacteria"]

    # lact_bac.reset_index(drop = True)
    # stre_bac.reset_index(drop = True)

    # bacteria_for_test = lact_bac.append(stre_bac, ignore_index = True)

    # bacteria_for_test.to_csv("data/bacterias_growth_test.csv", index = False)



if __name__ == "__main__":
    main()



