import pyautogui
import pywinctl as gw
import time
import random
from scripts__core.screen_scraping import *
from scripts__core.movements import *

window_title = "RuneLite - litlGenocide"
mouse_movements= mouse_movements(window_title)
screenscrape = screenscrape(window_title)

mouse_movements.move_mouse(300,300)

