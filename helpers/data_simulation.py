#!/usr/bin/Python3

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def init_simulation(file_name: str):
    dataset = pd.read_csv("data/" + file_name)
    return dataset


# print(init_simulation("streptococcus_variant.csv"))

def checking_column():
    strep = init_simulation("streptococcus_variant.csv")
    stack_names = ["MEDIUM" if x >= 5.0 else "HIGH" for x in strep["ph_acidification"]]
    strep["acid_category"] = np.array(stack_names)

    strep.to_csv("strep_test.csv", index=False)


checking_column()


def plotting_charts():
    strep = pd.read_csv("strep_test.csv")

    plt.figure(figsize=(12, 7))
    sns.scatterplot(x="ufc/ml", y="20_24_hours", hue="acid_category", data=strep)
    plt.show()


plotting_charts()


class BacterialGrowth:
    PANDAS_DATAFRAME = pd.core.frame.DataFrame

    def __init__(self):
        pass

    def make_dataset_for_simulation(self):
        pass

    @staticmethod
    def make_categories(fat_milk: float, proteins: float, tritatable_acidity: float):

        if fat_milk >= 3.25 and proteins >= 2.4 and tritatable_acidity >= 0.9:
            return "Regular yogurt"
        elif (3.25 > fat_milk > 1.1) and proteins >= 2.4 and tritatable_acidity >= 0.9:
            return "Low fat yogurt"
        elif fat_milk <= 1.1 and proteins >= 2.4 and tritatable_acidity >= 0.9:
            return "Non fat yogurt"

    @staticmethod
    def create_dataset(num_rows=10000) -> PANDAS_DATAFRAME:

        # this dataset is for regression model
        general_dataset = pd.DataFrame(data={
            'titratable_acidity': np.array([float("{0:.3f}".format(uniform(0.95, 1.19))) for _ in range(num_rows)]),
            'fat_milk_over_100mg_': np.array([float("{0:.4f}".format(uniform(1, 4))) for _ in range(num_rows)]),
            'pH_sour_milk_initial': np.array([float("{0:.3f}".format(uniform(4.4, 4.6))) for _ in range(num_rows)]),
            'streptococcus_strain_': np.array([float("{0:.3f}".format(uniform(4.0, 6.0))) for _ in range(num_rows)]),
            'lactobacillus_strain_': np.array([float("{0:.3f}".format(uniform(4.0, 6.0))) for _ in range(num_rows)]),
            'minimum_milk_proteins': np.array([float("{0:.3f}".format(uniform(2.4, 2.7))) for _ in range(num_rows)]),
            "ideal_temperature_c": np.array([float("{0:.3f}".format(uniform(40, 42))) for _ in range(num_rows)]),
        })

        # that one is for classification model
        # classification_dataset = pd.DataFrame(data = {})

        return general_dataset
