def fusion(a_list):
    sorted_list = sorted(a_list)
    copy = []

    mydict = dict()

    for i in range(len(sorted_list)):
        if sorted_list[i] + 1 == sorted_list[i +1]:
            copy.append(sorted_list[i])
        else:  

            mydict.update(copy)


    



def create_particles(max_coordinates):

    x = []
    y = []
    z = []
