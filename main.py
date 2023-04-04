import Data
import pygame

pygame.init()
pygame.mixer.init()


def sound_simpsons():

    sound1 = pygame.mixer.Sound("/Users/clementasensio/Desktop/Running Bart RPG Python/The-Simpsons-Theme.ogg")
    sound1.play(-1)


def Menu():

    print("\n      Bienvenue sur \n      RUNNING BART!\n\n          Menu \n\n       1- Jouer \n       2- Crédits \n       3- Quitter\n\n-----------------------")
    rep = input("")
    print("-----------------------")

    while rep != "1" and rep != "2" and rep != "3":
        print("Une entrée inconnue a été saisie :/ \n\nRéessayez")
        print("-----------------------")
        rep = input("")
        print("-----------------------")

    if rep == "1":
        start()

    elif rep == "2" :
        credit()

    elif rep == "3" :
        exit()


def credit():

    print("\n         Crédits \n       RUNNING BART \n\n  Membres de l'équipe : \n\n      Yassine HAMIL \n     Shaynna RAYMOND  \n     Clément ASENSIO \n     Williams WANDJI \n      Imène TOUDEFT")
    print("\n'Retour' pour revenir au menu\n")
    print("-----------------------")
    rep = input("")
    print("-----------------------")

    while rep != "Retour" and rep != "retour" :
        print("Une entrée inconnue a été saisie :/ \n\nRéessayez")
        print("-----------------------")
        rep = input("")
        print("-----------------------")

    if rep == "Retour" or rep == "retour" :
        Menu()


def exit():

    print("\nVoulez-vous vraiment quitter le jeu?\n\n - Oui -\n - Non -\n")
    print("-----------------------")
    rep = input("")
    print("-----------------------")

    while rep != "oui" and rep != "Oui" and rep != "non" and rep != "Non" :
        print("Une entrée inconnue a été saisie :/ \n\nRéessayez")
        print("-----------------------")
        rep = input("")
        print("-----------------------")

    if rep == "oui" or rep == "Oui":
        print("\nA bientôt sur RUNNING BART!")
        exit

    elif rep == "non" or rep == "Non":
        Menu()


def game_over() :
    print("Mince ! C'est le coup de trop, Bart est K.O. Vous n'avez pas réussi à atteindre sa chambre. \nÇa va certainement mal finir pour lui... \nGAME OVER")
    exit()


def show_invent():

    i = 1
    if len(Data.bart.inv) > 0:
        for item in Data.bart.inv:
            print(i, item.name, "\n")
            i += 1
        choice = int(input("Choisissez une arme à utiliser : \n"))
        while choice > len(Data.bart.inv):
            choice = int(input("Rentrez un choix ?"))

        choice -=1
        item = Data.bart.inv[choice]
        Data.bart.weapon = item


def fight(enemy):

    if enemy.health > 0:
        print(enemy.name, "te barre la route et compte régler ses comptes avec Bart\n")


    while Data.bart.health > 0 and enemy.health > 0:

        print("Que veux tu faire ? \n\n 1- ATTAQUER \n 2- SE DEFENDRE \n 3- CONSULTER L'INVENTAIRE\n")
        print("-----------------------")
        rep = input("")
        print("-----------------------\n")

        if rep == "1":

            if enemy.health > 0 :

                enemy.health -= Data.bart.weapon.damage + Data.bart.attack

                if Data.current_position != Data.R1:
                    print("\nBart utilise", Data.bart.weapon.name, "et inflige", (Data.bart.weapon.damage + Data.bart.attack), "de dégâts à", enemy.name)
                else :
                    print("\nBart exécute une patate de forain et inflige", Data.bart.attack, "de dégâts à", enemy.name)

                if enemy.health > 0:
                    print("\nIl reste", enemy.health, "PV à", enemy.name)

                else :
                    print("")
                    print(enemy.name, "est K.O!!\nBart remporte le combat\n")

            if Data.bart.health > 0 and enemy.health > 0:

                print("Oh Oh ! On dirait que", enemy.name, "est encore plus énervé. \nPrépares-toi à encaisser son attaque !\n")
                Data.bart.health -= enemy.weapon.damage
                print(enemy.name, "utilise", enemy.weapon.name, "et inflige", enemy.weapon.damage, "de dêgâts à Bart ! \nIl lui reste", Data.bart.health, "PV\n")

        elif rep == "2" :

            if Data.bart.armor.health > 0 and enemy.health > 0:

                print("\nBart se défend à l'aide de son skateboard\n")
                print("Se défendre avec un skateboard...plutôt ingénieux! \nMais il n'a pas l'air de pouvoir tenir très longtemps...", enemy.name, "est décontenancé. \nPrépares-toi à encaisser son attaque !\n")
                Data.bart.armor.health -= enemy.weapon.damage

                if Data.bart.armor.health > 0 :
                    print(enemy.name, "utilise", enemy.weapon.name, "et inflige", enemy.weapon.damage, "de dêgâts au", Data.bart.armor.name,"\nIl reste", Data.bart.armor.health, "PV au", Data.bart.armor.name, "\n" )
                else :
                    print("Oups ! Il semblerait que le skateboard a atteint sa limite...\nOn dirait que tu ne peux plus t'en servir pour te défendre","\n")


        elif rep == "3":
            show_invent()


