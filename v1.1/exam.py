import time
import mss
import numpy as np 
import cv2
import pyautogui
import torch
import os
#from var_file import var_class
from subprocess import run

#os.system(r'C:\Windows\NNA\trigger.py')



pyautogui.FAILSAFE = False

detect_var=0

accr = 10
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'C:\Windows\NNA\CSGO.pt', force_reload=True)
with mss.mss() as sct:
    monitor = {'top': 332, 'left': 752, 'width':416, 'height': 416}
os.system('cls')
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

                            boxX = int(rl[0][2]) #displays relitive to box
                            boxY = int(rl[0][3])

                            box2X = int(rl[0][0])
                            box2Y = int(rl[0][1])

                            width = box2X - boxX

                            finboxX = boxX+(width/accr)

                            finbox2X = box2X-(width/accr)

                        #print("x1:", boxX,"y1:", boxY,"x2:", box2X,"y2:", box2Y)

                        #!!!LMB up here
        else:
            detect_var=0
