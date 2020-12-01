import time
import json
import source as x
import threading
from threading import Thread

print("This is a student marks data store containing student name and marks in the form of key-value pair[Student-pair]")
print("Example of format ")
with open('data.json') as j:
    json_data = json.load(j)
    print(json_data)
print("Please enter 'YES' to continue")
ch=input()
while(ch=="YES"):
    print("Enter R to perform read operation")
    print("Enter C to perform create operation")
    print("Enter D to perform delete operation")
    print("Enter M to perform modify operation")
    ch=input()
    if ch == 'R':
        print("enter student name")
        key = input()
        display=x.read(key)
        print(display)

        with open('data.json') as j:
            json_data = json.load(j)
            print(json_data)
        print("Enter 'YES' to continue and 'NO' to stop")
        ch = input()

    elif ch == "C":
        print("Enter student's name")
        key = input()
        print("Enter student's marks")
        value = int(input())
        print("enter timeout value")
        timeout=int(input())
        display=x.create(key,value,timeout)
        if(display!=None):
            print(display)

        with open('data.json') as j:
            json_data = json.load(j)
            print(json_data)
        print("Enter 'YES' to continue and 'NO' to stop")
        ch = input()

    elif ch=="D":
        print("enter the student name [ key]")
        key=input()
        display=x.delete(key)
        print(display)

        with open('data.json') as j:
            json_data = json.load(j)
            print(json_data)
        print("Enter 'YES' to continue and 'NO' to stop")
        ch = input()

    elif ch=='M':
        print("enter student name [ key]")
        key=input()
        print("enter student marks [value]")
        value=int(input())
        display=x.modify(key,value)
        if (display != None):
            print(display)
        with open('data.json') as j:
            json_data = json.load(j)
            print(json_data)
        print("Enter 'YES' to continue and 'NO' to stop")
        ch = input()

    else:
        print("INVALID INPUT")
        print("Enter 'YES' to continue and 'NO' to stop")
        ch = input()


# Multiple threads can be accessed like this
t1=threading.Thread(target=(x.create or x.read or x.delete),args=(key,value,timeout))
t1.start()
time.sleep(1)
t2=threading.Thread(target=(x.create or x.read or x.delete),args=(key,value,timeout))
t2.start()
time.sleep(1)
