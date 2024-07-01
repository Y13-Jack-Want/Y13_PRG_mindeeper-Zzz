"""
name: Jack Want
Date: 24/06/024
Purpose: a planned gui for my minesweeper project
Version: 1
"""

#imports
from tkinter import *

# initial window varibales
window_cfg = {
    "width": 1200,
    "height": 950,
    "x-shift": 0,
    "y-shift": 0
}

#mine settings config
difficulties = {
    "easy": {    
        "board": (8,8),
        "mines": 10
    },
    "medium": {
        "board": (16,16),
        "mines": 40
    },
    "hard": {
        "board": (30,16),
        "mines": 99
    }
}

#grid square config
square_x = 30
square_y = 30
square = {
    "width": square_x, 
    "height": square_y, 
    "area": (square_x * square_y),
    "perimeter": ((2*square_x)+(2*square_y))
}

#difficulty select
difficulty = input("Difficulty: ")
brd_values = difficulties[difficulty]
print(brd_values)
brd_size = brd_values["board"]
print(brd_size)
brd_mines = brd_values["mines"]
print(brd_mines)
brd_width = brd_size[0]*square["width"]
print(brd_width)
brd_height = brd_size[1]*square["height"]
print(brd_height)

#root window creation
root = Tk()
root.title("Bomb wiper")
root.geometry('{}x{}+{}+{}'.format(window_cfg["width"],window_cfg["height"],window_cfg["x-shift"],window_cfg["y-shift"]))

#mainFrame time :3
left = Frame(root, bg='gray', width=600, height=650)
right = Frame(root, bg='pink', width=300, height=650)

#mainFrame layout
left.grid(row=0, column=0, sticky="nsew")
right.grid(row=0, column=1, sticky="nsew")

#left subframe setup
header = Frame(left, bg='#E6E6FA', width=600, height=50)
game = Frame(left, bg='#013220', width=30*square["width"], height=30*square["height"])

#90EE90

#left subframe layout
header.grid(row=0, column=0, sticky="ew")
game.grid(row=1, column=0, sticky="nsew")

root.mainloop()