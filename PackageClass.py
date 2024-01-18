class Package:
    #create the package object with identifying information, as well as its status
    # nlt = "No later than" 
    def __init__(self, package_id, address, city, state, zip_code, nlt, weight, delivery_status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.nlt = nlt
        self.weight = weight
        self.delivery_status = delivery_status
        self.depart_time = None
        self.arrival_time = None

    #return our package information
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                                                        self.zip_code, self.nlt, self.weight, self.delivery_status, 
                                                                                        self.arrival_time)
    
    #check and change the status of our package based on our time conversion
    #accounting for the current time versus the speed of our trucks
    def check_status(self, time_conversion):
        if self.arrival_time < time_conversion:
            self.status = "Delivered"
        elif self.depart_time > time_conversion:
            self.status = "Intransit"
        else: 
            self.status = "Processing"