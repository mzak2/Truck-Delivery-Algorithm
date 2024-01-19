#Student: ADD FOR SUBMISSION
#Student ID: ADD FOR SUBMISSION
#Class: DSA2 C950

import csv
import datetime
import TruckClass

from InstantiateHashMap import InstantiateHashMap
from Addresses import Addresses


#create our instance of the hash table
#then use our get_packages method to load our hash map from our csv file
packages_hash = InstantiateHashMap()
packages_hash.get_packages("csv/WGUPS_Package_csv.csv")

#placeholder for loop to test that our csv file data for packages is properly loaded
for pkg_id in range(1, 41):
     package = packages_hash.get(pkg_id)
     print(str(package))

#Call our Addresses class to find a specific address within the CSV
#Then return the value assigned to represent the address
# example: "Westerns Governors University" returns 0
print("-----------Address values--------")

address = "Sugar House Park" #should return the number "2"
address_csv = Addresses()
print(address_csv.get_address(address, "csv/WGUPS_Addresses_csv.csv"))


#Assign our test values for addresses and then return the intersection representing distance between
# uses the total_distance method in Addresses class
# example: "Westerns Governors University" = 0 and "Internation Peace Gardens" = 1
# should return a distance intersection of "7.2"
print("-----------Distance--------")

address_val_1 = 0
address_val_2 = 1
print(address_csv.total_distance(address_val_1, address_val_2, "csv/WGUPS_Distance_csv.csv"))
