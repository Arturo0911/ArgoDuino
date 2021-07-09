
import serial


def connection() -> list:
    
    print("[*] Waiting for connection...")
    arduino = serial.Serial(port ="COM4", baudrate= int(9600), timeout=2)
    counter = 1
    stack_data = list()
    while counter < 20:

        read_line = arduino.readline()
        line_conversion = str(read_line.decode("ascii", errors = "replace"))
        stack_data.append(line_conversion)
        counter += 1
    return stack_data
    
def main():
    
    print(connection())


if __name__ == "__main__":
    main()