"""Kinetic Growth"""

import numpy as np
from typing import Any, Union
from random import (
    uniform, 
    randint
)
from math import (
    log2,
    log10
)
 
"""The goal is can be calculated the growth using CUF/ml
    Colony forming unit, this unit is used in microbiology 
    to stimate the number of viable bacteria or fungal cells 
    in a sample. Viable is defined as the ability to multiply
    voa binary fission under the controlled conditions."""


class BacteriaGrowth:
    
    """Kinetic bacteria growth"""
    def __init__(self,lactobacillus: list, streptococcus: list, solution: float) -> None:
        """[summary]

        Args:
            lactobacillus (list): [description]
            streptococcus (list): [description]
            solution (float): [description]
        """
        self.lact_bac = lactobacillus
        self.strep_bac = streptococcus

    def show_concentration(self) -> Union[np.ndarray, np.ndarray]:
        return np.array(self.lact_bac), np.array(self.strep_bac)

    def calculating_concentration(self, initial_number_individuals: float, final_number_individuals: float, time_incubation: float) -> Union[float, float]:
        
        """[summary]
            n = log((# final of entities / initial number of individuals ))
        Returns:
            [type]: [description]
        """

        number_generations = log10(float(final_number_individuals/initial_number_individuals))/ log2(1)
        time_generations = time_incubation / number_generations

        return number_generations, time_generations
    
    def simulation_bacterial_growth(self) -> Any:
        """The concentration of both bacteria strains is essential to make 
            the growth propertly."""
        pass



