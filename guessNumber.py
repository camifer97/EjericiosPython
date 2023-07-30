import random

n = random.randrange(1,100)
number = int(input("Ingrese un numero del 1 al 100: "))

while n!=number:
    if n < number:
        print("El numero ingresado es demasiado grande.")
        number = int(input("Intentalo nuevamente: "))
    elif n > number:
        print("El numero ingresado es demasiado pequeño.")
        number = int(input("Intentalo nuevamente: "))
    else:
        break
print("Felicitaciones! Has ganado el juego.")

