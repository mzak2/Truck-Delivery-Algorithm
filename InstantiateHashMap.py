import csv
from PackageClass import Package

class InstantiateHashMap:
    #We initiate our list with a base list with a capacity of our chosen base amount
    #Looping through the list to create placeholders
    # Citing source: WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py 
    def __init__(self, base_capacity=64):
        self.list = []
        for i in range(base_capacity):
            self.list.append([])

    #Add an item into our list
    #designating the location for where an item will go based on a hash key
    #which takes the length of list as Modulo to determine the insertion location
    #The bucket is identified, and checked to see if a key value is matched
    def add(self, key, item):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        #here we update the key in the case that it is in the bucket already
        for pair in bucket_list:
            if pair[0] == key:
                pair[1] = item
                return True

        #if no key is found, then it will be added at the end of the bucket
        key_value_pair = [key, item]
        bucket_list.append(key_value_pair)
        return True
    
    #a simple loop to look for our key value pair "duo"
    #getting our data
    def get(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for duo in bucket_list:
            if key == duo[0]:
                return duo[1]
        return None
    
    #Delete an item from our hash table
    #looping through to find it and delete if found
    def delete(self, key):
        position_slot = hash(key) % len(self.list)
        location = self.list[position_slot]

        if key in location:
            location.remove(key)


    #define a function for calling later, that moves through the csv file
    # grabbing each comma separated value, and placing them as a list item [0-6]
    #add default status to each package as "Processing"
    #Then create the object "pkg" for the parameters defined by Package class
    #Finally use the "add" method within our hash map class to add it into itself
    def get_packages(self, csvfile):
        with open(csvfile) as pkg_info:
            packages_data = csv.reader(pkg_info) 
            for package in packages_data:
                pkg_id = int(package[0])
                pkg_address = package[1]
                pkg_city = package[2]
                pkg_state = package[3]
                pkg_zip_code = package[4]
                pkg_nlt = package[5]
                pkg_weight = package[6]
                pkg_delivery_status = "Processing"

                pkg = Package(pkg_id, pkg_address, pkg_city, pkg_state, pkg_zip_code, 
                              pkg_nlt, pkg_weight, pkg_delivery_status)
                
                self.add(pkg_id, pkg)