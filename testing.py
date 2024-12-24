import pygetwindow as gw
import pyautogui
import time

# The excact specific title of your game
window_title = 'RuneLite - litlGenocide'

# Get the window object
windows = gw.getWindowsWithTitle(window_title)
if not windows:
    print(f"No window found with title '{window_title}'")
    exit()

window = windows[0]  # Select the first matching window

# Get window dimensions
window_left = window.left
window_top = window.top
window_width = window.width
window_height = window.height

print(f"width, height, left, top ({window_width}, {window_height}, {window_left}, {window_top})")

center_x = (window_left + window_width // 2) - 17
center_y = window_top + window_height // 2

print( center_x, center_y)

pyautogui.moveTo(center_x , center_y)



