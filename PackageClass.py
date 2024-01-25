class Package:
    #create the package object with identifying information, as well as its status
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, delivery_status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.delivery_status = delivery_status
        self.depart_time = None
        self.delivery_time = None

    #return our package information
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                                                        self.zip_code, self.deadline, self.weight, self.delivery_status, 
                                                                                        self.delivery_time)
    
    #check and change the status of our package based on our time conversion
    #accounting for the current time versus the speed of our trucks
    def check_status(self, time_conversion):
        if self.delivery_time < time_conversion:
            self.delivery_status = "Delivered"
        elif self.depart_time > time_conversion:
            self.delivery_status = "Enroute"
        else: 
            self.delivery_status = "At Hub"