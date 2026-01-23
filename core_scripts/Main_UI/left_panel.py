# left_panel.py
import os
from customtkinter import *
from PIL import Image, ImageOps

class LeftPanel(CTkFrame):
    """
    Left panel with a grid of category buttons.
    - Currently shows 2 categories (Mining, Thieving).
    - Grid is ready for 3 columns when you add more categories later.
    - on_category_selected is called with the category id ("Category 1" / "Category 2").
    """

    def __init__(
        self,
        master,
        on_category_selected,
        mining_icon_path: str | None = None,
        thieving_icon_path: str | None = None,
        icon_size: tuple[int, int] = (48, 48),
        columns: int = 3,  # future-proof: 3-column grid ready
        **kwargs
    ):
        super().__init__(master, width=400, fg_color="#D3D3D3", **kwargs)
        self.pack_propagate(False)

        # ---------- Header ----------
        CTkLabel(
            master=self,
            text="Select the Category",
            text_color="#601E88",
            font=("Arial Bold", 22)
        ).pack(pady=(16, 8))

        # ---------- Scroll container ----------
        cat_scroll = CTkScrollableFrame(
            master=self,
            fg_color="transparent",
            width=400,
            height=540
        )
        cat_scroll.pack(expand=True, fill="both", padx=10, pady=10)

        # Optional: hide scrollbar (private API; ignore if it errors)
        try:
            cat_scroll._scrollbar.grid_remove()
        except Exception:
            pass

        # ---------- Categories (only 2 for now) ----------
        categories = [
            {
                "id": "Category 1",
                "label": "Mining",
                "icon_path": mining_icon_path or r"core_scripts\Main_UI\panel_img\pickaxe.png",
                "enabled": True,
            },
            {
                "id": "Category 2",
                "label": "Thieving",
                "icon_path": thieving_icon_path or r"core_scripts\Main_UI\panel_img\theivingmask.png",
                "enabled": True,
            },
        ]

        # ---------- Helper: CTkImage from path (centered/padded) ----------
        def make_icon(path: str | None):
            w, h = icon_size
            if path and os.path.isfile(path):
                try:
                    img = Image.open(path)
                    img = ImageOps.contain(img, (w, h))
                    canvas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
                    cx = (w - img.width) // 2
                    cy = (h - img.height) // 2
                    canvas.paste(img, (cx, cy))
                    return CTkImage(light_image=canvas, dark_image=canvas, size=(w, h))
                except Exception:
                    pass
            # Fallback placeholder
            ph = Image.new("RGBA", (w, h), (230, 230, 230, 255))
            return CTkImage(light_image=ph, dark_image=ph, size=(w, h))

        # ---------- Build buttons in a N-column grid ----------
        for i, cat in enumerate(categories):
            icon = make_icon(cat["icon_path"])
            btn = CTkButton(
                master=cat_scroll,
                text=cat["label"],
                image=icon,
                compound="top",         # text below image
                text_color="#8B4513",   # brown text
                width=100,
                height=84,              # tighter; reduces extra vertical padding
                anchor="center",        # center contents
                fg_color="transparent", # optional
                hover_color="#e0e0e0",  # optional
                state=("normal" if cat["enabled"] else "disabled"),
                command=(lambda cid=cat["id"]: on_category_selected(cid)) if cat["enabled"] else None
            )
            # Tighten gap between image and text if supported
            try:
                btn.configure(text_spacing=0)
            except Exception:
                pass

            row, col = divmod(i, columns)
            btn.grid(row=row, column=col, padx=8, pady=8, sticky="ew")

        # Make up to `columns` grid columns expand evenly
        for c in range(columns):
            cat_scroll.grid_columnconfigure(c, weight=1)
