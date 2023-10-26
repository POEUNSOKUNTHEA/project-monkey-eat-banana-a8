import tkinter as tk
import winsound
import os
import random

#  CONSTANTS
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(root) 

# ________________Virable_________________
score=0
win=0
isfound=False
isWin=True
life=3

bgGrid = 0
FRUIT = 6
FAST_FOOD = 2
WALL = 4
FIRE = 9
WINS = 7
MARIO = 1

#______________Images _________________________


hero_mk=tk.PhotoImage(file=os.path.join('imags','monkey.png'))
wall_image=tk.PhotoImage(file=os.path.join('imags','walld1.png'))
snack_image=tk.PhotoImage(file=os.path.join('imags','enemy.png'))
thorns_image=tk.PhotoImage(file=os.path.join('imags','thorns.png'))
BN_imag=tk.PhotoImage(file=os.path.join('imags','banana6.png'))
rock_imag=tk.PhotoImage(file=os.path.join('imags','rock.png'))
win_imag=tk.PhotoImage(file=os.path.join('imags','win.png'))
win_flag=tk.PhotoImage(file=os.path.join('imags','win_flag.png'))
enemy_image=tk.PhotoImage(file=os.path.join('imags','enemy.png'))



Help=tk.PhotoImage(file=os.path.join('imags','Help.png'))
bg3=tk.PhotoImage(file=os.path.join('imags','bg-start.png'))
bg5=tk.PhotoImage(file=os.path.join('imags','bg2.png'))
bgA=tk.PhotoImage(file=os.path.join('imags','buttonA.png'))
bg4=tk.PhotoImage(file=os.path.join('imags','bg-menu.png'))
# __________________bg-top_________________
bgtop1=tk.PhotoImage(file=os.path.join('imags','bg-top.png'))
bgtop2=tk.PhotoImage(file=os.path.join('imags','bg-top.png'))
bgtop3=tk.PhotoImage(file=os.path.join('imags','bg-top.png'))

BTN=tk.PhotoImage(file=os.path.join('imags','btn-removebg-preview.png'))
bg_welcome=tk.PhotoImage(file=os.path.join('imags','bg-welcome2.png'))
bg_welcome1=tk.PhotoImage(file=os.path.join('imags','welcome.png'))

story=tk.PhotoImage(file=os.path.join('imags','story.png'))
small_MK=tk.PhotoImage(file=os.path.join('imags','monkey1.png'))
WIN=tk.PhotoImage(file=os.path.join('imags','win.png'))
bg_story=tk.PhotoImage(file=os.path.join('imags','write-story.png'))
bg6=tk.PhotoImage(file=os.path.join('imags','bg6.png'))
bg8=tk.PhotoImage(file=os.path.join('imags','bg4.png'))
MK=tk.PhotoImage(file=os.path.join('imags','monkey-big.png'))

Child_MK=tk.PhotoImage(file=os.path.join('imags','MK_story.png'))
fire_image=tk.PhotoImage(file=os.path.join('imags','fire.png'))
booms=tk.PhotoImage(file=os.path.join('imags','boom.png'))
banana1=tk.PhotoImage(file=os.path.join('imags','banana5.png'))
banana2=tk.PhotoImage(file=os.path.join('imags','banana6.png'))
banana3=tk.PhotoImage(file=os.path.join('imags','banana3.png'))
banana4=tk.PhotoImage(file=os.path.join('imags','banana4.png'))

banana5=tk.PhotoImage(file=os.path.join('imags','banana5.png'))
banana6=tk.PhotoImage(file=os.path.join('imags','banana6.png'))
boom1=tk.PhotoImage(file=os.path.join('imags','boom1.png'))
boom3=tk.PhotoImage(file=os.path.join('imags','boom3.png'))
boom4=tk.PhotoImage(file=os.path.join('imags','boom4.png'))
Monkey=tk.PhotoImage(file=os.path.join('imags','monkey-mom.png'))
clock=tk.PhotoImage(file=os.path.join('imags','clock.png'))
heart=tk.PhotoImage(file=os.path.join('imags','heart.png'))
Score_MK=tk.PhotoImage(file=os.path.join('imags','monkey-mom.png'))
back=tk.PhotoImage(file=os.path.join('imags','back.png'))



fruit=[banana1,banana2,banana3,banana4,banana5,]
fruits=[booms,boom1,boom3,boom4]


