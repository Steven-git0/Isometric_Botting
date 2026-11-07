# right_panel.py
from customtkinter import *

class RightPanel(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#ffffff", **kwargs)
        self.pack_propagate(False)

        # --- Header ---
        CTkLabel(
            master=self,
            text="Select your Script",
            text_color="#601E88",
            font=("Arial Bold", 22)
        ).pack(pady=(24, 10))

        # --- Container for top and bottom sections ---
        content_frame = CTkFrame(master=self, fg_color="transparent")
        content_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Top frame: scrollable script list
        self.right_scroll = CTkScrollableFrame(
            master=content_frame,
            fg_color="transparent",
            height=250  # Limit height so bottom section is visible
        )
        self.right_scroll.pack(fill="x", side="top", pady=(0, 10))

        self.default_label = CTkLabel(
            master=self.right_scroll,
            text="Choose a category to display scripts.",
            font=("Arial", 16)
        )
        self.default_label.pack(pady=20)

        # Bottom frame: parameters input
        self.param_frame = CTkFrame(master=content_frame, fg_color="#f5f5f5")
        self.param_frame.pack(fill="both", expand=True, side="bottom", pady=(10, 0))

        CTkLabel(
            master=self.param_frame,
            text="Parameters",
            text_color="#601E88",
            font=("Arial Bold", 18)
        ).pack(pady=5)

        self.param_entries = {}  # store script param inputs

    def show_scripts(self, scripts, execute_script_func):
        # Clear script list
        for widget in self.right_scroll.winfo_children():
            widget.destroy()

        if not scripts:
            CTkLabel(master=self.right_scroll, text="No scripts found.").pack(pady=10)
            return

        for script in scripts:
            CTkButton(
                master=self.right_scroll,
                text=script,
                command=lambda s=script: self.show_parameters_for_script(s, execute_script_func),
                height=40
            ).pack(fill="x", padx=5, pady=3)

    def show_parameters_for_script(self, script_name, execute_script_func):
        # Clear old parameter fields
        for widget in self.param_frame.winfo_children():
            widget.destroy()

        CTkLabel(
            master=self.param_frame,
            text=f"Parameters for {script_name}",
            text_color="#601E88",
            font=("Arial Bold", 16)
        ).pack(pady=(5, 10))

        # Example dynamic parameters — replace with real logic
        params = ["Username", "World", "Repeat Count"]

        self.param_entries.clear()
        for p in params:
            CTkLabel(master=self.param_frame, text=p).pack(anchor="w", padx=10)
            entry = CTkEntry(master=self.param_frame)
            entry.pack(fill="x", padx=10, pady=(0, 5))
            self.param_entries[p] = entry

        CTkButton(
            master=self.param_frame,
            text="Run Script",
            fg_color="#601E88",
            text_color="#ffffff",
            command=lambda: execute_script_func(
                script_name,
                {k: v.get() for k, v in self.param_entries.items()}
            )
        ).pack(pady=10)