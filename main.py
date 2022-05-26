import time
from charset_normalizer import detect
import mss
import numpy as np 
import cv2
import pyautogui
import torch
import os
#from var_file import var_class
from subprocess import run
from var_file import var_class
from colorama import Fore
import keyboard

#os.system('start click.exe')



pyautogui.FAILSAFE = False

#=-=-=-=-=-=-=-=-=-=-=-gui=-=-=-=-=-=-=-=-=-=-=-=
game_select = pyautogui.confirm('Select Your Game', buttons = ['CSGO', 'Fortnite', 'Apex'])
box_size = int(pyautogui.confirm('Select detection box size (416 is standerd)', buttons = ['64', '128', '192', '256', '320', '384', '416', '448', '512', '576', '640', '704', '768']))
accr_test = pyautogui.confirm('Accuracy Level', buttons = ['Low', 'Mid', 'High', 'Very Heigh'])
hold_toggle = pyautogui.confirm('Enable hold or toglle', buttons = ['Hold', 'Toggle'])
epic_mode = pyautogui.confirm('Enable epic mode', buttons = ['Ya', 'Na (im lame)'])
#select box
if game_select == 'CSGO':
    yolo_path = "yolo/CSGO.pt"
if game_select == 'Fortnite':
    yolo_path = "yolo/Fortnite.pt"
if game_select == 'Apex':
    yolo_path = "yolo/Apex.pt"
#box size
box_size2 = int(box_size/2)#finds middle of selected area
width_scr, height_scr = pyautogui.size() #determans hieght and width
width2 = int(width_scr/2-box_size2) #x-cord of where box should start
height2 = int(height_scr/2-box_size2) #y cord of where box should start
print(width_scr, height_scr)
print(width2, height2)
print(box_size2)
#accr
if accr_test == 'Low': #10=10% 6.5=15.38...% 5=20% 3=33%
    accr = 10
if accr_test == 'Mid':
    accr = 6.5
if accr_test == 'High':
    accr = 5
if accr_test == 'Very High':
    accr = 3
    print("accr:", accr)
#epic mode=-=-=-=-=-=-
logo = var_class.logo
if epic_mode == "Ya":
    funny = var_class.funny
    funny2 = var_class.funny2
    funny3 = var_class.funny3
if epic_mode == "Na (im lame)":
    funny = var_class.lame
    funny2 = var_class.lame2
    funny3 = var_class.lame3

detect_var=0
#hold or toggle=-==-=-=--
if hold_toggle == 'Hold':
    hold_toggle = 0
if hold_toggle == 'Toggle':
    hold_toggle = 1


accr = 10
on_off = 1
var_1 = 0
print(Fore.GREEN + logo)
model = torch.hub.load('ultralytics/yolov5', 'custom', path=yolo_path, force_reload=True)
with mss.mss() as sct:
    monitor = {'top': 332, 'left': 752, 'width':416, 'height': 416}
os.system('cls')
print(funny)
while True:
        #t = time.time()

        img = np.array(sct.grab(monitor))

        results = model(img)

        
        #cv2.imshow('s', np.squeeze(results.render())) #does not respond : (

        #print('fps: {}'.format(1/ (time.time() - t)))
        #print(detect_var)

        rl = results.xyxy[0].tolist()

        if len(rl) > 0:

                if rl[0][4] > .35:

                        if rl[0][5] == 0:

                            detect_var=1

                            boxX = int(rl[0][0]) #displays relitive to box
                            boxY = int(rl[0][1])

                            box2X = int(rl[0][2])
                            box2Y = int(rl[0][3])
                            
                            width = box2X - boxX

                            finboxX = int(boxX+(width/accr))

                            finbox2X = int(box2X-(width/accr))

                            box_equ = finboxX < box_size2 < finbox2X and boxY < box_size2 < box2Y

                            if box_equ == True and on_off == 1:
                                
                                if var_1 == 0:
                                    var_1 = 1
                                    #print("on")
                                    pyautogui.keyUp('8')
                                    if hold_toggle == 1:
                                        os.system('start click.ahk')
                                    else:
                                        os.system('start click2.ahk')
                                        print("ran")
                                    #os.system('cls')
                                    print(funny3)
                            else:
                                detect_var=0
                                if var_1 == 1:
                                    var_1 = 0
                                    #print("changing off")
                                    pyautogui.keyDown('8')
                                    os.system('cls')
                                    if on_off == 1:
                                        print(funny)
                                    if on_off == 0:
                                        print(funny2)
        
        else:
            detect_var=0
            if var_1 == 1:
                var_1 = 0
                #print("changing off")
                pyautogui.keyDown('8')

        if keyboard.is_pressed('f1'):
            os.system('cls')
            on_off = 1
            print(funny)
        

        if keyboard.is_pressed('f2'):
            os.system('cls')
            on_off = 0
            print(funny2)