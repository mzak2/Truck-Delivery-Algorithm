#Student: ADD FOR SUBMISSION
#Student ID: ADD FOR SUBMISSION
#Class: DSA2 C950

import csv
import datetime
import TruckClass

from InstantiateHashMap import InstantiateHashMap


#create our instance of the hash table
#then use our get_packages method to load our hash map from our csv file
packages_hash = InstantiateHashMap()
packages_hash.get_packages("csv/WGUPS_Package_csv.csv")

#placeholder for loop to test that our csv file data for packages is properly loaded
for pkg_id in range(1, 41):
     package = packages_hash.get(pkg_id)
     print(str(package))

