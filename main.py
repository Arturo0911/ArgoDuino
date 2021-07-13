# import serial


from typing import Union
from core.arduino.process import *
from core.model.growth import *
from core.fermentation.fermentation import Fermentation

def main():
    reading_file("data/table_1.csv")
    ferment = Fermentation(6.1, 0.00025,0.22226)

if __name__ == "__main__":
    print(main())



