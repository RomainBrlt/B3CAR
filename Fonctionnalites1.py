import random

def jeu_devine():
    nombre_secret = random.randint(1, 100)
    tentative = 0
    
    print("Bienvenue dans le jeu de devinette !")
    
    while True:
        try:
            guess = int(input("Devinez un nombre entre 1 et 100 : "))
            tentative += 1
            
            if guess < nombre_secret:
                print("Trop bas ! Essayez encore.")
            elif guess > nombre_secret:
                print("Trop haut ! Essayez encore.")
            else:
                print(f"Bravo ! Vous avez trouvé en {tentative} tentatives.")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

jeu_devine()
