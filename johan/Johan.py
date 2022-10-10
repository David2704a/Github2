import random
print("HOLA")
for i in range(3):
    print("soy Johan Andres Chate \n")
print("<----Juego adivinar numero ------->\n")
al=random.randint(1,100)
cont=0
while True:
    n=int(input("digitar numero\n"))
    cont +=1
    if n>al:
        print("digitar un numero menor\n")
    elif n<al:
        print("digitar uno mayor\n")
    else:
        print(f"has adivinado el numero era:\t {al}\n") 
        break
print(f"los intentos fueron:\n{cont}")
print("")