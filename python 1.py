import random

caratteri_possibili = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lunghezza_password = int(input("Inserisci la lunghezza per la password: "))

password_generata = ""

for i in range(lunghezza_password):
    carattere_scelto = random.choice(caratteri_possibili)
    password_generata += carattere_scelto

print("La password generata è:", password_generata)