"""
name: Jack Want
Date: 24/06/024
Purpose: a planned gui for my minesweeper project
Version: 13
Additions: Final Version / added comments
"""

#imports
from tkinter import *
import random
import os
import sys

#declaring list that all class objects positions will be appended to
lliisstt = []
#sets up spawn protection
first_click = True

#class for each square on bomb grid
class Gridsqr:
    def __init__(self, pos, bomb):
        lliisstt.append(self)
        self.pos = pos
        self.bomb = bomb

    #setup the onclick effect of each square
    def button(self,is_bomb,xy):
        if is_bomb is True:
            #if bomb should explode
            self.pos = Button(game, bg='#90EE90', 
                              command = lambda: kablowey(self, xy)) 
            #iff bomb shouldn't explode
        else:
            self.pos = Button(game, text="", bg='#90EE90', 
                              command = lambda: safe(self, xy)) 

    #setup the weight values so that all grid squares are equal
    def weight(self, xy):
        x = xy.split(",")[0]
        y = xy.split(",")[1]
        xval = x.split("x")[1]
        yval = y.split("y")[1]
        game.grid_rowconfigure(yval, weight=1)
        game.grid_columnconfigure(xval, weight=1)

    #plot every square onto the grid
    def grid(self, xy):
        x = xy.split(",")[0]
        y = xy.split(",")[1]
        xval = x.split("x")[1]
        yval = y.split("y")[1]
        self.pos.grid(row=yval, column=xval, sticky='nsew')

    #change colour of gridsquare
    def colour(self, colour):
        self.pos.configure(bg=colour)
        
    #change number displayed on gridsquare
    def number(self, num):
        self.pos.configure(text=num)

    #disable the gridsquare so it can no longer be clicked
    def disable(self):
        self.pos.config(state=DISABLED)

    #make grid square safe to click
    def make_safe_pls(self, xy):
        self.pos.config(command = lambda: safe(self, xy))

    #make grid square explode on click
    def make_bomb_pls(self, xy):
        self.pos.config(command = lambda: safe(kablowey, xy))

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
    },
    "!!!IMPOSSIBLE!!!": {
        "board": (99,99),
        "mines": 1225
    },
    "Inverted": {
        "board": (10,10),
        "mines": 90
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
selecting = True
#print available difficulties
for difficult in difficulties:
    print("{}: {}x{}, {}mines".format(difficult, difficulties[difficult]["board"][0], difficulties[difficult]["board"][1], difficulties[difficult]["mines"]))
#select and validate difficulty
while selecting is True:
    difficulty = input("Difficulty: ")
    try:
        brd_values = difficulties[difficulty]
        selecting = False
    except:
        print("not a valid difficulty")

#establish variables
brd_size = brd_values["board"]
brd_mines = brd_values["mines"]
brd_width = brd_size[0]*square["width"]
brd_height = brd_size[1]*square["height"]

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

#setup the grid and everything inside 
def grid_setup():
    #set up the the board and position values for configuration
    global brd_size
    global brd_mines
    x_amnt = brd_size[0]
    y_amnt = brd_size[1]
    x = 0
    y = 0
    grid_keys= []
    
    #declare the bomblist
    bomb_list=[]
    #select random squares to be bombs according to the difficulty
    for z in range(brd_mines):
        validating = True
        while validating is True:
            selectedx = random.randint(0,x_amnt-1)
            selectedy = random.randint(0,y_amnt-1)
            to_be_appended = "x{},y{}".format(selectedx,selectedy)
            if to_be_appended not in bomb_list:
                validating = False
        bomb_list.append(to_be_appended)

    #make all of the squares in the grid
    safe_count = 0
    bomb_pos = []
    for a in range(y_amnt):
        for i in range(x_amnt):
            temp = "x"+str(x)+",y"+str(y)
            #setup for if the square is to be a bomb
            if temp in bomb_list:
                gridsqr_index = len(grid_keys)
                grid_keys.append(Gridsqr(temp,True))
                grid_keys[gridsqr_index].button(True, temp)
                grid_keys[gridsqr_index].weight(temp)
                grid_keys[gridsqr_index].grid(temp)
                bomb_pos.append(len(grid_keys))
                x+=1
            #setup for if the square is to be safe
            else:    
                gridsqr_index = len(grid_keys)
                grid_keys.append(Gridsqr(temp,False))
                grid_keys[gridsqr_index].button(False, temp)
                grid_keys[gridsqr_index].weight(temp)
                grid_keys[gridsqr_index].grid(temp)
                safe_count +=1
                x+=1
        x=0
        y+=1
    return(grid_keys,bomb_list,bomb_pos,safe_count)

#the function to be ran if a safe square is clicked
cleared = []
def safe(who, where):
    #set up the the board and position values for configuration
    global cleared_safe_squares
    global first_click
    x = str(where).split(",")[0]
    y = str(where).split(",")[1]
    xval = x.split("x")[1]
    yval = y.split("y")[1]
    
    first_click = False
    
    #calculate how many bombs the square touches
    bombs = 0
    x_check = -1
    y_check = -1
    for i in range(3):
        for i in range(3):
            check_x = int(xval)+x_check
            check_y = int(yval)+y_check
            check_pos = str("x"+str(check_x)+",y"+str(check_y))
            if check_x >= 0 and check_y >= 0:
                if check_pos in bomb_list:
                    bombs += 1
            x_check += 1
        x_check = -1
        y_check += 1

    #if the square hasn't been already cleared
    if who not in cleared:
        cleared.append(who)
        #put the number of bombs it touches on the square
        who.number(str(bombs))
        #mark the square white
        who.colour("white")
        #disable the button
        who.disable()
        #increment the value to see if the game has been won
        cleared_safe_squares +=1
        #if all squares cleared then display winscreen
        if cleared_safe_squares == safe_count:
            win_screen()
        #if the amount of bombs it touches is zero then run the zero code
        if bombs == 0:
            zero(who, where)
        return(1)
    else:
        return(3)

#the function to be ran if a bomb is clicked
def kablowey(who,where):
    #set up the the board and position values for configuration
    global brd_size
    global brd_mines
    global first_click
    x_amnt = brd_size[0]
    y_amnt = brd_size[1]
    #if first click is true then move where the bomb is and dont explode
    if first_click is True:
        bomb_list.remove(where)
        validating = True
        while validating is True:
            selectedx = random.randint(0,x_amnt-1)
            selectedy = random.randint(0,y_amnt-1)
            to_be_appended = "x{},y{}".format(selectedx,selectedy)
            if to_be_appended not in bomb_list:
                validating = False
        bomb_list.append(to_be_appended)
        
        lliisstt[bomb_pos][to_be_appended-1].make_bomb_pls(to_be_appended)
        who.make_safe_pls(where)
        first_click = False
    #if not first click explode all mines and run lose screen
    else:    
        for bomba in bomb_pos:
            lliisstt[bomba-1].colour("red")
        lose_screen()
    return(2)

#display the screen you will see upon winning
def win_screen():
    win = Toplevel(root)
    win.grab_set()
    win.geometry("300x100")
    win.title("Epic Victory")
    win_text = Label(win, text="YOU WON :D")
    restarted = Button(win, text="restart?", command=retry)
    win_text.place(relx=0.5, rely=0.5, anchor=CENTER)
    restarted.place(relx=0.5, rely=0.8, anchor = CENTER)
    disable_buttons()

#display the screen you will see upon losing
def lose_screen():
    lose = Toplevel(root)
    lose.grab_set()
    lose.geometry("300x100")
    lose.title("Skill Issue")
    lose_text = Label(lose, text="you died :p")
    restarded = Button(lose, text="retry?", command=retry)
    lose_text.place(relx=0.5, rely=0.5, anchor=CENTER)
    restarded.place(relx=0.5, rely=0.8, anchor = CENTER)
    disable_buttons()

#disables all buttons on the grid
def disable_buttons():
    for buton in lliisstt:
        buton.disable()

#funtion for clearing adjacent squares upon clicking a zero
def zero(who, where):
    #set up the the board and position values for configuration
    global brd_size
    x_amnt = brd_size[0]
    y_amnt = brd_size[1]
    x = str(where).split(",")[0]
    y = str(where).split(",")[1]
    xval = x.split("x")[1]
    yval = y.split("y")[1]
    
    #iterate through adjacent tiles
    x_check = -1
    y_check = -1
    for i in range(3):
        for i in range(3):
            check_x = (int(xval)+x_check)
            check_y = (int(yval)+y_check)
            if check_x >= 0 and check_y >= 0:
                if check_x < x_amnt and check_y < y_amnt:
                    numbertime = (check_y*x_amnt)+check_x
                    check_pos = str("x"+str(check_x)+",y"+str(check_y))
                    #run the safe command on each adjacent square
                    safe(lliisstt[numbertime],check_pos)
            x_check += 1
        x_check = -1
        y_check += 1

#restart the whole program
def retry():
    os.execv(sys.executable, ['python'] + sys.argv)

#left subframe layout
header.grid(row=0, column=0, sticky="nsew")
game.grid(row=1, column=0, sticky="nsew")

#run the setup loop and assign its returned values to variables
grid_values = grid_setup()
grid_keys = grid_values[0]
bomb_list = grid_values[1]
bomb_pos = grid_values[2]
safe_count = grid_values[3]
cleared_safe_squares = 0

#run the mainloop
root.mainloop()
