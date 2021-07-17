"""Kinetic Growth"""

import pandas as pd
import os
import numpy as np
from typing import Any, Tuple
from math import (
    log2,
    log10
)
import csv
import seaborn as sns
import matplotlib.pyplot as plt

"""The goal is can be calculated the growth using CUF/ml
    Colony forming unit, this unit is used in microbiology 
    to estimate the number of viable bacteria or fungal cells 
    in a sample. Viable is defined as the ability to multiply
    voa binary fission under the controlled conditions."""


def growth_bacterial_chart(file_path: str):
    bacterial_csv = pd.read_csv(file_path)
    sns.scatterplot(x="time", y="growth_log", data=bacterial_csv)
    plt.show()


def csv_make_simulation():
    class CSVMaker:

        def __init__(self) -> None:
            self.dir_name = "yogurt_simulation"

        def create_directories(self) -> None:
            if not os.path.exists(self.dir_name):
                os.makedirs(self.dir_name)
            with open(self.dir_name + "/yogurt_dataset.csv", "w") as file:
                writer = csv.writer(file)
                writer.writerow(
                    []
                )

        def fill_directories(self, *args) -> None:
            with open(self.dir_name + "/yogurt_dataset.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [args[0], args[1], args[2], args[3]]
                )

    CSVMaker().create_directories()


class BacteriaGrowth:
    """Kinetic bacteria growth"""

    def __init__(self,colonies_number: float,
                 lactobacillus: list, streptococcus: list,
                 total_dilution_factor: float, solution: float,
                 volume_culture_plate: float) -> None:

        self.lactic_bac = lactobacillus
        self.strep_bac = streptococcus
        self.solution = solution
        self.colonies_number = colonies_number
        self.total_dilution_factor = total_dilution_factor
        self.volume_culture_plate = volume_culture_plate

    def show_concentration(self) -> Tuple[np.ndarray, np.ndarray]:
        return np.array(self.lactic_bac), np.array(self.strep_bac)

    def estimation_bacterial_concentration(self):
        pass

    @staticmethod
    def calculating_concentration(initial_number_individuals: float, final_number_individuals: float,
                                  time_incubation: float) -> Tuple[float, float]:
        """[summary]
            n = log((# final of entities / initial number of individuals ))
        Returns:
            [numbers_generations]: [when we have a simple sample of bacterias in one environment, the generations are
                calculated using the above formula]
            [time_generations]: [ time that every father take to make generations]
        """

        """There are two periods in th yogurt production: 
            - Fermentation
            - Post_acidification
        """

        number_generations = log10(float(final_number_individuals / initial_number_individuals)) / log2(1)
        time_generations = time_incubation / number_generations

        return number_generations, time_generations

    def simulation_bacterial_growth(self) -> Any:
        """The concentration of both bacteria strains is essential to make 
            the growth properly."""
        pass


def create_csv_value():
    pass