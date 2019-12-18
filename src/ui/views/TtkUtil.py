import tkinter as tk
import tkinter.font as tk_font
from typing import List


def get_font_with_modified_settings(widget: tk.Widget, settings: List[str], values: List[str]) -> tk_font:
    font = (tk_font.Font(font=widget['font'])).actual()  # get settings dict
    for setting, value in zip(settings, values):
        font[setting] = value  # modify setting
    font = tk_font.Font(**font)  # use modified dict to create Font
    return font
