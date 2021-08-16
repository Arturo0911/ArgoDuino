import serial
import matplotlib.pyplot as plt
import time

#Creamos la conexion
'''
El /dev/ttyUSB0 se refiere al puerto en el que esta
conectado el Arduino, este es para linux ñaño, pero
si tenes la VM puedes probar cambiando esto por 'COMx'
donde x es el numero del puerto, el 9600 es el boudrate
ñañon
'''

# arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=0)
point = 0
fig, ax = plt.subplots()
plt.ion()

maxlen = 20
x = []
y = []

while True:
     #data = arduino.readline().decode().strip()
    time.sleep(0.2)
    if data:
        data = int(data)
        x.append(point)
        y.append(data)
        if len(x) > maxlen:
            x = x[1:]
            y = y[1:]
        plt.plot(x, y, color='r')
        point += 1
        plt.pause(0.05)

        ax.clear()
        plt.ylim([0, 1023])
        plt.show()



#Codigo Arduino
#Para Leer la entrada Analogica
#y enviarla al serial o USB

'''
int value = 0;
int inPin = A1;
void setup() {
 Serial.begin(9600);
 }
 void loop() {
 value = analogRead(inPin);
 Serial.println(value);
 delay(10);
 }
'''
