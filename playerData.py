from weaponData import Weapon


class Player:

    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        self.weapon = Weapon("", 0)
        self.inv = []
