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
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(root) 

# ________________Virable_________________
score=0
flag=0
isfound=False
isWin=True
life=3
bgGrid = 0

#______________Images _________________________



hero_mk=tk.PhotoImage(file=os.path.join('imags','hero.png'))
wall_image=tk.PhotoImage(file=os.path.join('imags','walld1.png'))
BN_imag=tk.PhotoImage(file=os.path.join('imags','banana1.png'))
win_imag=tk.PhotoImage(file=os.path.join('imags','win.png'))
win_flag=tk.PhotoImage(file=os.path.join('imags','win_flag.png'))
fire_image=tk.PhotoImage(file=os.path.join('imags','fire.png'))
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
banana1=tk.PhotoImage(file=os.path.join('imags','banana1.png'))
banana2=tk.PhotoImage(file=os.path.join('imags','banana1.png'))
banana3=tk.PhotoImage(file=os.path.join('imags','banana1.png'))
banana4=tk.PhotoImage(file=os.path.join('imags','banana1.png'))

banana5=tk.PhotoImage(file=os.path.join('imags','banana1.png'))
banana6=tk.PhotoImage(file=os.path.join('imags','banana2.png'))
banana7=tk.PhotoImage(file=os.path.join('imags','banana2.png'))
banana8=tk.PhotoImage(file=os.path.join('imags','banana2.png'))
Monkey=tk.PhotoImage(file=os.path.join('imags','monkey-mom.png'))
clock=tk.PhotoImage(file=os.path.join('imags','clock.png'))
heart=tk.PhotoImage(file=os.path.join('imags','heart.png'))
Score_MK=tk.PhotoImage(file=os.path.join('imags','monkey-mom.png'))
back=tk.PhotoImage(file=os.path.join('imags','back.png'))



fruit=[banana1,banana2,banana3,banana4,banana5,]
fruits=[banana6,banana7 ,banana8]


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


#_____________Funnnction for drawLevel______________
def levelEasy(event):
    global item,item1,score,life,timer
    canvas.delete('all')
    canvas.create_image(680,340,image=bg6)
  

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

    # ________________start-hero-level1__________________

    canvas.create_image(70,495,image=hero_mk)
    canvas.create_image(103,550,image=wall_image)
    canvas.create_image(300,450,image=wall_image)
    canvas.create_image(500,350,image=wall_image)
    canvas.create_image(700,550,image=wall_image)
    canvas.create_image(750,250,image=wall_image)
    canvas.create_image(1000,370,image=wall_image)
    canvas.create_image(1250,600,image=wall_image)

    canvas.create_image(1253,210,image=wall_image)
    canvas.create_image(1210,180,image=BN_imag)
    canvas.create_image(1290,170,image=win_flag)

   

    settime()
#_____________Funnnction for drawLevel______________
def levelMedium(event):
    global item,item1,score,life,timer
    canvas.delete('all')
    canvas.create_image(680,340,image=bg6)
  

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


    settime()


#_____________Funnnction for drawLevel______________
def levelHard(event):
    global item,item1,score,life,timer
    canvas.delete('all')
    canvas.create_image(680,340,image=bg6)
  

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


    



    settime()

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

    canvas.create_text(400, 210, text="Easy",tags="level1", fill='gold', font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'))
    canvas.tag_bind("level1","<Button-1>",levelEasy) 

    canvas.create_text(400, 325, text="Medium",tags="level2", fill='gold', font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'))
    canvas.tag_bind("level2","<Button-1>",levelMedium) 

    canvas.create_text(400, 445, text="Hard",tags="level3", fill='gold', font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'))
    canvas.tag_bind("level3","<Button-1>",levelHard)    

# _______________Back click________________
def bakClick(event):
    canvas.delete('all')
    interface()
canvas.tag_bind('bak','<Button-1>',bakClick)

# _________lost_______________
def Lost():

    canvas.create_rectangle(220,200,1000,500,fill='white')

    canvas.create_text(600,250,text="You Lost!",font=('BLOODY TYPE PERSONAL USE', 50 ,'bold'), fill="black")

    canvas.create_image(300,350,image=Score_MK)
    canvas.create_text(400,350,text='score X ', font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'),fill='black')
    canvas.create_text(480,350,text=score,font='212BabyGirl 30 bold',fill='red')

    canvas.create_image(700,350,image=heart)
    canvas.create_text(790,350,text='Heart X ', font=('BLOODY TYPE PERSONAL USE', 25 ,'bold'),fill='black')
    canvas.create_text(860,350,text=' 0',font='212BabyGirl 30 bold',fill='red')

    canvas.create_text(900,450,text='Menu',font=('BLOODY TYPE PERSONAL USE', 30 ,'bold'),fill='black',tags='ne')

    Lost()

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


# __


# _____________functionn for next level_____________
def nextLevel(event):
    canvas.delete('all')
    global score,life,flag,isfound,isWin,time
    score=0
    flag=0
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