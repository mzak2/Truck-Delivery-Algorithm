class InstantiateHashMap:
    #We initiate our list with a base list with a capacity of our chosen base amount
    #Looping through the list to create placeholders
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
