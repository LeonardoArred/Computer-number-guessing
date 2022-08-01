import random


def adivina_el_numero (x): 
    '''X is superior limit and Y is the number computer has to guess'''

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to 'Guess the number'")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Think a number and computer will guess it")
    print(f"Choice a number between 1 and {x}")
    
    limite_inferior = 1
    limite_superior = x
    
    respuesta = ""

    while respuesta != "c":
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior) #Entre 1 y x 
        else:
            prediccion = limite_superior

        respuesta = input(f"Mi prediction is: {prediccion} , if prediction is higher input: 'A', if it is lower: 'B', but if it is the correct one: 'C': ").lower( )

        if respuesta == "a":
            limite_superior = prediccion -1  
        elif respuesta == "b":
            limite_inferior = prediccion +1
        
    print(f"The number {prediccion} has been guessed by the computer")

numero_alto = int(input("The lowest number is 1, input the highest number: "))

adivina_el_numero(numero_alto)