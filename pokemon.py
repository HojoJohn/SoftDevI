class Pokemon:
    __slots__ = [ 'name','type','health_points','damage_points']
    def __init__(self, Name, Type=None,Health=None,Damage=None):
        self.name = Name
        self.type = Type
        self.health_points = Health
        self.damage_points = Damage
    def get_damage(self):
        return self.damage_points
    
    def lose_round(self,damage_points):
        self.damage_points = damage_points
        if self.health_points <= damage_points:
            print("Lose Round")
        else:
            print("Continue")
    def is_fainted(self):

        if self.health_points <= 0:
            return True
        else:
            return False
    def __str__(self):

        return "Pokemon Name=" + self.name + ", Type=" + self.type + ", Health=" + self.health_points + ", Damage" + self.damage_points
    def __repr__(self):
        return "Pokemon:\n" + \
            "\tName = " + self.name + "\n" + \
            "\tType = " + self.type + '\n' + \
            "\tHealth = " + self.health_points + "\n" \
            "\tDamage = " + self.damage_points + "\n"

