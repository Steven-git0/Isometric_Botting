#install client resizer the settings are for 1400x1000
#pip install pyautogui
import pyautogui 
import time
import tkinter as tk
import pygetwindow as gw
import math

def update_mouse_position():
    window_title = 'RuneLite - litlGenocide'
    window = gw.getWindowsWithTitle(window_title)[0]

    if not window:
        print(f"No window found with title '{window_title}'")
        exit()

    rx, ry, width, height = window.left, window.top, window.width, window.height
    x, y = pyautogui.position()
    
    position_label.config(text=f"Mouse X: {(x-rx)}, Mouse Y: {(y-ry)}")

    abs_label.config(text=f"Mouse X: {(x)}, Mouse Y: {(y)}")

    size_label.config(text=f"Window Length: {width}, Window Height: {height}")

    ratio_label.config(text=f"Ratio X: {round((x-rx)/width, 5)}, Ratio Y: {round((y-ry)/height, 5)}")

    color = pyautogui.pixel(x,y)
    color_label.config(text = f"Color: {color}")
    root.after(100, update_mouse_position)  # Update every .1 second

root = tk.Tk()
root.title("Mouse Position Tracker")

position_label = tk.Label(root, text="", font=("Arial", 12))
position_label.pack(padx=10, pady=10)

abs_label = tk.Label(root, text="", font=("Arial", 12))
abs_label.pack(padx=10, pady=10)

size_label = tk.Label(root, text="", font=("Arial", 12))
size_label.pack(padx=10, pady=10)

ratio_label = tk.Label(root, text="", font=("Arial", 12))
ratio_label.pack(padx=10, pady=10)

color_label = tk.Label(root, text="", font=("Arial", 12))
color_label.pack(padx=10, pady=10)

update_mouse_position()  # Start updating the mouse position

root.mainloop()