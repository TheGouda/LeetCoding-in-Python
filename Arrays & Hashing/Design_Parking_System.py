class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):

        list_of_cars = []
        self.list_of_cars = list_of_cars

        self.list_of_cars.append(big)
        self.list_of_cars.append(medium)
        self.list_of_cars.append(small)

    def addCar(self, carType: int) -> bool:

        if((carType == 1) and (self.list_of_cars[0] != 0)):
            self.list_of_cars[0] -= 1
            return True

        elif((carType == 2) and (self.list_of_cars[1] != 0)):
            self.list_of_cars[1] -= 1
            return True
        
        elif((carType == 3) and (self.list_of_cars[2] != 0)):
            self.list_of_cars[2] -= 1
            return True
        
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)