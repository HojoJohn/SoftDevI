CALORIES_PER_POUND = 30000
CALORIES_PER_MILE = 100

class Pet:
    __slots__ = ['__name', '__species', '__weight', '__fur_color', '__age']

    def __init__(self, name, species, weight, fur_color,age=0):

        self.__name = name
        self.__species = species
        self__weight = weight
        self.__age = age
        self.__fur_color = fur_color

    def feed(self,calories):
        self.__weight += calories/CALORIES_PER_POUND
        

    def walk(self,miles):

        self.__weight += miles*CALORIES_PER_MILE/CALORIES_PER_POUND

    def get_name(self):
        return self.__name
    def get_weight(self):
        return self.__weight