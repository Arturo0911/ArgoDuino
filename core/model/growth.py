"""Kinetic Growth"""

import pandas as pd
import numpy as np
from typing import Any, Union
from random import uniform
 

class BacteriaGrowth:
    
    """Kinetic bacteria growth"""
    def __init__(self,lactobacillus: list, streptococcus: list) -> None:
        self.lact_bac = lactobacillus
        self.strep_bac = streptococcus

    def simulation_bacterial_growth(self) -> Any:
        """The concentration of both bacteria strains is essential to make 
            the growth propertly."""
        pass

    def show_concentration(self) -> Union[np.ndarray, np.ndarray]:
        return np.array(self.lact_bac), np.array(self.strep_bac)



