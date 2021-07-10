"""Kinetic Growth"""

import pandas as pd
import numpy as np


def reading_file(path_file):
    file = pd.read_csv(path_file)
    print(file)
