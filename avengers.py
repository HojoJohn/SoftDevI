

class Superhero:
    __slots__ = [ 'name','identity','power','weapon']

    def __init__(self, name, identity, power, weapon):

        self.name = name
        self.identity = identity
        self.power = power
        self.weapon = weapon
    
    
    
    def thor():
        super1 = Superhero
        super1.name = "Thor"
        super1.identity = "Thor"
        super1.power = "Super Strength"
        super1.weapon = "Mojlnir"
        print('Found Avenger Bio:')
        print(super1.name,'(',super1.identity,')',':')
        print('Abilities:')
        print(super1.power)
        print('Weapon')
        print(super1.weapon)


    
    

def main():
    super1 = Superhero
    super1.name = "Thor"
    super1.identity = "Thor"
    super1.power = "Extreme Super Strength"
    super1.weapon = "Mojlnir"
    print('Found Avenger Bio:')
    print(super1.name,'(',super1.identity,')',':')
    print('Abilities:')
    print("\t",super1.power)
    print('Weapon: ')
    print("\t",super1.weapon)

    super2 = Superhero
    super2.name = "Hawkeye"
    super2.identity = "Clint Barton"
    super2.power = "Bow Mastery"
    super2.weapon = "Bow and Arrows"
    print('Found Avenger Bio:')
    print(super2.name,'(',super2.identity,')',':')
    print('Abilities:')
    print("\t",super2.power)
    print('Weapon: ')
    print("\t",super2.weapon)

    super3 = Superhero
    super3.name = "Captain America"
    super3.identity = "Steve Rogers"
    super3.power = "Super Soldier Serum"
    super3.weapon = "Shield"
    print('Found Avenger Bio:')
    print(super3.name,'(',super3.identity,')',':')
    print('Abilities:')
    print("\t",super3.power)
    print('Weapon: ')
    print("\t",super3.weapon)

    super4 = Superhero
    super4.name = "SpiderMan"
    super4.identity = "Peter Parker"
    super4.power = "Spider powers"
    super4.weapon = "Web Shooters"
    print('Found Avenger Bio:')
    print(super4.name,'(',super4.identity,')',':')
    print('Abilities:')
    print("\t",super4.power)
    print('Weapon: ')
    print("\t",super4.weapon)


    print('Roster: ')

    print("[Leader]",super3.name)
    print(super2.name)
    print(super1.name)
    print(super4.name)

main()
