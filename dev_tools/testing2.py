from windmouse.core import Coordinate
from windmouse.pyautogui_controller import PyautoguiMouseController
import pyautogui
import pywinctl as gw
import time
import random
cursor = PyautoguiMouseController()

for x, y in [(300, 300), (400, 300), (500, 300)]:
    cursor.start_position = (None, None)
    cursor.dest_position = (Coordinate(x), Coordinate(y))
    cursor.move_to_target(step_duration=0.01)


pyautogui.mouseDown(pyautogui.position(), button='right')
time.sleep(random.uniform(.10, .20))
pyautogui.mouseUp(pyautogui.position(), button='right')