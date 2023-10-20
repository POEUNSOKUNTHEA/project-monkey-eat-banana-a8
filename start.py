from ast import Delete
from asyncio import events
from cgitb import text
from ctypes.wintypes import tagSIZE
from email.mime import image
import tkinter as tk
from tkinter import Canvas, font
from typing import Counter 
import winsound
import os
import random
from PIL import Image,ImageTk
#  CONSTANTS
SCREEN_WIDTH = 1430
SCREEN_HEIGHT = 800

root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(root) 

# ________________Virable_________________
score=0
door=0
isfound=False
isWin=True
life=3

bgGrid = 0
FRUIT = 6
FAST_FOOD = 2
WALL = 4
BOOM = 9
DOOR = 7
MARIO = 1

#______________Images _________________________


mario_left=tk.PhotoImage(file=os.path.join('imags','monkey1.png'))
door_imag=tk.PhotoImage(file=os.path.join('imags','doors.png'))
wall_image=tk.PhotoImage(file=os.path.join('imags','walld.png'))
boom_image=tk.PhotoImage(file=os.path.join('imags','boom.png'))
Help=tk.PhotoImage(file=os.path.join('imags','Help.png'))
bg3=tk.PhotoImage(file=os.path.join('imags','bg-start.png'))
bg5=tk.PhotoImage(file=os.path.join('imags','Backgroud5.png'))
bgA=tk.PhotoImage(file=os.path.join('imags','buttonA.png'))
bg4=tk.PhotoImage(file=os.path.join('imags','bg-menu.png'))
# wall=tk.PhotoImage(file=os.path.join('imags','wall.png'))
BTN=tk.PhotoImage(file=os.path.join('imags','btn-removebg-preview.png'))

# hero=tk.PhotoImage(file=os.path.join('imags','monster.png'))
bg6=tk.PhotoImage(file=os.path.join('imags','bg2.png'))
bg8=tk.PhotoImage(file=os.path.join('imags','Bghelp.png'))
boom_imgae=tk.PhotoImage(file=os.path.join('imags','boom.png'))
apple=tk.PhotoImage(file=os.path.join('imags','apples.png'))
cherry=tk.PhotoImage(file=os.path.join('imags','cherry.png'))
orange=tk.PhotoImage(file=os.path.join('imags','oranges.png'))
carrot=tk.PhotoImage(file=os.path.join('imags','carrots.png'))

grape=tk.PhotoImage(file=os.path.join('imags','grapes.png'))
beer=tk.PhotoImage(file=os.path.join('imags','beer.png'))
pizza=tk.PhotoImage(file=os.path.join('imags','pizza.png'))
hot=tk.PhotoImage(file=os.path.join('imags','hot.png'))
Monkey=tk.PhotoImage(file=os.path.join('imags','monkey-mom.png'))
clock=tk.PhotoImage(file=os.path.join('imags','clock.png'))
heart=tk.PhotoImage(file=os.path.join('imags','heart.png'))
fruits=tk.PhotoImage(file=os.path.join('imags','monkey-mom.png'))
back=tk.PhotoImage(file=os.path.join('imags','back.png'))



fruit=[apple,cherry,orange,carrot,grape,]
food=[pizza,hot ,beer]

#_____________Grid for level 1___________________
def levelEasy(event):

    global grid, score, life, time 
    score=0
    life=3
    time = 50

    # grid = [[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    #         [4,0,6,0,4,6,4,0,6,0,4,6,4,0,6,0,4,6,4,9,6,6,9,0,4],
    #         [4,6,9,6,0,0,0,6,2,6,0,0,0,6,2,6,0,0,0,0,9,6,0,6,4],
    #         [4,0,6,0,4,6,4,0,6,0,4,6,4,0,6,0,4,6,4,0,6,0,9,0,4],
    #         [4,6,9,6,4,4,4,6,2,6,4,4,4,6,9,6,4,4,4,6,9,6,0,0,4],
    #         [4,0,6,0,4,6,4,0,6,0,4,6,4,0,6,0,4,6,4,0,6,9,0,0,7],
    #         [4,0,4,4,4,0,4,4,4,4,4,0,4,4,4,4,4,0,4,4,4,4,4,4,4],
    #         [4,0,6,0,4,0,4,0,6,0,4,0,4,0,6,0,4,0,4,0,6,0,4,6,4],
    #         [4,6,9,6,0,0,0,6,2,6,0,0,0,6,2,6,0,0,0,6,9,6,0,0,4],
    #         [4,0,6,0,4,0,4,0,6,0,4,0,4,0,6,0,4,0,4,0,6,0,4,0,4],
    #         [4,4,4,4,4,0,4,4,4,4,4,0,4,4,4,4,4,0,4,4,4,4,4,0,4],
    #         [4,0,9,0,4,6,4,0,6,0,4,6,4,0,6,0,4,6,4,0,6,0,6,0,4],
    #         [4,6,6,6,4,4,4,6,9,6,4,4,4,6,9,6,4,4,4,6,2,6,9,6,4],
    #         [4,0,9,0,0,6,0,0,9,0,0,6,0,0,9,0,0,6,0,0,6,0,9,0,4],
    #         [4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]]

    arrayToDrawing()
    settime()


