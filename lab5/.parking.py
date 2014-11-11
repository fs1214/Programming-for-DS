
class Parking:
    def __init__(self, name):
        self.name = name
        self.maxlength= 6
        self.maxwidth = 3
        self.vehicles = []

    def allow(self, vehicle):
        return vehicle.length <= self.maxlength and vehicle.width <= self.maxwidth

    def park(self, vehicle):
        if self.allow(vehicle):
            self.vehicles.append(vehicle)
        else:
            raise Exception("Vehicle is not allowed")
    def __repr__(self):
        return "{}, has {} vehicles".format(self.name, len(self.vehicles))

class StreetParking(Parking):
    def __init__(self, name):
        Parking.__init__(self,name)
        self.maxwidth = 4

    def allow(self, vehicle):
        return vehicle.length <= self.maxlength \
                and vehicle.width <= self.maxwidth\
                and len(self.vehicles) == 0

class Vehicle:
    def __init__(self, name, height, width, length):
        self.name = name
        self.height = float(height)
        self.width = float(width)
        self.length = float(length)
    def __repr__(self):
        return "{} (h={} w={} l={})".format(self.name, self.height, self.width, self.length)

if __name__ == "__main__":
    vehicles = []
    vehicles.append(Vehicle("Tesla", 2.8, 3.4, 5.8))
    vehicles.append(Vehicle("MyBike", 1, 0.3, 2))
    vehicles.append(Vehicle("Truck", 5, 5, 10))
    parkings = []
    parkings.append(StreetParking("Street"))
    parkings.append(Parking("Normal parking"))
    #parkings.append(Garage("Garage", maxheight= 2.6))
    for v in vehicles:
        for p in parkings:
            try:
                p.park(v)
                print "Succesfully parked {} in {}".format(v,p)
                break
            except:
                print "Couldn't park {} in {}".format(v,p)