#_____________Grid for level 1___________________
def level1(event):

    global grid, score, life, time 
    score=0
    life=3
    time = 50

    grid = [[0,0,0,0,0,0,4,4,4,4,4,0,0,0,0,4,4,4,4,4,0,0,0,0,4,4,4,4,4,0,0,0,0,0],
            [0,4,4,4,4,4,4,6,9,6,4,4,4,4,4,4,0,0,6,4,4,4,4,4,4,0,6,6,4,4,4,4,4,4],
            [0,4,0,6,0,6,0,6,0,0,6,0,6,0,0,6,0,2,0,0,6,0,6,0,0,6,9,0,0,6,0,6,9,4],
            [4,4,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,6,4,4],
            [4,0,0,6,0,6,0,2,6,6,0,0,6,0,6,0,2,0,6,0,6,6,0,6,0,0,2,0,0,6,0,6,0,4],
            [4,9,2,0,4,4,6,0,0,4,4,4,4,4,4,0,6,0,9,4,4,4,4,4,4,6,0,0,4,4,0,9,0,4],
            [4,0,0,6,4,4,4,4,4,4,6,0,0,0,4,4,4,4,4,4,0,6,2,0,4,4,4,4,4,4,6,0,6,4],
            [4,4,6,0,4,6,0,0,6,0,0,9,6,0,6,0,0,6,0,0,6,0,0,0,6,0,0,0,0,4,0,0,4,4],
            [0,4,0,9,4,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,4,9,6,4,0],
            [4,4,6,0,4,0,4,9,0,6,0,2,0,9,0,0,4,0,6,0,9,4,0,2,0,0,9,4,0,4,6,0,4,4],
            [4,6,0,6,4,6,0,0,0,9,0,6,0,0,6,0,0,2,0,6,0,6,6,0,0,7,0,9,0,4,0,0,6,4],
            [4,0,9,0,4,0,4,6,0,6,0,4,0,6,0,6,0,0,0,9,0,4,0,0,9,0,9,4,0,4,6,2,0,4],
            [4,6,0,2,4,6,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,6,6,4],
            [4,4,0,0,4,0,6,0,9,0,6,0,4,4,9,0,2,6,0,6,0,6,0,2,0,0,6,0,4,4,6,9,0,4],
            [0,4,1,6,4,4,4,0,6,0,0,2,0,0,6,0,0,0,6,9,0,4,4,0,6,9,0,6,0,6,0,0,4,4],
            [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]]
           

 

    arrayToDrawing()
    settime()


