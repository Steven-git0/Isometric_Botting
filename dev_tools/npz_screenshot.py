import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
import pyautogui
import numpy as np
import pygetwindow as gw
import time
import cv2
from PIL import Image, ImageEnhance, ImageFilter
import pygetwindow as gw
from sklearn.cluster import DBSCAN
import re
from core_scripts.screen_scraping import *
from core_scripts.movements import *

window_title = "RuneLite - litlGenocide"

window = gw.getWindowsWithTitle(window_title)[0]
if not window:
    print(f"No window found with title '{window_title}'")
    exit()
rx, ry, width, height = window.left, window.top, window.width, window.height

mouse_movements = mouse_movements(window_title)
screenscrape = screenscrape(window_title)


screenshot = pyautogui.screenshot(region=(623, 682, 35, 30))
#screenshot.show()

needle_color = cv2.cvtColor(np.array(screenshot.convert("RGB")), cv2.COLOR_RGB2BGR)

needle_gray  = cv2.cvtColor(needle_color, cv2.COLOR_BGR2GRAY)
needle_edges = cv2.Canny(needle_gray, 50, 150)
kernel = np.ones((3,3), np.uint8)
needle_edges = cv2.dilate(needle_edges, kernel, iterations=1)

np.savez(
    'image_identification/deposit_inv.npz',
    needle_color=needle_color,
    needle_edges=needle_edges
)

