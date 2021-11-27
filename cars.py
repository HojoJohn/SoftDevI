MAX_FUEL = 15

class Car:

    __slots__ = [ '__VIN','__make','__model','__year','__mileage','__fuel' ]

    def __init__(self,VIN,make,model,year):

        self.__VIN = VIN
        self.__make = make
        self.__model = model
        self.__year = year

        self.__mileage = 0
        self.__fuel = 0


    def print_car(self):

        print("Car VIN: ", self.__VIN, "Make: ", self.__make,"Model: ", self.__model,
            "Year: ", self.__year, "Mileage: ", self.__mileage, "Fuel: ", self.__fuel, sep="")
    
    def filler_up(self, gallons):

        self.__fuel += gallons

        if self.__fuel > MAX_FUEL:

            self.__fuel
    
    def driver_up(self,miles):

        max_miles = self.__fuel = 
        
        if miles > max_miles:
            miles = max_miles
        
        self.__mileage += miles

        self.__fuel -= miles


            
        







        