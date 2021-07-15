"""Kinetic Growth"""

import numpy as np
from typing import Any, Tuple, List
from math import (
    log2,
    log10
)

"""The goal is can be calculated the growth using CUF/ml
    Colony forming unit, this unit is used in microbiology 
    to estimate the number of viable bacteria or fungal cells 
    in a sample. Viable is defined as the ability to multiply
    voa binary fission under the controlled conditions."""


def csv_make_simulation():
    """
    """
    pass


class BacteriaGrowth:
    """Kinetic bacteria growth"""

    def __init__(self, lactobacillus: list, streptococcus: list, solution: float) -> None:
        """[summary]

        Args:
            lactobacillus (list): [description]
            streptococcus (list): [description]
            solution (float): [description]
        """
        self.lactic_bac = lactobacillus
        self.strep_bac = streptococcus
        self.solution = solution

    def show_concentration(self) -> Tuple[np.ndarray, np.ndarray]:
        return np.array(self.lactic_bac), np.array(self.strep_bac)

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

        number_generations = log10(float(final_number_individuals / initial_number_individuals)) / log2(1)
        time_generations = time_incubation / number_generations

        return number_generations, time_generations

    def simulation_bacterial_growth(self) -> Any:
        """The concentration of both bacteria strains is essential to make 
            the growth properly."""
        pass
