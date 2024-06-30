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
    "width": 460,
    "height": 350,
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
square_x = 16
square_y = 16
square = {
    "width": square_x, 
    "height": square_y, 
    "area": (square_x * square_y),
    "perimeter": ((2*square_x)+(2*square_y))
}

#root window creation
root = Tk()
root.title("Bomb wiper")
root.geometry('{}x{}+{}+{}'.format(window_cfg["width"],window_cfg["height"],window_cfg["x-shift"],window_cfg["y-shift"]))

#Frame time :3
left = Frame(root, bg='gray' width=square[0], height=square[1])
right = Frame(root, bg='pink' width=(square[0]*), height=, padx=)