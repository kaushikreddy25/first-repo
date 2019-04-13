'''
Created on 12-Apr-2019

@author: guruk
'''
import pyautogui

print(pyautogui.size())

print(pyautogui.position())

pyautogui.moveTo(500, 500, duration= 1)

pyautogui.moveRel(500, 0, duration= 1)


pyautogui.moveRel(-400, -450, duration= 1)

pyautogui.click(558,46)

pyautogui.click()

#Use pytautogui.displayMousePosition() from cmd to check the position of clickable
#to write the coordinates in program