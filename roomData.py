import Data

class Room:

    def __init__(self, name, linked_room, ops):
        self.name = name
        self.linked_room = linked_room
        self.ops = ops

    def add_linked_room(self, rooms):
        for i in range(0, len(rooms), 1):
            self.linked_room.append(rooms[i])


    def next_room(self):
        while Data.current_position != Data.R9:

            if Data.current_position != Data.R0 :
                print("Homer est toujours derrière Bart ! Dans quelle direction souhaite-tu fuir ? \n")
                print("-----------------------\n")

            for i in range(0, len(self.linked_room), 1):

                if self.linked_room[i] != None and i == 0:
                    print("- Nord - pour rejoindre", self.linked_room[i].name, "\n")
                elif self.linked_room[i] != None and i == 1:
                    print("- Est - pour rejoindre", self.linked_room[i].name, "\n")
                elif self.linked_room[i] != None and i == 2:
                    print("- Sud - pour rejoindre", self.linked_room[i].name, "\n")
                elif self.linked_room[i] != None and i == 3:
                    print("- Ouest - pour rejoindre", self.linked_room[i].name, "\n")

            while True:

                print("-----------------------")
                rep = input("")
                print("-----------------------\n")

                while rep != "Nord" and rep != "nord" and rep != "Est" and rep != "est" and rep != "Sud" and rep != "sud" and rep != "Ouest" and rep != "ouest":
                    print("Une entrée inconnue a été saisie :/ \n\nRéessayez")
                    print("-----------------------")
                    rep = input("")
                    print("-----------------------")

                if self.linked_room[0] != None and (rep =="Nord" or rep == "nord"):
                    return self.linked_room[0]
                elif self.linked_room[1] != None and (rep =="Est" or rep == "est"):
                    return self.linked_room[1]
                elif self.linked_room[2] != None and (rep =="Sud" or rep == "sud"):
                    return self.linked_room[2]
                elif self.linked_room[3] != None and (rep =="Ouest" or rep == "ouest"):
                    return self.linked_room[3]
