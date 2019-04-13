'''
Created on 12-Apr-2019

@author: guruk
'''
#keep notepad open in pos 5 of taskbar while running this program

import pyautogui

pyautogui.moveTo(419,1062, duration=1)

pyautogui.click()


pyautogui.click(100,100)

pyautogui.typewrite(['end','enter'], interval =0.1)


pyautogui.typewrite('Hello World. This is me Python typing this :)', interval =0.1)

pyautogui.typewrite(['enter','a','space','b', 'left', 'left', 'space','X','space','Y'], interval=0.1)

pyautogui.typewrite(['end','enter'], interval=0.1)

pyautogui.typewrite('Typing this in new line', interval =0.1)

pyautogui.hotkey('ctrl','o')

print(pyautogui.KEYBOARD_KEYS)
