import pyautogui
import time
from random import randrange

print('started :)')
# switch tabs after 17sec and page up-down after 2 sec to increase key inputs
while (True):
    pyautogui.keyDown('alt')
    time.sleep(.5)
    for i in range(randrange(5)):
        pyautogui.press('tab')
        time.sleep(.5)
    pyautogui.keyUp('alt')
    time.sleep(7)
    for i in range(randrange(5)):
        pyautogui.press('pageup')
        time.sleep(.5)
    for i in range(randrange(5)):
        pyautogui.press('pagedown')
        time.sleep(.5)
