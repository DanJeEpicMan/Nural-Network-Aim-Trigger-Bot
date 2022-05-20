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
from pynput.keyboard import Key, Controller

keyboard = Controller()
#keyboard.press(Key.space)
#keyboard.release(Key.space)

keyboard.press('a')
time.sleep(5)
keyboard.release('a')

# Type two upper case As
#keyboard.press('A')a
#keyboard.release('A')
#with keyboard.pressed(Key.shift):
    #keyboard.press('a')
    #keyboard.release('a')