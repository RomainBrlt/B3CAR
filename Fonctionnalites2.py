import random

def jeu_devine():
    nombre_secret = random.randint(1, 100)
    tentative = 0
    
    print("Bienvenue dans le jeu de devinette !")
    
    difficulte = input("Choisissez une difficulté (facile, moyen, difficile) : ").lower()
    if difficulte == "facile":
        max_tentatives = 15
    elif difficulte == "moyen":
        max_tentatives = 10
    else:
        max_tentatives = 5
    
    while tentative < max_tentatives:
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
    
    if tentative == max_tentatives:
        print(f"Dommage ! Vous avez dépassé {max_tentatives} tentatives. Le nombre était {nombre_secret}.")

jeu_devine()
