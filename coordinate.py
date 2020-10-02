import pyautogui
from time import sleep
pyautogui.PAUSE = 1
sleep(5)

#this pyautogui.position() returns the x and y coordinates of the mouse
x,y=pyautogui.position()
print(x,y)


#pyautogui.moveTo(x,y) is used to move the mouse from any position to the point x,y
#pyautogui.click() is used to simulate a mouse click over here.

pyautogui.moveTo(x,y)
pyautogui.click()
