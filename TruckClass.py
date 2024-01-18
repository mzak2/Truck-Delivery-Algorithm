class Truck:
    #create the Truck object with identifying information, as well as its current load
    def __init__(self, max_capacity, mph, load, packages, current_mileage, location, departure_time):
        self.max_capacity = max_capacity
        self.mph = mph
        self.load = load
        self.packages = packages
        self.current_mileage = current_mileage
        self.location = location
        self.departure_time = departure_time

    #return our truck information
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.max_capacity, self.mph, self.load, 
                                                                                    self.packages, self.current_mileage, 
                                                                                    self.location, self.departure_time)