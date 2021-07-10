# import serial


from typing import Union
from core.arduino.process import *
from core.model.growth import *


def main():
    reading_file("data/table_1.csv")


if __name__ == "__main__":
    print(main())
