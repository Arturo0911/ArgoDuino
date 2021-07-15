# import serial

from core.model.growth import *


def main():
    # reading_file("data/table_1.csv")
    # ferment = Fermentation(6.1, 0.00025,0.22226)
    bacteria = BacteriaGrowth([], [], 0.10)
    lactose, strep = bacteria.show_concentration()
    print(lactose)
    print(strep)
    # bacteria.simulation_bacterial_growth()


if __name__ == "__main__":
    main()



