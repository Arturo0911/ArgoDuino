# import serial
from app import app
"""from app.core.model.growth import *


def main():
    # reading_file("data/table_1.csv")
    # ferment = Fermentation(6.1, 0.00025,0.22226)
    bacteria = BacteriaGrowth([], [], 0.10)
    lactose, strep = bacteria.show_concentration()
    print(lactose)
    print(strep)
    # bacteria.simulation_bacterial_growth()
"""
def main():
    app.run(port = 5000, debug=True)

if __name__ == "__main__":
    main()



