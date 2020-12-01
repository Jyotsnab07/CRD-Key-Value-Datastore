import time
import json
import threading
from threading import*
import time
# Sample of data
my_json_string={
"Jyotsna":45,
"Prabha":100
}
# write into datastore json file
with open('data.json', 'w') as file:
    json.dump(my_json_string, file)
# store data in form of dictionary json_data
with open('data.json') as j:
    json_data = json.load(j)

# function to write data to datastore
def display():
    with open('data.json', 'w') as file:
        json.dump(json_data, file)

# read operation
def read(key):
    if key not in json_data:
        return("ERROR : Key does not exist in database")
    else:
        temp = json_data[key]
        if temp[1] != 0:
            if time.time() < temp[1]:
                final = str(key) + ":" + str(temp[0])
                return(final)
            else:
                return("ERROR : time-to-live for", key, "has expired")
        else:
            final = str(key) + ":" + str(temp[0])
            return(final)

# create operation
def create(key,value,timeout):

    if key in json_data:
        return("ERROR: Key already exists (Duplicate key not possible)")
    else:
        if (type(key) == str):
            if len(json_data) < (1024 * 1020 * 1024) and value <= (
                    16 * 1024 * 1024):  # constraints for file size less than 1GB and Jasonobject value less than 16KB
                if timeout == 0:
                    list = [value, timeout]
                else:
                    list = [value, time.time() + timeout]
                if len(key) <= 32:  # constraints for input key_name capped at 32chars
                    json_data[key] = list
                    display()

            else:
                return("ERROR: Memory limit exceeded ")
        else:
            return("ERROR : Key_name must be in string format")

# delete operation
def delete(key):
    if key not in json_data:
        return("ERROR: Key does not exist in database")
    else:
        temp = json_data[key]
        if temp[1] != 0:
            if time.time() < temp[1]:
                del json_data[key]
                display()

                return("Deletion of key successful")
            else:
                return("ERROR : time-to-live of", key, "has expired")
        else:
            del json_data[key]
            display()

            return("Deletion of key successful")

# modify operation
def modify(key,value):
    if key not in json_data:
        return ("ERROR : given key does not exist in database.")
    else:
        temp = json_data[key]
        if temp[1] != 0:
            if time.time() < temp[1]:
                    list = []
                    list.append(value)
                    list.append(temp[1])
                    json_data[key] = list
                    display()

            else:
                return ("ERROR : time-to-live of", key, "has expired")
        else:
            list = []
            list.append(value)
            list.append(temp[1])
            json_data[key] = list
            display()
