    #!/usr/bin/env python
"""
Create a terminal program that displays a list of rooms available for rent and the price of each room to the user. This information is available in a comma-separated text file.
`rooms.txt`
# code, name, price
1,Master Suite,500
2,Family Room,200
3,Single Room,100
4,Standard Room,100

`rooms.txt`
# code, name, price
1,Master Suite,500
2,Family Room,200
3,Single Room,100
4,Standard Room,50

The program asks the user for their name, the room number to be reserved,
and the number of days, and finally displays the estimated amount to be paid.

The program must save this choice in another file containing the reservations

`reservations.txt`
# customer, room, days
Bruno,3,12

If another user tries to reserve the same room, the program must display a
message informing them that it is already reserved.
"""
import os
import logging
import sys

log = logging.Logger("Alert")

busy = {}
try:
    for line in open("reservations.txt"):
        name,number_room,days = line.strip().split(",")
        busy[int(number_room)] = {
            "name": name,
            "days": days
        
        }
    
except FileNotFoundError:
    log.error("File not Found")
    sys.exit(1)


rooms = {}
try:
    for line in open("quartos.txt"):
        code,name,price = line.strip().split(",")
        rooms[int(code)] = {
            "name":name,
            "price": float(price), #TODO: Decimal
            "avaliable": False if int(code) in busy else True
        }
    
except FileNotFoundError:
    log.error("File not Found")
    sys.exit(1)


print("Hotel Phytonico")
print("-" * 40)
print("Rooms available")
for code, datas in rooms.items():
    name_room = datas['name']
    price = datas['price']
    avaliable = "❌" if not datas['avaliable'] else "🟩"
    print(f"{code} - {name_room} - ${price:.2f} - {avaliable}")

name = input("What is your name? ")
try:
    number_room = int(input("What is the room number? "))
    if not rooms[number_room]['avaliable']:
        print(f"The room {number_room} not is avaliable ")
        sys.exit(1)
except ValueError as e:
    log.error("Number Invalid", str(e))
    sys.exit(1)
except KeyError:
    log.error("the room {number_room} does not exist ")
    sys.exit(1)
    
try:
    days = int(input("What is number of days? "))
except ValueError:
    print("Number invalid")
    sys.exit(1)
       
amount_payable = rooms[number_room]['price'] * days
print(f"The total amount is ${amount_payable}")

#Creating the file where customer information saved

path = os.curdir
filepath = os.path.join(path,"reservations.txt")
with open(filepath,"a") as file_:
    file_.write(f"{name},{number_room},{days}\n")