#_____________Grid for level 2___________________
def levelMedium(event):

    global grid,score, life, time
    score=0
    life=3
    time = 50
    # grid = [[5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5],
    #         [5,5,5,5,5,5,5,5,5,5,5,4,0,9,0,0,6,0,4,0,2,2,0,0,4,5,5,5,5,5,5,5,5,5],
    #         [5,5,5,5,5,5,5,5,5,5,5,4,6,2,0,6,9,0,0,0,9,2,6,0,4,5,5,5,5,5,5,5,5,5],
    #         [5,5,5,5,5,5,5,5,5,5,5,4,0,0,9,0,6,0,4,0,2,2,0,0,4,4,4,4,4,4,4,4,4,4],
    #         [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,4,4,0,4,4,0,0,9,0,0,9,0,9,4],
    #         [4,0,0,9,0,4,0,9,0,4,0,9,0,4,0,9,0,4,9,0,0,4,0,2,4,4,0,0,6,9,0,0,0,4],
    #         [4,0,9,6,9,4,2,6,2,4,9,6,9,4,0,2,9,4,0,6,9,4,0,6,9,4,0,9,0,0,0,9,0,4],
    #         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,9,6,0,0,7],
    #         [4,0,9,6,9,4,9,6,9,4,9,6,9,4,0,6,9,4,0,6,9,4,0,6,9,4,9,0,6,0,0,9,0,4],
    #         [4,0,0,9,0,4,0,9,0,4,0,2,0,4,0,9,0,4,0,0,0,4,0,9,0,4,0,9,0,9,0,0,0,4],
    #         [4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,4,4,4,4,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    #         [5,5,5,5,5,5,5,5,5,5,5,4,0,6,0,6,0,0,4,0,0,0,0,6,0,4,5,5,5,5,5,5,5,5],
    #         [5,5,5,5,5,5,5,5,5,5,5,4,9,6,9,6,6,0,0,0,9,6,9,6,9,4,5,5,5,5,5,5,5,5],
    #         [5,5,5,5,5,5,5,5,5,5,5,4,0,9,0,9,0,9,4,0,0,9,0,0,0,4,5,5,5,5,5,5,5,5],
    #         [5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5]]

    arrayToDrawing()
    settime()

#_____________Grid for level 3___________________
def levelHard(event):

    global grid,score,life,time
    score=0
    life=3
    time = 50
    # grid = [[4,4,4,4,5,5,5,5,4,4,4,4,4,7,4,4,4,4,4,5,5,5,5,4,4,4,4],
    #         [4,6,2,6,4,5,5,4,9,6,0,6,9,0,9,6,0,6,9,4,5,5,4,6,2,6,4],
    #         [4,2,6,2,0,4,4,0,6,0,9,0,6,0,6,0,9,0,6,0,4,4,0,2,0,2,4],
    #         [5,4,0,0,6,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,4,4,6,0,6,4,5],
    #         [5,5,4,9,0,9,0,0,0,9,0,2,0,4,0,2,0,9,0,0,0,9,0,9,4,5,5],
    #         [5,5,5,4,6,0,0,2,9,6,9,0,0,4,0,0,9,6,9,0,2,0,6,4,5,5,5],
    #         [5,5,5,4,0,9,6,4,0,6,0,4,0,0,0,4,0,6,0,4,0,9,0,4,5,5,5],
    #         [5,5,5,4,6,4,0,6,0,9,0,2,0,4,0,2,0,9,0,0,0,4,6,4,5,5,5],
    #         [5,5,5,4,0,2,4,9,0,6,9,4,4,4,4,4,9,0,0,9,4,2,0,4,5,5,5],
    #         [5,5,5,4,6,9,6,4,0,0,0,0,0,1,0,4,0,0,0,4,6,9,6,4,5,5,5],
    #         [5,5,5,4,0,0,0,0,4,4,4,4,4,0,4,4,0,4,4,0,0,0,0,4,5,5,5],
    #         [5,5,5,5,4,6,9,2,6,0,0,4,6,0,6,4,0,0,6,2,9,6,4,5,5,5,5],
    #         [5,5,5,5,5,4,9,0,2,9,0,0,9,2,9,0,4,9,2,0,9,4,5,5,5,5,5],
    #         [5,5,5,5,5,5,4,6,9,4,6,0,9,2,9,0,6,4,9,6,4,5,5,5,5,5,5],
    #         [5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5],]
            
    arrayToDrawing()
    settime()

