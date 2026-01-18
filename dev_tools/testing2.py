from humancursor import SystemCursor
import pyautogui
import pygetwindow as gw
import time
import random
cursor = SystemCursor()

cursor.move_to([300, 300], duration = 0.01)
cursor.move_to([400, 300], duration = 0.01)
cursor.move_to([500, 300], duration = 0.01)


pyautogui.mouseDown(pyautogui.position(), button='right')
time.sleep(random.uniform(.10, .20))
pyautogui.mouseUp(pyautogui.position(), button='right')