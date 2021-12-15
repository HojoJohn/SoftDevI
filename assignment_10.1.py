import random

def fusion(a_list):
    sorted_list = sorted(a_list)
    copy = []

    mydict = dict()

    for i in range(len(sorted_list)):
        if sorted_list[i] + 1 == sorted_list[i +1]:
            copy.append(sorted_list[i])
        else:  

            mydict[copy] = len(copy)
            copy.clear


    



def create_particles(max_coordinates):

    sety = set()
    n = max_coordinates * 3

    for  i in range(0, n):
        x = random.randint(0, max_coordinates)
        y = random.randint(0, max_coordinates)
        z = random.randint(0, max_coordinates)
        coords = (x, y, z)

        sety.add(coords)
    
    return sety

def build_dict_xy(a_set):
    """
    a_set = [x,y]
    for i in range(0, len(a_set[i])):
        return tuple[x,y,z]"""

def main():
    a_list = [3,4,6,3,2,1,5]

    fusion(a_list)
    create_particles(100)

main

        
