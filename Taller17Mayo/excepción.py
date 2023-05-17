#ZeroDivisionError
try:
    operacion= 8 / 0
except ZeroDivisionError:
    print("Error: División por cero.")
    
#valueError
while True:
    try:
        edad = int(input("Escribe tu edad: "))
        break
    except ValueError:
        print("¡Debes ingresar un número!")
    
#typeError
for i in range(3):
    try:
        list = [1,2,3,4,5]
        list2 = list[0.4]
        print(list2)
        break
    except TypeError:
        print("No se puede encotrar este tipo de objeto en la lista")
        

