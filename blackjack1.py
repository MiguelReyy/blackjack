import random

deck1 = { 
    "A": 11, 
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5, 
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9, 
    "10": 10, 
    "j": 10, 
    "Q": 10, 
    "K": 10 
} 

carta_aleatoria1 = random.choice(list(deck1.keys()))

carta_aleatoria2 = random.choice(list(deck1.keys()))

carta_dealer3 = random.choice(list(deck1.keys()))

carta_dealer4 = random.choice(list(deck1.keys()))

sumacartasmias = deck1[carta_aleatoria1] + deck1[carta_aleatoria2]

sumacartasdiler = deck1[carta_dealer3] + deck1[carta_dealer4]

print(f"Tus cartas son: {carta_aleatoria1} y {carta_aleatoria2}")

print(f"Y tienen una puntuacion de: {sumacartasmias}")

print(f"Tus cartas son: {carta_dealer3} y {carta_dealer4}")

print(f"Y tienen una puntuacion de: {sumacartasdiler}")

if sumacartasmias < sumacartasdiler:

    print("has perdido gracias por jugar.")

elif sumacartasmias > sumacartasdiler:
    print("has ganado, enhorabuena")

else:
    print("empate,cada uno se lleva lo suyo")

