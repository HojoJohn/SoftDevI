import csv, random

class Pokedex:
    __slots__ = [ 'pokemon_list']
    def __init__(self):
        self.pokemon_list = []
    def load(self,filename):
        csv_file = open(filename, 'r')

        for i in range(len(csv_file)):
            title = csv.reader(csv_file)

            self.pokemon_list.append(title)
        return title
    
    def create_parties(self):
        set1 = {}
        set2 = {}
        pokemon_list = self.pokemon_list

        for pokemon_list in range(6):
            set1.add(random.shuffle(pokemon_list))
            set2.add(random.shuffle(pokemon_list))
        
        return set1, set2


