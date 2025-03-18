import serial

ser = serial.Serial('COM9', 115200, timeout=2)

a = True
while a == True:
    var = input("Escribe: ")
    if (var == "a"):
     
     ser.write(b'a')

    elif (var == "b"):
        ser.write(b'b')

    r = input("Deseas terminar?")
    if (r == "si"):
       ser.close()
       break
    elif (r != "si"):
       a == True

print("El programa ha finalizado")