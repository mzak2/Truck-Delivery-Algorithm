#Student: ADD FOR SUBMISSION
#Student ID: ADD FOR SUBMISSION
#Class: DSA2 C950

import csv
import datetime
import TruckClass

from InstantiateHashMap import InstantiateHashMap
from PackageClass import Package
from Addresses import Addresses


#create our instance of the hash table
#then use our get_packages method to load our hash map from our csv file
packages_hash = InstantiateHashMap()
packages_hash.get_packages("csv/WGUPS_Package_csv.csv")

#placeholder for loop to test that our csv file data for packages is properly loaded
#used to put all 40 of our given packages into the hash map for preparation to load the trucks
for pkg_id in range(1, 41):
     package = packages_hash.get(pkg_id)
     print(str(package))

#Define the packages for each truck
packages_truck_1 = [1, 6, 13, 14, 15, 16, 19, 20, 25, 29, 30, 31, 34, 37, 40]
packages_truck_2 = [2, 3, 4, 5, 7, 9, 18, 21, 27, 28, 32, 33, 35, 36, 38, 39]
packages_truck_3 = [8, 10, 11, 12, 17, 22, 23, 24, 26]

#define all the other parameters for each truck
truck_1 = TruckClass.Truck(16, 18, None, [], 0.0, 
                                        "4001 South 700 East", datetime.timedelta(hours=8))

truck_2 = TruckClass.Truck(16, 18, None, [], 0.0, 
                                        "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

truck_3 = TruckClass.Truck(16, 18, None, [], 0.0, 
                                        "4001 South 700 East", datetime.timedelta(hours=8))

#load our trucks using our hash map and finding the corresponding package_ids
for pkg_id in packages_truck_1:
     package = packages_hash.get(pkg_id)
     truck_1.add_package(package)

for pkg_id in packages_truck_2:
     package = packages_hash.get(pkg_id)
     truck_2.add_package(package)

for pkg_id in packages_truck_3:
     package = packages_hash.get(pkg_id)
     truck_3.add_package(package)

#print all address for our packages as a test
print("------packages address---------")
for package in truck_1.packages:
     print(package.address)
     


#Call our Addresses class to find a specific address within the CSV
#Then return the value assigned to represent the address
# example: "Westerns Governors University" returns 0
print("-----------Address values--------")

address = "4580 S 2300 E" #should return the number "21"
address_csv = Addresses()
print(address_csv.get_address(address))




#Assign our test values for addresses and then return the intersection representing distance between
# uses the total_distance method in Addresses class
# example: "Westerns Governors University" = 0 and "Internation Peace Gardens" = 1
# should return a distance intersection of "7.2"
print("-----------Distance--------")

address_val_1 = 0
address_val_2 = 5
print(address_csv.total_distance(address_val_1, address_val_2))

#loops through all of our packages and gets their total distance from truck_1
#default location of truck_1 is at the hub
for i in range(len(truck_1.packages)):
     distance = address_csv.total_distance(address_csv.get_address(truck_1.location),
                                           address_csv.get_address(truck_1.packages[i].address))

     print(f"Our distance from the hub for Package id: {truck_1.packages[i].package_id} is {distance}" )

print("-----truck address and package address-------")
print(address_csv.get_address(truck_1.packages[0].address))
print(address_csv.get_address(truck_1.location))
print(address_csv.total_distance(address_csv.get_address(truck_1.location), (address_csv.get_address(truck_1.packages[0].address))))


def begin_route(truck):
     awaiting_delivery = []
     for pkg_id in truck.packages:
          package = packages_hash.get(pkg_id)
          awaiting_delivery.append(package)
     
     truck.packages.clear()

     while len(awaiting_delivery) > 0:
          nearest_address = 999
          nearest_pkg = None
          for package in awaiting_delivery:
               if address_csv.total_distance(address_csv.get_address(truck_1.location), 
                                             (address_csv.get_address(truck.packages[package]))) <= nearest_address:
                    nearest_address = address_csv.total_distance(address_csv.get_address(truck_1.location),
                                                                  (address_csv.get_address(truck.packages[package].address)))
                    nearest_pkg = package
          
          truck.packages.append(nearest_pkg.package_id)
          print("Next package ID is: " + nearest_pkg.package_id)

          awaiting_delivery.remove(nearest_pkg)

          truck.mileage += nearest_address
          print("Total mileage is: " + nearest_address)

          truck.location = nearest_pkg.address


          truck.time += datetime.timedelta(hours= nearest_address / 18)
          nearest_pkg.arrival_time = truck.time
          nearest_pkg.depart_time = truck.departure_time
          print(truck.time)

begin_route(truck_1)

begin_route(truck_2)

truck_3.departure_time = min(truck_1.time, truck_2.time)
begin_route(truck_3)