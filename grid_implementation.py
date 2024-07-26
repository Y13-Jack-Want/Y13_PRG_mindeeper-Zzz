"""
name: Jack Want
Date: 24/06/024
Purpose: a planned gui for my minesweeper project
Version: 2
Additions: implement wieght ratios
"""

#imports
from tkinter import *

# initial window varibales
window_cfg = {
    "width": 1000,
    "height": 900,
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
        "board": (30,30),
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
left = Frame(root, bg='gray')
right = Frame(root, bg='pink')

#mainframe weight
root.grid_columnconfigure(0, weight=8)
root.grid_columnconfigure(1, weight=2)
root.grid_rowconfigure(0, weight=9)

#mainFrame layout
left.grid(row=0, column=0, sticky="nsew")
right.grid(row=0, column=1, sticky="nsew")

#left subframe setup
header = Frame(left, bg='#E6E6FA')
game = Frame(left, bg='#013220')

#left subframe weight
left.grid_columnconfigure(0, weight=8)
left.grid_rowconfigure(0, weight=1)
left.grid_rowconfigure(1, weight=8)

#bombframe
def grid_setup():
    global brd_size
    x_amnt = brd_size[0]
    print(x_amnt)
    y_amnt = brd_size[1]
    print(y_amnt)
    x = 0
    y = 0
    grid_dict= {}
    grid_keys= []
    for a in range(y_amnt):
        for i in range(x_amnt):
            temp = str(x)+","+str(y)
            grid_keys.append(temp)
            grid_dict[temp] = False
            x+=1
        x=0
        y+=1
    print(grid_dict)
    print(grid_keys)
    return(grid_dict,grid_keys)
grid_values = grid_setup()
grid_dict = grid_values[0]
grid_keys = grid_values[1]

#def make_button():


#def grid_button():

def temporaria():
    print(":3")


#90EE90 : colour for later :3

#left subframe layout
header.grid(row=0, column=0, sticky="nsew")
game.grid(row=1, column=0, sticky="nsew")

root.mainloop()
