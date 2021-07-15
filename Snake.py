import os
import random

import readchar

WIDTH = 20
HEIGHT = 15
POS_X = 0
POS_Y = 1
NUM_OF_MAP_OBJECTS = 11

my_position = [0, 0]
tail_length = 0
tail = []
map_objects = []

end_Game = False
is_Dead = False

while not end_Game:
    os.system("cls")

    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    # Drawing the map
    print(" " + "-"*(WIDTH*3) + " ")

    for coordinate_y in range(HEIGHT):
        print("|", end="")
        for coordinate_x in range(WIDTH):
            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    end_Game = True
                    is_Dead = True

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print(" " + "-"*(WIDTH*3) + " ")

    # Snake movement
    direction = readchar.readchar().decode()
    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= HEIGHT
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= WIDTH
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= HEIGHT
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= WIDTH
    elif direction == "q":
        exit()

if is_Dead:
    print("Has muerto")