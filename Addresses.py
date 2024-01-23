import csv
from math import dist


class Addresses:

    #open the designated csv file as read only ('r')
    #search through the rows until they find the matching string literal
    # return the farthest value to the left to represent the address
    def get_address(self, address):
        with open("csv/WGUPS_Addresses_csv.csv", 'r') as address_info:
            csv_reader = csv.reader(address_info)
            for row in csv_reader:
                if len(row) >= 3 and address in row[1]:
                    return int(row[0])
    
    #open our Distance csv file and find the intersection of two given addresses
    #utilizes the get_address method above to get our values
    # example: "Westerns Governors University" = 0 and "Internation Peace Gardens" = 1
    # should return a distance intersection of "7.2"
    def total_distance(self, address_1, address_2):
        with open("csv/WGUPS_Distance_csv.csv", 'r') as distance_info:
            csv_reader = csv.reader(distance_info)
            column_index = int(address_1)
            row_index = int(address_2)

            for i, row in enumerate(csv_reader):
                if i == row_index:
                    distance = row[column_index]
                    if distance == '':
                        distance = 0

                    return float(distance)
            
            return None