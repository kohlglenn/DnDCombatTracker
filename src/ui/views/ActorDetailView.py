import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import *
from presenter.GamePresenter import GamePresenter
from ui.views.IView import IView
from typing import List, Tuple
from ui.views.TtkUtil import get_font_with_modified_settings as get_font


class ActorDetailView(IView, Frame):
    def __init__(self, actor: str, master=None):
        Frame.__init__(self, master)
        if master is not None and hasattr(master, "presenter"):
            self.presenter = master.presenter
        else:
            self.presenter = GamePresenter()
        self.master = master
        self.actor = actor
        self.update_button = None
        self.current_turn = 0
        self.hp_val = tk.StringVar()
        self.hp_val.set("195")
        self.init_window()

    # TODO: Finish copying format from here https://tetra-cube.com/dnd/dnd-statblock.html
    # TODO: Make it look nicer
    def init_window(self):
        self.master.title("Actor Detail View")
        self.pack()

        name_label = Label(self, text="Adult Black Dragon")
        name_label.pack()
        size_alignment_label = Label(self, text="Huge dragon, chaotic evil")
        size_alignment_label.pack()
        ac_label = Label(self, text="Armor Class 19 (natural armor)")
        ac_label.pack()
        hp_label = Label(self, text="Hit Points")
        hp_label.pack()
        hp_entry = Entry(self, textvariable=self.hp_val)
        hp_entry.pack()
        speed_label = Label(self, text="Speed 40 ft., fly 80 ft., swim 20 ft.")
        speed_label.pack()
        self.pack_table(headers=["STR", "DEX", "CON", "INT", "WIS", "CHA"],
                        values=[self.presenter.get_stat_block_with_mods(self.actor)])


    def pack_table(self, headers: List[str], values: List[List[str]]):
        table = Frame(self)
        table.pack()
        for column in range(0, len(headers)):
            header = headers[column]
            temp_header = Label(table, text=header, style="UNDERLINE.TLabel")
            temp_header.grid(row=0, column=column)
            for row in range(0, len(values)):
                value = values[row][column]
                temp_value = Label(table, text=value)
                temp_value.grid(row=row+1, column=column)

    def update(self, **kwargs):
        pass


root = tk.Tk()
root.geometry("300x400")
style = Style()
style.theme_use('clam')
underline_label_font = get_font(tk.Label(None), ["underline"], ["true"])
style.configure("UNDERLINE.TLabel", font=underline_label_font)
app = ActorDetailView("Test", root)
root.mainloop()
