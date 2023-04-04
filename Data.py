from playerData import Player
from opsData import ops
from weaponData import Weapon
from roomData import Room


#---PLAYER---

bart = Player("Bart",100, 15,50)
#armor_bart = ("Skateboard", 50)
#bart.armor = armor_bart


#---OPS---

homer = ops("Homer", 200)
weapon_homer = Weapon("Étranglement", 50)
homer.weapon = weapon_homer


nelson = ops("Nelson", 100)
weapon_nelson = Weapon("Humiliation", 25)
nelson.weapon = weapon_nelson


tahiti_bob = ops("Tahiti Bob", 150)
weapon_tahiti_bob = Weapon("Couteau de cuisine", 35)
tahiti_bob.weapon = weapon_tahiti_bob


skinner = ops("Skinner", 40)
weapon_skinner = Weapon("sa mère, Agnès Skinner qui lance son dentier!", 10)
skinner.weapon = weapon_skinner


#---BART WEAPONS---

lance_pierre = Weapon("Lance-pierre", 30)
fireworks = Weapon("Feux d'artifice", 50)
bartman = Weapon ("Costume de BartMan", 80)


#---CHEST SANTE---

beer = 60
krusty_burger = 50
bd = 80


#---CREATION DES ROOM---

R0 = Room("la Salle de classe", [], None)
R1 = Room("le Couloir de l'école", [], skinner)
R2 = Room("le Krusty Burger", [], None)
R3 = Room("le Bar chez Moe's", [], None)
R4 = Room("le Bureau du principal Skinner", [], None)
R5 = Room("l'Arrière-boutique de Kwik-E-Mart", [], nelson)
R6 = Room("le Parc", [], tahiti_bob)
R7 = Room("le Salon de la Maison Simpson", [], homer)
R8 = Room("la Boutique Kwik-E-Mart", [], None)
R9 = Room("la Chambre de Bart", [], None)
R10 = Room("la Boutique de BD", [], None)


#---AJOUT DES LIAISONS DES ROOM---

R0.add_linked_room([None, R1, None, None])
R1.add_linked_room([None, None, R4, R0])
R2.add_linked_room([None, None, R5, None])
R3.add_linked_room([None, R4, R6, None])
R4.add_linked_room([R1, R5, None, R3])
R5.add_linked_room([R2, None, R8, R4])
R6.add_linked_room([R3, R10, None, None])
R7.add_linked_room([None, None, R9, R10])
R8.add_linked_room([R5, None, None, None])
R9.add_linked_room([None, None, None, None])
R10.add_linked_room([None, R7, None, R6])

#---POSITION DE DEPART---

current_position = R0