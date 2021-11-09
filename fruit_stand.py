class Fruit:

    __slots__ = [ 'type','price', 'count']

    def __init__(self, type, price):


        self.type = type
        self.price = price
        self.count = 0

FRUITS = {'apple' : Fruit ("Apple", 1.35),
          'pear' : Fruit ("Pear", 2,00)}


Apple = Fruit()
Apple.type =  "apple"
Apple.price = 1.35

Pear = Fruit()
Pear.type = 'pear'
Pear.price = 2.00   


def add_to_basket(fruit,basket):
    fruit = fruit.lower()

    if fruit in FRUITS:
        basket += [FRUITS[fruit]]
    elif fruit == '':
        pass
    else:
        print("Sorry, we don't sell ",fruit, "'s", sep="")
    

def calculate_cost(basket):
    cost = 0
    for fruit in basket:
        cost += fruit.price
        fruit.count += 1
    return cost

def count_fruit(fruit, basket):
    count = 0
    for item in basket:
        if item == fruit:
            count += 1
    
    return count
def main():

    basket = []
    selection = None

    while selection != '':
        selection =input("Which fruit would you like")
        add_to_basket(selection.lower(), basket)
    
    cost = calculate_cost(basket)
    
    print("Thank you for purchasing:",FRUITS['apple'].count,"Apples","and",
                FRUITS['pear'].count,"Pears,")
    
    f_spec = "{0:2f}"
    print("That comes to $:",f_spec.format(cost))
    




main