#_____________Grid for level 2___________________
def level2(event):

    global grid,score, life, time
    score=0
    life=3
    time = 50
   
    grid = [[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
            [4,0,0,0,4,6,4,0,6,0,4,6,4,0,6,0,4,6,4,0,6,6,9,0,4],
            [4,6,9,6,0,0,0,6,2,6,0,0,0,6,2,6,0,0,0,0,9,6,0,6,4],
            [4,0,6,0,4,6,4,0,6,0,4,6,4,0,6,0,4,6,4,0,6,0,9,0,4],
            [4,6,9,6,4,4,4,6,2,6,4,4,4,6,9,6,4,4,4,6,9,6,0,0,4],
            [4,0,6,0,4,6,4,0,6,0,4,6,4,0,6,0,4,6,4,0,6,9,0,0,7],
            [4,0,4,4,4,0,4,4,4,4,4,0,4,4,4,4,4,0,4,4,4,4,4,4,4],
            [4,0,6,0,4,0,4,0,6,0,4,0,4,0,6,0,4,0,4,0,6,0,4,6,4],
            [4,6,9,6,0,0,0,6,2,6,0,0,0,6,2,6,0,0,0,6,9,6,0,0,4],
            [4,0,6,0,4,0,4,0,6,0,4,0,4,0,6,0,4,0,4,0,6,0,4,0,4],
            [4,4,4,4,4,0,4,4,4,4,4,0,4,4,4,4,4,0,4,4,4,4,4,0,4],
            [4,0,9,0,4,6,4,0,6,0,4,6,4,0,6,0,4,6,4,0,6,0,6,0,4],
            [4,6,6,6,4,4,4,6,9,6,4,4,4,6,9,6,4,4,4,6,2,6,9,6,4],
            [4,0,9,0,0,6,0,0,9,0,0,6,0,0,9,0,0,6,0,0,6,0,9,0,4],
            [4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]]

    arrayToDrawing()
    settime()

#_____________Grid for level 3___________________
def level3(event):

    global grid,score,life,time
    score=0
    life=3
    time = 50
    grid = [[4,4,4,4,5,5,5,5,4,4,4,4,4,7,4,4,4,4,4,5,5,5,5,4,4,4,4],
            [4,6,2,6,4,5,5,4,9,6,0,6,9,0,9,6,0,6,9,4,5,5,4,6,2,6,4],
            [4,2,6,2,0,4,4,0,6,0,9,0,6,0,6,0,9,0,6,0,4,4,0,2,0,2,4],
            [5,4,0,0,6,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,4,4,6,0,6,4,5],
            [5,5,4,9,0,9,0,0,0,9,0,2,0,4,0,2,0,9,0,0,0,9,0,9,4,5,5],
            [5,5,5,4,6,0,0,2,9,6,9,0,0,4,0,0,9,6,9,0,2,0,6,4,5,5,5],
            [5,5,5,4,0,9,6,4,0,6,0,4,0,0,0,4,0,6,0,4,0,9,0,4,5,5,5],
            [5,5,5,4,6,4,0,6,0,9,0,2,0,4,0,2,0,9,0,0,0,4,6,4,5,5,5],
            [5,5,5,4,0,2,4,9,0,6,9,4,4,4,4,4,9,0,0,9,4,2,0,4,5,5,5],
            [5,5,5,4,6,9,6,4,0,0,0,0,0,1,0,4,0,0,0,4,6,9,6,4,5,5,5],
            [5,5,5,4,0,0,0,0,4,4,4,4,4,0,4,4,0,4,4,0,0,0,0,4,5,5,5],
            [5,5,5,5,4,6,9,2,6,0,0,4,6,0,6,4,0,0,6,2,9,6,4,5,5,5,5],
            [5,5,5,5,5,4,9,0,2,9,0,0,9,2,9,0,4,9,2,0,9,4,5,5,5,5,5],
            [5,5,5,5,5,5,4,6,9,4,6,0,9,2,9,0,6,4,9,6,4,5,5,5,5,5,5],
            [5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5],]
            
    arrayToDrawing()
    settime()



# __________________Show interface___________________
def interface():

    canvas.create_image(680,320,image=bg3)
    winsound.PlaySound("sound\\start.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

    canvas.create_image(120,70,image=bg_welcome1)
   
    
    canvas.create_image(700,100,image=bg_welcome)
    canvas.create_text(700,120,text="MONKEY EAT FRUITS",font=('BLOODY TYPE PERSONAL USE',35 ,'bold'),fill='gold',tags='start')

    canvas.create_image(700,400,image=bgA)
    canvas.create_text(700,325,text="GAME",font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'),fill='gold',tags='start')

    canvas.create_text(700,400,text="HELP",font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'),fill='gold',tags='help')

    canvas.create_text(700,475,text="STORY",font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'),fill='gold',tags='story')

    canvas.create_image(1130,320,image=MK)
    canvas.create_image(230,320,image=MK)


interface()

# =======================settime=======================

time = 50
def settime():
    global time
    canvas.itemconfig(timer,text='Timer : ' + str(time)+ "s")

    if time <= 50:
        time -= 1

    if time <= 0:
        Lost()
        time=50
    canvas.after(1500,settime)

# __________________Show Help________________________
def helpGame(event):

    canvas.delete('all')

    canvas.create_image(680,320,image=bg8)
    canvas.create_image(300,320,image=MK)

    canvas.create_image(150,40,image=back)
    canvas.create_text(150,42,text="Back", font=('BLOODY TYPE PERSONAL USE', 15 ,'bold'), fill='black', tags='back')

    canvas.create_image(935,350,image=Help)

canvas.tag_bind('help','<Button-1>',helpGame)
# __________________Show Story________________________
def StoryGame(event):

    canvas.delete('all')

    canvas.create_image(680,320,image=bg5)
    canvas.create_image(450,370,image=Child_MK)

    canvas.create_image(150,40,image=back)
    canvas.create_text(150,42,text="Back", font=('BLOODY TYPE PERSONAL USE', 15 ,'bold'), fill='black', tags='back')

    canvas.create_image(935,80,image=story)
    canvas.create_text(935,95,text="STORY", font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'), fill='gold', tags='back')
    canvas.create_image(935,410,image=bg_story)

    canvas.create_image(840,207,image=small_MK)
    canvas.create_text(953,200,text="Little monkeys have ", font=('212BabyGirl', 13 ,'bold'), fill='gold', tags='back')
    canvas.create_text(956,220,text=" to run to eat bananas ", font=('212BabyGirl', 13 ,'bold'), fill='gold', tags='back')
    canvas.create_text(935,240,text="but there must be conditions ", font=('212BabyGirl', 13 ,'bold'), fill='gold', tags='back')
    canvas.create_text(915,260,text=" in each session,such as: ", font=('212BabyGirl', 13 ,'bold'), fill='gold', tags='back')
    canvas.create_text(935,290,text="1.Don't touch the snake will fall ", font=('212BabyGirl', 13 ,'bold'), fill='gold', tags='back')
    canvas.create_text(931,310,text="2.Do not touch the thorns on  ", font=('212BabyGirl', 13 ,'bold'), fill='gold', tags='back')
    canvas.create_text(904,330,text="the dead branches. ", font=('212BabyGirl', 13 ,'bold'), fill='gold', tags='back')
    canvas.create_text(933,350,text="3.Avoid falling rocks and don't ", font=('212BabyGirl', 13 ,'bold'), fill='gold', tags='back')
    canvas.create_text(883,370,text=" touch the fire. ", font=('212BabyGirl', 13 ,'bold'), fill='gold', tags='back')
    canvas.create_text(930,410,text=" Good luck playing each ", font=('BLOODY TYPE PERSONAL USE', 15 ,'bold'), fill='gold', tags='back')
    canvas.create_text(930,440,text=" episode ", font=('BLOODY TYPE PERSONAL USE', 15 ,'bold'), fill='gold', tags='back')
    
    canvas.create_image(930,500,image=WIN)
    canvas.create_text(930,570,text=" hope you win this one. ", font=('BLOODY TYPE PERSONAL USE', 15 ,'bold'), fill='gold', tags='back')

canvas.tag_bind('story','<Button-1>',StoryGame)

# ___________________Show Level________________
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
def countDoor(thewin):
    global win, score
    win = thewin
    if win>=1 and score >= 20:
        winsound.PlaySound("sound\\win.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
        win()
    if win>=1 and score< 20:
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
Boom=random.choices(fruits)


#_____________Funnnction for drawLevel______________
def arrayToDrawing():
    global grid,item,item1,score,life,timer
    canvas.delete('all')
    canvas.create_image(680,340,image=bg6)
    # winsound.PlaySound("sound\\monkey.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)


    canvas.create_image(100,40,image=back)
    canvas.create_text(100,42,text="Back", font=('BLOODY TYPE PERSONAL USE', 15 ,'bold'), fill='black', tags='bac')

    canvas.create_image(400,50,image=bgtop1)
    canvas.create_image(325,50,image=Score_MK)
    canvas.create_text(410,50,text="Score : ",font='212BabyGirl 20 bold' ,fill="white")
    item=canvas.create_text(470,50,text=score,font='212BabyGirl 20 bold',fill='white')

    canvas.create_image(750,50,image=bgtop2)
    canvas.create_image(680,50,image=heart)
    canvas.create_text(750,50,text="Heart :",font='212BabyGirl 20 bold' ,fill="white")
    item1=canvas.create_text(820,50,text=life,font='212BabyGirl 20 bold' ,fill="white")

    canvas.create_image(1115,50,image=bgtop3)
    canvas.create_image(1035,50,image=clock)
    timer = canvas.create_text(1130,50,text='Timer : ' + str(time)+ "s",fill='white',font='212BabyGirl 20 bold')


    
    for ro in range(len(grid)):
        for co in range (len(grid[ro])):

            myfruit=random.choices(fruit)
            Boom=random.choices(fruits)

            x1=160+(30*co)
            x2=150+(30*co)
            y1=150+(30*ro)
            y2=180+(30*ro)
            
            if grid[ro][co]== bgGrid:
                canvas.create_rectangle(x1,y1,x2,y2, fill="", outline='') 

            elif grid[ro][co]== FRUIT:
                canvas.create_image(x1,y1,image=myfruit, anchor="nw")

            elif grid[ro][co]== FAST_FOOD: 
                canvas.create_image(x1,y1,image=Boom, anchor="nw")

            elif grid[ro][co]== WALL:               
                canvas.create_image(x1,y1,image=wall_image, anchor="nw")

            elif grid[ro][co]== FIRE:                
                canvas.create_image(x1,y1,image=fire_image, anchor="nw")
            elif grid[ro][co]== FIRE:                
                canvas.create_image(x1,y1,image=fire_image, anchor="nw")
                
            elif grid[ro][co]== WINS:    
                canvas.create_image(x1,y1,image=win_flag, anchor="nw")

            elif grid[ro][co]== MARIO:               
                canvas.create_image(x1,y1,image=hero_mk, anchor="nw")
                
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
def moveMonkey(direction):
    global win
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

            if grid[row][col-1] == WINS:
                countDoor(win + 1)

            if grid[row][col-1] == FIRE:
                numberOfLife(life - 1)
                winsound.PlaySound("sound\\bird.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

            if grid[row][col-1] != WALL:
                grid[row][col]=0
                grid[row][col-1] =1
#____________________________________________move Right______________________________________________
    if direction == "right":
        if col != len(grid[0])-1:
            if grid[row][col+1] == FRUIT:
                countScore(score + 1)
                winsound.PlaySound("sound\\getCoin.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

            if grid[row][col+1] == FAST_FOOD:
                countScore(score - 1)
                winsound.PlaySound("sound\\eat.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)                

            if grid[row][col+1] == FIRE:
                numberOfLife(life - 1)
                winsound.PlaySound("sound\\bird.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

            
            if grid[row][col+1] == WINS:
                countDoor(win + 1)

            print(win)
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

            
            if grid[row-1][col] == WIN:
                countDoor(win + 1)   

            if grid[row-1][col] == FIRE:
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

            
            if grid[row+1][col] == WINS:
                countDoor(win + 1)

            if grid[row+1][col] == FIRE:
                numberOfLife(life - 1)
                winsound.PlaySound("sound\\bird.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

            
            if grid[row+1][col] != WALL:
                grid[row][col]=0
                grid[row+1][col] =1
                
    arrayToDrawing()

def moveLeft(event):
    moveMonkey("left")

def moveRight(event):
    moveMonkey("right")

def moveUp(event):
    moveMonkey("up")

def moveDown(event):
    moveMonkey("down")

def positionMonkey(grid):  
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 10:
                positionOfMonkey=[r, c]
    return positionOfMonkey

def moveMonkeyLeft(event):
    indexOfMonkey=positionMonkey(grid)
    r=indexOfMonkey[0]
    c=indexOfMonkey[1]
    if c != 0:
        grid[r][c]=0
        grid[r][c-1]=10
    canvas.after(50,lambda: moveMonkeyLeft(event))
    arrayToDrawing()

def moveMonkeyRight(event):
    indexOfMonkey=positionMonkey(grid)
    r=indexOfMonkey[0]
    c=indexOfMonkey[1]
    if c != 0:
        grid[r][c]=0
        grid[r][c+1]=10
    canvas.after(50,lambda: moveMonkeyRight(event))
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

    canvas.create_image(150,40,image=back)
    canvas.create_text(150,42,text="Back",font=('BLOODY TYPE PERSONAL USE', 15 ,'bold'), fill='black', tags='bak')

    canvas.create_text(400, 210, text="Level1",tags="level1", fill='gold', font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'))
    canvas.tag_bind("level1","<Button-1>",level1) 

    canvas.create_text(400, 325, text="Level2",tags="level2", fill='gold', font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'))
    canvas.tag_bind("level2","<Button-1>",level2) 

    canvas.create_text(400, 445, text="Level3",tags="level3", fill='gold', font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'))
    canvas.tag_bind("level3","<Button-1>",level3)    

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
    canvas.create_rectangle(350,200,1050,500,fill='gold')

    canvas.create_text(720,250,text="You Won!",font=('BLOODY TYPE PERSONAL USE', 50 ,'bold'), fill="black")

    canvas.create_image(450,350,image=Score_MK)
    canvas.create_text(550,350,text='score X ', font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'),fill='black')
    canvas.create_text(630,350,text=score,font='212BabyGirl 30 bold',fill='red')

    canvas.create_image(780,350,image=heart)
    canvas.create_text(880,350,text='Heart X ', font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'),fill='black')
    canvas.create_text(950,350,text=' 0',font='212BabyGirl 30 bold',fill='red')

    canvas.create_text(930,450,text='Menu',font=('BLOODY TYPE PERSONAL USE', 30 ,'bold'),fill='black',tags='ne')
    win()

# _________lost_______________
def Lost():

    canvas.create_rectangle(350,200,1050,500,fill='gold')

    canvas.create_text(720,250,text="You Lost!",font=('BLOODY TYPE PERSONAL USE', 50 ,'bold'), fill="black")

    canvas.create_image(450,350,image=Score_MK)
    canvas.create_text(550,350,text='score X ', font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'),fill='black')
    canvas.create_text(630,350,text=score,font='212BabyGirl 30 bold',fill='red')

    canvas.create_image(780,350,image=heart)
    canvas.create_text(880,350,text='Heart X ', font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'),fill='black')
    canvas.create_text(950,350,text=' 0',font='212BabyGirl 30 bold',fill='red')

    canvas.create_text(930,450,text='Menu',font=('BLOODY TYPE PERSONAL USE', 30 ,'bold'),fill='black',tags='ne')

    Lost()


# _____________functionn for next level_____________
def nextLevel(event):
    canvas.delete('all')
    global grid,score,life,win,isfound,isWin,time
    score=0
    win=0
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