def start():

    sound_simpsons()

    print("\nIl est midi et la sonnerie de la pause déjeuner vient de retentir. \nBart qui vient à peine de finir de recopier ses lignes de punition, s'empresse de quitter la salle de classe. \n\n- 'Pas si vite!!' lui crie sa professeure, Madame Edna Krabappel \n- 'J'espère que ça te servira de leçon ! Ton lance pierre a été confisqué par Mr.Skinner, sache que tu ne le reverra pas de si tôt! \n   "
          "J'ai aussi appellé ton père. Ça t'apprendra à vouloir lancer des cailloux sur tes camarades de classe!' \n\nBart apperçoit au loin le reflet du crâne luisant de calvitie d'Homer sur les casiers de l'école. \n\n- 'LA PROF EST UNE GROSSE ###### !!' s'exclame Bart en fuyant avec son skateboard\n- 'ESPECE DE PITIT SKJD/?2K/POJ\D#GUSJ !!!' hurle Homer en se lançant à sa poursuite\n"
          "\nCette fois, c'est la bêtise de trop. Bart risque de vraiment se faire tuer.\nAides-le à fuir Homer et rejoindre sa chambre où il sera en sécurité (ou pas...).\n")
    print("-----------------------\n")

    while True and Data.current_position != Data.R9:

        if Data.bart.health <= 0:
            game_over()
            break

        Data.current_position = Data.current_position.next_room()
        print("\nTe voilà dans", Data.current_position.name, "\n")

        if Data.current_position.ops is not None:
            fight(Data.current_position.ops)

        if Data.current_position == Data.R3 and Data.beer != 0:
            Data.bart.health += Data.beer
            print("Tu te faufiles derrière le comptoir quand Moe a le dos tourné et tu obtiens une bière\nBart récupère ", Data.beer, "PV en la buvant\n")
            print("Ses PV sont maintenant de ", Data.bart.health, "\n")
            Data.beer = 0

        elif Data.current_position == Data.R2 and Data.krusty_burger != 0:
            Data.bart.health += Data.krusty_burger
            print("Krusty le clown offre des échantillons de burger devant son restaurant\nBart en prend 1 et récupère", Data.krusty_burger, "PV en le mangeant\n")
            print("Ses PV sont maintenant de", Data.bart.health, "\n")
            Data.krusty_burger = 0

        elif Data.current_position == Data.R8:
            if Data.fireworks in Data.bart.inv:
                Data.bart.inv.remove(Data.fireworks)
                Data.bart.inv.append(Data.fireworks)
            else:
                Data.bart.inv.append(Data.fireworks)
                print("Apu reçoit la visite des inspecteurs d'hygiène et fait face à de gros problèmes.\nBart en profite pour voler des", Data.fireworks.name, "très dangereux ! \nTu peux les retrouver dans ton inventaire d'armes\n")

        elif Data.current_position == Data.R10 :
            if Data.current_position == Data.R10 and Data.bd != 0:
                Data.bart.health += Data.bd
                print("Ça tombe bien le nouveau tome de la bd préférée de Bart vient de sortir !\nIl récupère", Data.bd, "PV en le lisant\n")
                print("Ses PV sont maintenant de ", Data.bart.health)
                Data.bd = 0

            if Data.bartman in Data.bart.inv:
                Data.bart.inv.remove(Data.bartman)
                Data.bart.inv.append(Data.bartman)
            else:
                Data.bart.inv.append(Data.bartman)
                print("Tu t'introduis dans la pièce secrète et récupères le", Data.bartman.name,"\nTu peux le retrouver dans ton inventaire d'armes\n")

        elif Data.current_position == Data.R4:
            if Data.lance_pierre in Data.bart.inv:
                Data.bart.inv.remove(Data.lance_pierre)
                Data.bart.inv.append(Data.lance_pierre)
            else:
                Data.bart.inv.append(Data.lance_pierre)
                print("Tu réussis à ouvrir la porte du bureau grâce à la clée volée de Skinner. \nBart peut maintenant récupérer son", Data.lance_pierre.name, "confisqué.\n")

    if Data.current_position == Data.R7:
        print("Homer s'écroule au sol !")

    if Data.current_position == Data.R9:
        print("FELICITATION ! Tu as réussi à atteindre la chambre de Bart et à echapper à Homer !\n\n              FIN DU JEU")


Menu()