# __________________Show interface___________________
def interface():

    canvas.create_image(680,320,image=bg3)
    winsound.PlaySound("sound\\start.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

    canvas.create_image(1000,400,image=bgA)
   
    
    canvas.create_text(1000,315,text="GAME",font=('212BabyGirl', 25 ,'bold'),fill='gold',tags='start')

    canvas.create_text(1000,400,text="HELP",font=('212BabyGirl', 25 ,'bold'),fill='gold',tags='help')

    canvas.create_text(1000,485,text="EXIT",font=('212BabyGirl', 25 ,'bold'),fill='gold',tags='exit')

interface()
# __________________Show Help________________________
def helpGame(event):

    canvas.delete('all')

    canvas.create_image(600,320,image=bg8)

    canvas.create_image(100,50,image=back)
    canvas.create_text(100,50,text="Back", font='212BabyGirl 15 bold', fill='black', tags='back')

    canvas.create_image(650,320,image=Help)

canvas.tag_bind('help','<Button-1>',helpGame)

# ___________________settime_________________
time = 50
def settime():
    global time
    canvas.itemconfig(timer,text='Timer : ' + str(time)+ "s")

    if time <= 50:
        time -= 1

    if time <= 0:
        Lost()

    canvas.after(1500,settime)

# ___________________Close Windows__________________
def exitGame(event):

    canvas.quit()

canvas.tag_bind('exit','<Button-1>',exitGame)

# _____________________Show Level________________
def playGame(event):

    canvas.delete('all')
    clickLevel()

canvas.tag_bind('start','<Button-1>',playGame)


#_____________Back click______________
def backClick(event):
    canvas.delete('all')
    interface()
canvas.tag_bind('back','<Button-1>',backClick)

#_____________________Find Door_______________________________________________________________
def countDoor(theDoor):
    global door, score
    door = theDoor
    if door>=1 and score >= 20:
        winsound.PlaySound("sound\\win.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
        win()
    if door>=1 and score< 20:
        winsound.PlaySound("sound\\gameover.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
        Lost()

# ___________sum score____________
def countScore(newScore):
    global score
    score = newScore
    canvas.itemconfig(item,text=score)

#_________ minus life______________
def numberOfLife(mylife):
    global life
    life = mylife
    if life <= 0:
        winsound.PlaySound("sound\\gameover.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
        Lost()
    canvas.itemconfig(item1,text=life)
myfruit=random.choices(fruit)
fastfood=random.choices(food)

#_____________Funnnction for drawLevel______________
def arrayToDrawing():
    global grid,item,item1,score,life,timer
    canvas.delete('all')
    canvas.create_image(680,340,image=bg6)
    canvas.create_image(1050,300,image=Monkey)

    canvas.create_image(150,50,image=back)
    canvas.create_text(150,50,text="Back", font='212BabyGirl 15 bold', fill='black', tags='bac')

    canvas.create_image(300,50,image=fruits)
    canvas.create_text(400,50,text="Score : ",font='212BabyGirl 30 bold' ,fill="white")
    item=canvas.create_text(500,50,text=score,font='212BabyGirl 30 bold',fill='white')

    canvas.create_image(660,50,image=heart)
    canvas.create_text(750,50,text="Heart :",font='212BabyGirl 30 bold' ,fill="white")
    item1=canvas.create_text(850,50,text=life,font='212BabyGirl 30 bold' ,fill="white")

    canvas.create_image(990,50,image=clock)
    timer = canvas.create_text(1115,50,text='Timer : ' + str(time)+ "s",fill='white',font='212BabyGirl 30 bold')
    

    
    for ro in range(len(grid)):
        for co in range (len(grid[ro])):

            myfruit=random.choices(fruit)
            fastfood=random.choices(food)

            x1=100+(30*co)
            x2=130+(30*co)
            y1=150+(30*ro)
            y2=180+(30*ro)
            
            if grid[ro][co]== bgGrid:
                canvas.create_rectangle(x1,y1,x2,y2, fill="", outline='') 

            elif grid[ro][co]== FRUIT:
                canvas.create_image(x1,y1,image=myfruit, anchor="nw")

            elif grid[ro][co]== FAST_FOOD: 
                canvas.create_image(x1,y1,image=fastfood, anchor="nw")

            elif grid[ro][co]== WALL:               
                canvas.create_image(x1,y1,image=wall_image, anchor="nw")

            elif grid[ro][co]== BOOM:                
                canvas.create_image(x1,y1,image=boom_image, anchor="nw")
            elif grid[ro][co]== BOOM:                
                canvas.create_image(x1,y1,image=boom_image, anchor="nw")
                
            elif grid[ro][co]== DOOR:    
                canvas.create_image(x1,y1,image=door_imag, anchor="nw")

            elif grid[ro][co]== MARIO:               
                canvas.create_image(x1,y1,image=mario_left, anchor="nw")
                
        canvas.create_rectangle(x1,y1,x2,y2, outline='')

    return None


# __________Function for return row and col__________________
def positionNumOne(grid):  
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == MARIO:
                position=[r, c]
    return position
# ________________move left________________
def moveCharactor(direction):
    global door
    position=positionNumOne(grid)
    row = position[0]
    col = position[1]
    if direction == "left":
        if col != bgGrid:
            if grid[row][col-1] == FRUIT:
                countScore(score + 1)
                winsound.PlaySound("sound\\getCoin.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

            if grid[row][col-1] == FAST_FOOD:
                countScore(score - 1)
                winsound.PlaySound("sound\\eat.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)      

            if grid[row][col-1] == DOOR:
                countDoor(door + 1)

            if grid[row][col-1] == BOOM:
                numberOfLife(life - 1)
                winsound.PlaySound("sound\\bird.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

            if grid[row][col-1] != WALL:
                grid[row][col]=0
                grid[row][col-1] =1
#____________________________________________move Right______________________________________________
    if direction == "right" and "jump":
        if col != len(grid[0])-1:
            if grid[row][col+1] == FRUIT:
                countScore(score + 1)
                winsound.PlaySound("sound\\getCoin.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

            if grid[row][col+1] == FAST_FOOD:
                countScore(score - 1)
                winsound.PlaySound("sound\\eat.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)                

            if grid[row][col+1] == BOOM:
                numberOfLife(life - 1)
                winsound.PlaySound("sound\\bird.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

            
            if grid[row][col+1] == DOOR:
                countDoor(door + 1)

            print(door)
            if grid[row][col+1] !=WALL:
                grid[row][col]=0
                grid[row][col+1] =1

#________move Up_____________
    if direction == "up":
        if row != 0:
            if grid[row-1][col] == FRUIT:
                countScore(score + 1)
                winsound.PlaySound("sound\\getCoin.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

            if grid[row-1][col] == FAST_FOOD:
                countScore(score - 1)
                winsound.PlaySound("sound\\eat.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)                

            
            if grid[row-1][col] == DOOR:
                countDoor(door + 1)   

            if grid[row-1][col] == BOOM:
                numberOfLife(life - 1)
                winsound.PlaySound("sound\\bird.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

            
            if grid[row-1][col] != WALL:
                grid[row][col] = 0
                grid[row-1][col] = 1
                
# _______________move Down______________
    if direction == "down":
        if row != len(grid[0])-1:
            if grid[row+1][col] == FRUIT:
                countScore(score + 1)
                winsound.PlaySound("sound\\getCoin.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

            
            if grid[row+1][col] == FAST_FOOD:
                countScore(score - 1)
                winsound.PlaySound("sound\\eat.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)                

            
            if grid[row+1][col] == DOOR:
                countDoor(door + 1)

            if grid[row+1][col] == BOOM:
                numberOfLife(life - 1)
                winsound.PlaySound("sound\\bird.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

            
            if grid[row+1][col] != WALL:
                grid[row][col]=0
                grid[row+1][col] =1
                
    arrayToDrawing()

def moveLeft(event):
    moveCharactor("left")

def moveRight(event):
    moveCharactor("right")

def moveUp(event):
    moveCharactor("up")

def moveDown(event):
    moveCharactor("down")

def positionGhost(grid):  
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 10:
                positionOfGhost=[r, c]
    return positionOfGhost

def moveGhostLeft(event):
    indexOfGhost=positionGhost(grid)
    r=indexOfGhost[0]
    c=indexOfGhost[1]
    if c != 0:
        grid[r][c]=0
        grid[r][c-1]=10
    canvas.after(50,lambda: moveGhostLeft(event))
    arrayToDrawing()

def moveGhostRight(event):
    indexOfGhost=positionGhost(grid)
    r=indexOfGhost[0]
    c=indexOfGhost[1]
    if c != 0:
        grid[r][c]=0
        grid[r][c+1]=10
    canvas.after(50,lambda: moveGhostRight(event))
    arrayToDrawing()

#______________ back click_______________________________________________________________________________________________________
def bacClick(event):
    canvas.delete('all')
    clickLevel()
canvas.tag_bind('bac','<Button-1>',bacClick)

# ___________________Choose level___________________
def clickLevel():
    
    canvas.create_image(680,340,image=bg4)

    canvas.create_image(400,350,image=BTN)

    canvas.create_image(150,50,image=back)
    canvas.create_text(150,50,text="Back", font='212BabyGirl 15 bold', fill='black', tags='bak')

    canvas.create_text(400, 200, text="Easy",tags="level1", fill='gold', font=('212BabyGirl', 25 ,'bold'))
    canvas.tag_bind("level1","<Button-1>",levelEasy) 

    canvas.create_text(400, 320, text="Medium",tags="level2", fill='gold', font=('212BabyGirl', 25 ,'bold'))
    canvas.tag_bind("level2","<Button-1>",levelMedium) 

    canvas.create_text(400, 440, text="Hard",tags="level3", fill='gold', font=('212BabyGirl', 25 ,'bold'))
    canvas.tag_bind("level3","<Button-1>",levelHard)    

# _______________Back click________________
def bakClick(event):
    canvas.delete('all')
    interface()
canvas.tag_bind('bak','<Button-1>',bakClick)

#____________key control__________
root.bind("<Left>",moveLeft)
root.bind("<Right>",moveRight)
root.bind("<Up>",moveUp)
root.bind("<Down>",moveDown)

# ________________win______________
def win():

    canvas.delete(arrayToDrawing)
    canvas.create_rectangle(220,200,1000,500,fill='white')
    canvas.create_text(600,250,text="You Won!",font=('212BabyGirl', 50 ,'bold'), fill="black")

    canvas.create_image(300,350,image=fruits)
    canvas.create_text(400,350,text='score X ', font='212BabyGirl 25 bold',fill='black')
    canvas.create_text(480,350,text=score,font='212BabyGirl 30 bold',fill='red')

    canvas.create_image(700,350,image=heart)
    canvas.create_text(790,350,text='Heart X ', font='212BabyGirl 25 bold',fill='black')
    canvas.create_text(860,350,text=life,font='212BabyGirl 30 bold',fill='red')

    canvas.create_text(900,450,text='Menu',font='212BabyGirl 30',fill='black',tags='ne')
    win()

# _________lost_______________
def Lost():

    canvas.create_rectangle(220,200,1000,500,fill='white')

    canvas.create_text(600,250,text="You Lost!",font="212BabyGirl 60 bold", fill="black")

    canvas.create_image(300,350,image=fruits)
    canvas.create_text(400,350,text='score X ', font='212BabyGirl 25 bold',fill='black')
    canvas.create_text(480,350,text=score,font='212BabyGirl 30 bold',fill='red')

    canvas.create_image(700,350,image=heart)
    canvas.create_text(790,350,text='Heart X ', font='212BabyGirl 25 bold',fill='black')
    canvas.create_text(860,350,text='0',font='212BabyGirl 30 bold',fill='red')

    canvas.create_text(900,450,text='Menu',font='212BabyGirl 30',fill='black',tags='ne')

    Lost()

# _____________functionn for next level_____________
def nextLevel(event):
    canvas.delete('all')
    global score,life,grid,door,isfound,isWin,time
    score=0
    door=0
    isfound=False
    isWin=True
    time = 0
    life=3
    clickLevel()

# _______________click to restart and next_______________
canvas.tag_bind('ne','<Button-1>',nextLevel)

# _________________________________________________________________________________________________________

canvas.pack(expand=True, fill='both')
root.mainloop()