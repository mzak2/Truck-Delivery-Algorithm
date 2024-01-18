#Student: ADD FOR SUBMISSION
#Student ID: ADD FOR SUBMISSION
#Class: DSA2 C950

import csv
import datetime
import TruckClass

from InstantiateHashMap import InstantiateHashMap
from PackageClass import Package

#get our pakacge data from the csv file
with open("csv/WGUPS_Package_csv.csv") as pkgs_csv:
    packages_csv = csv.reader(pkgs_csv)
    packages_csv = list(packages_csv)

#define a function for calling later, that moves through the csv file
# grabbing each comma separated value, and placing them as a list item [0-6]
#add default status to each package as "Processing"
#Then create the object "pkg" for the parameters defined by Package class
#Finally use the "add" method within our hash map class to add it into itself
def get_packages(csvfile, packages_hash):
    with open(csvfile) as pkg_info:
        packages_data = csv.reader(pkg_info) 
        for package in packages_data:
                pkg_id = int(package[0])
                pkg_address = package[1]
                pkg_city = package[2]
                pkg_state = package[3]
                pkg_zip_code= package[4]
                pkg_nlt = package[5]
                pkg_weight = package[6]
                pkg_delivery_status = "Processing"

                pkg = Package(pkg_id, pkg_address, pkg_city, pkg_state, pkg_zip_code, 
                                        pkg_nlt, pkg_weight, pkg_delivery_status)
                
                packages_hash.add(pkg_id, pkg)

#create our instance of the hash table
#then use our get_packages method to load our hash map
packages_hash = InstantiateHashMap()
get_packages("csv/WGUPS_Package_csv.csv", packages_hash)

#placeholder for loop to test that our csv file data for packages is properly loaded
for pkg_id in range(1, 41):
     package = packages_hash.get(pkg_id)
     print(str(package))

