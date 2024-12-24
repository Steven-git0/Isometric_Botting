#install client resizer the settings are for 1400x1000
#pip install pyautogui
import pyautogui 
import time
import tkinter as tk

def update_mouse_position():
    x, y = pyautogui.position()
    position_label.config(text=f"Mouse X: {x}, Mouse Y: {y}")

    color = pyautogui.pixel(x,y)
    color_label.config(text = f"Color: {color}")
    root.after(100, update_mouse_position)  # Update every .1 second

root = tk.Tk()
root.title("Mouse Position Tracker")

position_label = tk.Label(root, text="", font=("Arial", 12))
position_label.pack(padx=10, pady=10)

color_label = tk.Label(root, text="", font=("Arial", 12))
color_label.pack(padx=10, pady=10)

update_mouse_position()  # Start updating the mouse position

root.mainloop()