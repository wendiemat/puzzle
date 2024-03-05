# 29/04/2022
# 9-PIECE PUZZLE

from tkinter import *
import time
import random, turtle

# create the GUI

# random background colour
colours = ['lightblue', 'lightgrey', 'paleturquoise', 'lightskyblue', 'salmon', 'palegreen', 'lightpink', 'lightcoral', 'palegreen', 'orchid', 'violet']
colour = random.choice(colours)

r = Tk()
r.geometry ("1100x600+0+0")
r.title ("Its A Puzzle!!")
r.configure (background = colour)

t = Frame (r, bg = "black", pady = 2, width = 1100, height = 800, relief = RIDGE)
t.grid (row = 0, column = 0)
labelTitle = Label(t, font = ('ink free', 50, 'bold'), text = 'Puzzle Game', bd = 9, bg = "black", fg = colour, justify = CENTER)
labelTitle.grid (row = 0, column = 0)

tMain = Frame (r, bg = colour, bd = 9, width = 1100, height = 800, relief = RIDGE)
tMain.grid (row = 1, column = 0, padx = 20)

tLeft = Frame (tMain, bg = colour, bd = 9, width = 590, height = 590, pady = 2, relief = RIDGE)
tLeft.pack (side = LEFT)

tRight = Frame (tMain, bg = colour, bd = 9, width = 550, height = 400, padx = 10, pady = 2, relief = RIDGE)
tRight.pack (side = RIGHT)

tRight1 = Frame (tRight, bg = colour, bd = 9, width = 450, height = 150, padx = 10, pady = 2, relief = RIDGE)
tRight1.grid (row = 0, column = 0)

tRight2 = Frame (tRight, bg = colour, bd = 9, width = 230, height = 200, padx = 10, pady = 2, relief = RIDGE)
tRight2.grid (row = 1, column = 0)
              
tRight3 = Frame (tRight, bg = colour, bd = 9, width = 290, height = 200, padx = 10, pady = 2, relief = RIDGE)
tRight3.grid (row = 1, column = 1)

tRight4 = Frame (tRight, bg = colour, bd = 9, width = 450, height = 150, padx = 10, pady = 2, relief = RIDGE)
tRight4.grid (row = 2, column = 0)


# create functions
# calculate number of clicks
numOfClicks = 0
showClicks = StringVar()
showClicks.set('Clicks ' + '\n' + '0')

# clicks counter
def updateCounter():
    global numOfClicks, showClicks
    showClicks.set('Clicks ' + '\n' + str(numOfClicks))

# calculate time taken
timeElapsed = 0.0
showTime = StringVar()
showTime.set('Time ' + '\n' + '0.0')
    
# time elapsed
def updateTimer():
    global showTime, timeElapsed
    if numOfClicks >= 1:
        timeElapsed = time.time()
        timeElapsed = timeElapsed/3600
    showTime.set('Time ' + '\n' + str(timeElapsed) + 's')
    
gameState = StringVar()


def updateGamestate(gamestates):
    global gameState
    gameState.set(gamestates)
    
class Button_:
    def __init__(self, text_, x, y):
        self.enterValue = text_
        self.textEntered = StringVar()
        self.textEntered.set(text_)
        self.x = x
        self.y = y
        self.numButton = Button(tLeft, textvar = self.textEntered, font = ('ink free', 50), bd = 3, command = lambda i = self.x, j = self.y: checkEmptySpot(i,j))
        self.numButton.place(x = self.x*185, y = self.y*185, width = 200, height = 200)
    
def shuffler():
    global numOfClicks, numsButton, timeElapsed
    nums = []
    for x in range(9):
        x += 1
        if x == 9:
            nums.append('')
        else:
            nums.append(str(x))
            
    for y in range(len(numsButton)):
        for x in range(len (numsButton[y])):
            num = random.choice(nums)
            numsButton[y][x].textEntered.set(num)
            nums.remove(num)
    numOfClicks = 0
    timeElapsed = 0.0
    updateCounter()
    updateGamestate('')
    updateTimer()

# show on GUI
labelShowClicks = Label(tRight2, textvar = showClicks, font = ('ink free', 50)).place(x = 0, y = 10, width = 200, height = 160)
labelShowClicks = Label(tRight1, textvar = gameState, font = ('ink free', 50)).place(x = 0, y = 10, width = 410, height = 100)
labelTimeElapsed = Label(tRight3, textvar = showTime, font = ('ink free', 40)).place(x = 0, y = 10, width = 250, height = 160)
shuffleButton = Button(tRight4, text = 'Reset', font = ('ink free', 50), bd = 4, command = shuffler).place(x = 0, y = 10, width = 410, height = 100)

# the puzzle
numsButton = []
name = 0

for y in range(3):
    numsButton_ = []
    for x in range(3):
        name += 1
        if name == 9:
            name = ""
        numsButton_.append(Button_(str(name), x, y))
    numsButton.append(numsButton_)

shuffler() 
def checkEmptySpot(y, x):
    global numsButton, numOfClicks
    if not numsButton[x][y].textEntered.get() == "":
        for i in range(-1, 2):
            newX = x + i
            if not (newX < 0 or len(numsButton) - 1 < newX or i == 0):
                if numsButton[newX][y].textEntered.get() == "":
                    text = numsButton[x][y].textEntered.get()
                    numsButton[x][y].textEntered.set(numsButton[newX][y].textEntered.get())
                    numsButton[newX][y].textEntered.set(text)
                    checkWin()
                    break
                
        for j in range(-1, 2):
            newY = y + j
            if not (newY < 0 or len(numsButton) - 1 < newY or j == 0):
                if numsButton[x][newY].textEntered.get() == "":
                    text = numsButton[x][y].textEntered.get()
                    numsButton[x][y].textEntered.set(numsButton[x][newY].textEntered.get())
                    numsButton[x][newY].textEntered.set(text)
                    checkWin()
                    break
        numOfClicks += 1
        updateCounter()
        updateTimer()

# determine winner
def checkWin():
    lost = False
    for y in range(len(numsButton)):
        for x in range(len(numsButton[y])):
            if numsButton[y][x].enterValue != numsButton[x][y].textEntered.get():
                lost = True
            elif not lost:
                updateGamestate("WINNER!!!")
                updateTimer()

r.mainloop()