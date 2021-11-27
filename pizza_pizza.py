
class Toppings:

    __slots__ = [ 'type','price']

    def __init__(self,type,price):

        self.type = type
        self.price = price
        
TOPPINGS = {'F' : Toppings ("Mozzarella", 1.0),
          'SC' : Toppings ("Shredded Cheese", 0.0),
          'C' : Toppings ("Cheddar", 0.5),
          'P' : Toppings ("Pepperoni", 1.5),
          'S' : Toppings ("Sausage", 1.5),
          'B' : Toppings ("Bacon", 1.0),
          'M' : Toppings ("Meatball", 2.0),
          'MS' : Toppings ("Mushrooms", 1.0),
          'BP' : Toppings ("Bell Peppers", 1.0),
          'J' : Toppings ("Jalapeno Peppers", 1.0),
          'PN' : Toppings ("Pineapple", 1.5),
          'N' : Toppings ("None", 0.0)}


F = Toppings()
F.type =  "Mozzarella"
F.price = 1.0

SC = Toppings()
SC.type =  "Shredded Cheese"
SC.price = 0.0

C = Toppings()
C.type =  "Cheddar"
C.price = 0.5

P = Toppings()
P.type =  "Pepperoni"
P.price = 1.5

S = Toppings()
S.type =  "Sausage"
S.price = 1.5

B = Toppings()
B.type =  "B"
B.price = 1.0

M = Toppings()
M.type =  "Meatball"
M.price = 2.0

MS = Toppings()
MS.type = "Mushroom"
MS.price = 1.0

BP = Toppings()
BP.type =  "Bell Peppers"
BP.price = 1.0

J = Toppings()
J.type =  "Jalapeno Pepper"
J.price = 1.00

PN = Toppings()
PN.type =  "Pineapple"
PN.price = 1.5

class Pizza:

    __slots__ = [ 'type','price']

    def __init__(self,type,price):

        self.type = type
        self.price = price

PIZZA = {'meats' : Pizza ("Meat", 5.0),
        'cheese' : Pizza ("Cheese", 5.0),
        'veggies' : Toppings ("Veggies", 1.0)

}
 

def main():

    print("Welcome to Pizza Factory, where all order include two pizzas!")
    print("For your first pizza ...")
    input("Choose one type of cheese(0 for options:")

    print("Cheese Options:")

    print("Fresh Mozzarella(f): $1.0", "Shredded Cheese(s): $0.0", "Cheddar(c): $0.5")


main