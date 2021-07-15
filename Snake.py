import os
import readchar

WIDTH = 20
HEIGHT = 15
POS_X = 0
POS_Y = 1

my_position = [0, 0]


while True:
    # Drawing the map
    print(" " + "-"*(WIDTH*3) + " ")

    for coordinate_y in range(HEIGHT):
        print("|", end="")
        for coordinate_x in range(WIDTH):
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")

    print(" " + "-"*(WIDTH*3) + " ")

    # Snake movement
    direction = readchar.readchar().decode()
    if direction == "w":
        my_position[POS_Y] -= 1
    elif direction == "a":
        my_position[POS_X] -= 1
    elif direction == "s":
        my_position[POS_Y] += 1
    elif direction == "d":
        my_position[POS_X] += 1
    elif direction == "q":
        exit()
    os.system("cls")