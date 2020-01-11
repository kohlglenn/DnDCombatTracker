import tkinter as tk
from tkinter.ttk import *
from presenter.GamePresenter import GamePresenter
from ui.views.IView import IView
from ui.views.CreateNpcView import CreateNpcView
from ui.views.CreatePlayerView import CreatePlayerView
from ui.views.CombatTurnOrderView import CombatTurnOrderView
from ui.views.TtkUtil import get_font_with_modified_settings as get_font


class App(IView, Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        if master is not None and hasattr(master, "presenter"):
            self.presenter = master.presenter
        else:
            self.presenter = GamePresenter()
        self.master = master
        self.row_end = 1
        self.init_window()

    def init_window(self):
        self.master.title("Main App")
        self.pack()

        create_npc_button = Button(self, text="Add NPC(s)",
                                   command=lambda: self.launch_window(CreateNpcView))
        create_player_button = Button(self, text="Add Player(s)",
                                      command=lambda: self.launch_window(CreatePlayerView))
        combat_turn_order_button = Button(self, text="Combat Turn Order",
                                          command=lambda: self.launch_window(CombatTurnOrderView))
        create_npc_button.pack()
        create_player_button.pack()
        combat_turn_order_button.pack()

    def launch_window(self, constructor):
        extra_window = tk.Toplevel(self)
        constructor(extra_window)

    def update(self, **kwargs):
        pass


root = tk.Tk()
root.geometry("200x200")
style = Style()
style.theme_use('clam')

# Custom styles
style.configure("DEFAULT.TLabel")
bold_button_font = get_font(tk.Button(None), ["weight"], ["bold"])
style.configure("BLUE.TLabel", background="#adc8ef", font=bold_button_font)
italic_font = get_font(tk.Label(None), ["slant"], ["italic"])
style.configure("ITALIC.TLabel", font=italic_font)
title_font = get_font(tk.Label(None), ["weight", "underline"], ["bold", "true"])
style.configure("TITLE.TLabel", font=title_font, anchor="center")
underline_label_font = get_font(tk.Label(None), ["underline"], ["true"])
style.configure("UNDERLINE.TLabel", font=underline_label_font)

app = App(root)
root.mainloop()
