from ast import Delete
from asyncio import events
# from cgitb import text
# from ctypes.wintypes import tagSIZE
from email.mime import image
import tkinter as tk
from tkinter import Tk, Canvas
# from typing import Counter 
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
snack_image=tk.PhotoImage(file=os.path.join('imags','enemy.png'))
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



