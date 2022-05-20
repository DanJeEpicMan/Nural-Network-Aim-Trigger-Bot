import time
from charset_normalizer import detect
from matplotlib.pyplot import box
import mss
import numpy as np 
import cv2
import pyautogui
import torch
import os
#from var_file import var_class
from subprocess import run
import threading
from colorama import Fore
import keyboard
#python -m pip install pysimplegui
var_1 = 1

detect_var=0
box2X=0
box2Y=0
boxX=0
boxY=0
width=0
#=-=-=-=-=-=-=config-=-=-=-=-=-=-=-

game_select = pyautogui.confirm('Select Your Game', buttons = ['CSGO', 'Fortnite', 'Apex'])
box_size = int(pyautogui.confirm('Select detection box size (416 is standerd)', buttons = ['64', '128', '192', '256', '320', '384', '416', '448', '512', '576', '640', '704', '768']))
epic_mode = pyautogui.confirm('Enable epic mode', buttons = ['Ya', 'Na (im lame)'])
#select box
if game_select == 'CSGO':
    yolo_path = "yolo/CSGO.pt"
if game_select == 'Fortnite':
    yolo_path = "yolo/Fortnite.pt"
if game_select == 'Apex':
    yolo_path = "yolo/Apex.pt"
#box size
box_size2 = int(box_size/2)
width_scr, height_scr = pyautogui.size()
width2 = int(width_scr/2-box_size2) 
height2 = int(height_scr/2-box_size2)
print(width_scr, height_scr)
print(width2, height2)
print(box_size2)

def yolo_detect():
    print(Fore.GREEN + "yolo_detect active")
    on_off = 1
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=yolo_path, force_reload=True)
    with mss.mss() as sct:
        monitor = {'top': width2, 'left': height2, 'width':box_size, 'height': box_size}
    # os.system('cls')
    while True:
        t = time.time()

        img = np.array(sct.grab(monitor))

        results = model(img)

        
        #cv2.imshow('s', np.squeeze(results.render())) #does not respond : (

        print('fps: {}'.format(1/ (time.time() - t)))
        #print(detect_var)

        rl = results.xyxy[0].tolist()

        if len(rl) > 0:

                if rl[0][4] > .35:

                        if rl[0][5] == 0:

                            detect_var=1
                            print(detect_var)

                            box2X = int(rl[0][2]) #displays relitive to box
                            box2Y = int(rl[0][3])

                            boxX = int(rl[0][0])
                            boxY = int(rl[0][1])
                            
                            box_equ = boxX < box_size2 < box2X and boxY < box_size2 < box2Y

                            if box_equ == True and on_off == 1:
                                print("work")


                            #print(boxX, boxY, box2X, box2Y, width)

                        #print("x1:", boxX,"y1:", boxY,"x2:", box2X,"y2:", box2Y)
        else:
            detect_var=0
  
  
if var_1 == 1:

    #find out why multithred was so slow

    # creating threads
    t1 = threading.Thread(target=yolo_detect)
    #t2 = threading.Thread(target=tb_shoot)  
  
    #starting threads
    t1.start()
    #t2.start()