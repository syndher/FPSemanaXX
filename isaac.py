room_descriptions = [

    [ "A", "B", "C", "D", "E" ],
    [ "F", "G", "H", "I", "J" ],
    [ "K", "L", "M", "N", "O" ],
    [ "P", "Q", "R", "S", "T" ],
    [ "U", "V", "W", "X", "Y" ],
    ]
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
room_exits=[[(False, False, True, True), (False, True, True, True), (False, True, True, True), (False, True, True, True), (False, True, True, False)],
            [(True, False, True, True), (True, True, True, True), (True, True, True, True), (True, True, True, True), (True, True, True, False)],
            [(True, False, True, True), (True, True, True, True), (True, True, True, True), (True, True, True, True), (True, True, True, False)],
            [(True, False, True, True), (True, True, True, True), (True, True, True, True), (True, True, True, True), (True, True, True, False)],
            [(True, False, False, True), (True, True, False, True), (True, True, False, True), (True, True, False, True), (True, True, False, False)],
            ]
position = (2, 2)

x, y = position
description = room_descriptions[y][x]
print(position, ":", description)
while(True):
    command = input("What now?")

    if command == "north":
        if (room_exits[y][x][NORTH]):
            print("You move north...")
            y = y - 1
        else:
            print("you can't move north...")
    elif command == "south":
        if (room_exits[y][x][SOUTH]):
            print("You move south...")
            y = y + 1
        else:
            print("you can't move south...")
    elif command == "east":
        if (room_exits[y][x][EAST]):
            print("You move east...")
            x = x - 1
        else:
            print("you can't move east...")
    elif command == "west":
        if (room_exits[y][x][WEST]):
            print("You move west...")
            x = x + 1
        else:
            print("you can't move west...")
    elif command == "goodbye":
        break
    else:
        print("i don't understand " + command)
        

position = (x,y)
