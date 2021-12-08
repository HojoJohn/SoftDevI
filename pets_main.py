import pets


def main():
    pet = pets.Pet("Buttercup","basket hound(canine)", 70,"Brown",4)
    print("name =", pet.__name, ", weight =", pet.__weight)

    print(pet)

    

main