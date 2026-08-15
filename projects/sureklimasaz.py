import pyautogui 
import time

time.sleep(10)

def mesaj():
    
    pyautogui.write("deneme")
    pyautogui.press('enter')

while True:
    mesaj()    