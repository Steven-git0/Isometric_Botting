
import pyautogui 
import time
import tkinter as tk
import pywinctl as gw
import math

def update_mouse_position():
    window_title = 'RuneLite - litlGenocide'
    windows = gw.getWindowsWithTitle(window_title)
    x, y = pyautogui.position()

    if windows:
        window = windows[0]
        rx, ry, width, height = window.left, window.top, window.width, window.height
        position_label.config(text=f"Mouse X: {(x-rx)}, Mouse Y: {(y-ry)}")
        size_label.config(text=f"Window Length: {width}, Window Height: {height}")
        ratio_label.config(text=f"Ratio X: {round((x-rx)/width, 5)}, Ratio Y: {round((y-ry)/height, 5)}")
    else:
        position_label.config(text=f"Mouse X: N/A, Mouse Y: N/A (No '{window_title}' window)")
        size_label.config(text="Window Length: N/A, Window Height: N/A")
        ratio_label.config(text="Ratio X: N/A, Ratio Y: N/A")

    abs_label.config(text=f"Mouse X: {(x)}, Mouse Y: {(y)}")

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