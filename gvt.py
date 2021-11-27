COMMON = 1
UNCOMMON = 2
RARE = 3
LEGENDARY = 4

RESET = "\u001b[0m"
WHITE = "\u001b[38;5;7m"
LIGHT_GREEN = "\u001b[38;5;10m"
BLUE = "\u001b[38;5;26m"
ORANGE = "\u001b[38;5;130m"
GREEN = "\u001b[38;5;28m"
RED = "\u001b[38;5;9m"
YELLOW = "\u001b[38;5;11m"

RARITY_STRINGS = {
    COMMON : WHITE + "C", 
    UNCOMMON : LIGHT_GREEN + "U", 
    RARE : BLUE + "R", 
    LEGENDARY : ORANGE + "L"}

class Card:
    __slots__ = [ '__name','__resource_cost','__rarity','__faction','__attack_power','__health']

    def __init__(self,name,resource_cost,rarity,faction,attack_power,health):

        self.__name = name
        self.__resource_cost = resource_cost
        self.__rarity = rarity
        self.__faction = faction
        self.__attack_power = attack_power
        self.__health = health

    def get_name(self):
        return self.__name

    def get_resource_cost(self):
        return self.__resource_cost
    def get_rarity(self):
        return self.__rarity
    def get_faction(self):
        return self.__faction
    def get_attack_power(self):
        return self.__attack_power
    def get_health(self):
        return self.__health

    def __repr__(self):
        
        output = self.__name\ + "\nRarity\"+


    def __str__(self):


