#!/usr/bin/python3.9

from core.arduino.process import Arduino



def main():
    """Start connection with Arduino"""
    arduino = Arduino()
    arduino.read_lines



if __name__ == "__main__":
    main()