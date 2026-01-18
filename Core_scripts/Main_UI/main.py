"""
main.py — Sandscripts for OSRS
- Creates the CTk root window
- Shows a login screen first
- After login, shows LeftPanel (categories) and RightPanel (scripts + params)
- LeftPanel -> chooses a category
- RightPanel -> lists scripts from that category (top), shows params and Run (bottom)
"""

# =========================
# 1) Imports & Constants
# =========================
import os
import sys
# import subprocess  # uncomment if you want to actually run scripts

from customtkinter import *
from PIL import Image

# These are your panel classes defined in separate files:
#   right_panel.py -> class RightPanel(CTkFrame)
#   left_panel.py  -> class LeftPanel(CTkFrame)
from right_panel import RightPanel
from left_panel import LeftPanel

# Map the left-side categories to Windows folders that contain .py scripts
SCRIPTS_MAP = {
    "Category 1": r"scripts_mining",
    "Category 2": r"scripts_theiving",
}

# If you want more categories later, add them here and also add labels to LEFT_CATEGORIES
LEFT_CATEGORIES = list(SCRIPTS_MAP.keys())  # ["Category 1", "Category 2"]


# =========================
# 2) App Setup
# =========================
set_window_scaling(1)        # scales geometry() args on HiDPI
set_appearance_mode("System")

app = CTk()
app.geometry("800x600")
app.resizable(True, True)
app.title("Sandscripts for OSRS")


# =========================
# 3) Assets / Images
# =========================
# Note: using raw strings to avoid backslash-escape issues on Windows.
side_img_data = Image.open(r"core_scripts\Main_UI\side-img.png")
email_icon_data = Image.open(r"core_scripts\Main_UI\email-icon.png")
password_icon_data = Image.open(r"core_scripts\Main_UI\password-icon.png")
google_icon_data = Image.open(r"core_scripts\Main_UI\google-icon.png")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(400, 600))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20, 20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))
google_icon = CTkImage(dark_image=google_icon_data, light_image=google_icon_data, size=(17, 17))


# =========================
# 4) Login Screen
# =========================
# Left splash image (visible on login)
splash_image = CTkLabel(master=app, text="", image=side_img)
splash_image.pack(expand=True, side="left")

# Right-side login frame
login_frame = CTkFrame(master=app, width=400, height=600, fg_color="#ffffff")
login_frame.pack_propagate(False)  # keep fixed size
login_frame.pack(expand=True, side="right")

CTkLabel(
    master=login_frame,
    text="Welcome Back!",
    text_color="#601E88",
    font=("Arial Bold", 24)
).pack(pady=(50, 5))

CTkLabel(
    master=login_frame,
    text="Sign in to your account",
    text_color="#7E7E7E",
    font=("Arial Bold", 12)
).pack()

CTkLabel(
    master=login_frame,
    text="  Email:",
    text_color="#601E88",
    font=("Arial Bold", 14),
    image=email_icon,
    compound="left",
    justify="left",
    anchor="w"
).pack(pady=(38, 0))

CTkEntry(
    master=login_frame,
    width=225,
    fg_color="#EEEEEE",
    border_color="#601E88",
    border_width=1,
    text_color="#000000"
).pack()

CTkLabel(
    master=login_frame,
    text="  Password:",
    text_color="#601E88",
    font=("Arial Bold", 14),
    image=password_icon,
    compound="left",
    justify="left"
).pack(pady=(21, 0))

CTkEntry(
    master=login_frame,
    width=225,
    fg_color="#EEEEEE",
    border_color="#601E88",
    border_width=1,
    text_color="#000000",
    show="*"
).pack()


# =========================
# 5) Panels (created but not packed until after login)
# =========================
right_panel = RightPanel(master=app)  # your class from right_panel.py
left_panel_widget = None              # will be created after login (needs callback wiring)


# =========================
# 6) Wiring: Load & Execute
# =========================
def load_scripts(category_name: str):
    """
    Called by LeftPanel when a category is selected.
    Looks up the folder in SCRIPTS_MAP, lists .py files, and shows them in RightPanel.
    """
    folder = SCRIPTS_MAP.get(category_name)
    scripts = []
    if folder and os.path.isdir(folder):
        scripts = [f for f in os.listdir(folder) if f.endswith(".py")]
    else:
        print(f"[WARN] Missing/invalid folder for '{category_name}': {folder}")

    # Wrap execute_script so RightPanel can pass (script_name, params) and we still know the category.
    right_panel.show_scripts(
        scripts,
        lambda script_name, params=None: execute_script(category_name, script_name, params or {})
    )


def execute_script(category_name: str, script_name: str, params: dict):
    """
    Called by RightPanel when the user clicks 'Run Script'.
    For now, just prints what would run. You can enable subprocess below.
    """
    folder = SCRIPTS_MAP.get(category_name)
    if not folder:
        print(f"[ERROR] Unknown category: {category_name}")
        return

    script_path = os.path.join(folder, script_name)
    print(f"Would run: {script_path} with params: {params}")

    # Example: actually run with Python + --key=value args
    # cmd = [sys.executable, script_path] + [f"--{k}={v}" for k, v in params.items()]
    # subprocess.Popen(cmd)  # or subprocess.run(cmd, check=True)


# =========================
# 7) Login -> Show Main UI
# =========================
def on_login():
    # Hide login UI
    login_frame.pack_forget()
    splash_image.pack_forget()

    # Create a container frame for left/right panels
    main_container = CTkFrame(app)
    main_container.pack(fill="both", expand=True)

    # Grid setup: left column fixed, right column expands
    main_container.grid_columnconfigure(0, weight=0)
    main_container.grid_columnconfigure(1, weight=1)
    main_container.grid_rowconfigure(0, weight=1)

    # Left panel (uses your new LeftPanel signature)
    global left_panel_widget
    left_panel_widget = LeftPanel(
        master=main_container,
        on_category_selected=load_scripts,
        mining_icon_path=r"core_scripts\Main_UI\panel_img\pickaxe.png",
        thieving_icon_path=r"core_scripts\Main_UI\panel_img\theivingmask.png",
        icon_size=(56, 56),   # tweak as you like
        columns=3             # future-proof grid; only 2 items now
    )
    left_panel_widget.configure(width=260)
    left_panel_widget.grid(row=0, column=0, sticky="ns")

    # Right panel
    global right_panel
    right_panel = RightPanel(master=main_container)
    right_panel.grid(row=0, column=1, sticky="nsew")


CTkButton(
    master=login_frame,
    text="Login",
    fg_color="#601E88",
    hover_color="#E44982",
    font=("Arial Bold", 12),
    text_color="#ffffff",
    width=225,
    command=on_login
).pack(pady=(40, 0))


# =========================
# 8) Mainloop
# =========================
app.mainloop()
