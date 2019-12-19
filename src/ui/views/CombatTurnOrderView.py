import tkinter as tk
from tkinter.ttk import *
from presenter.GamePresenter import GamePresenter
from ui.views.IView import IView
from typing import List, Tuple
from ui.views.TtkUtil import get_font_with_modified_settings as get_font
from ui.views.ActorDetailView import ActorDetailView


# TODO: Refactor out all of the style settings into a main app folder, refactor GameModel, implement GamePresenter
# TODO: Add binding to each label to bring up the actor detail view where you can change stuff
# TODO: Add feature to color dead/dying actors another color (?!) and skip over or delete dead actors
# TODO: Add feature to add another actor during combat
# TODO: feature - remove actor during combat
class CombatTurnOrderView(IView, Frame):
    actors: List[Tuple[str, int]]

    def __init__(self, master=None):
        Frame.__init__(self, master)
        if master is not None and hasattr(master, "presenter"):
            self.presenter = master.presenter
        else:
            self.presenter = GamePresenter()
        self.master = master
        self.actors = self.get_actors()
        self.next_button = None
        self.update_button = None
        self.current_turn = 0
        self.init_window()

    def init_window(self):
        self.master.title("Combat Order")
        self.grid()

        info_label = Label(self, text="Click on a name to see details", style="ITALIC.TLabel")
        info_label.grid(row=0, column=0, columnspan=2)

        name_label = Label(self, text="Character Name", style="TITLE.TLabel")
        name_label.grid(row=1, column=0)

        class_label = Label(self, text="Initiative", style="TITLE.TLabel")
        class_label.grid(row=1, column=1)

        self.render_actors()

    def render_actors(self):
        last_row = 1
        for i in range(0, len(self.actors)):
            if i == self.current_turn:
                label_style = "BLUE.TLabel"
            else:
                label_style = "DEFAULT.TLabel"
            temp_name_label = Label(self, text=self.actors[i][0], style=label_style)
            temp_init_label = Label(self, text=self.actors[i][1], style=label_style)
            temp_name_label.grid(row=i + last_row + 1, column=0)
            temp_init_label.grid(row=i + last_row + 1, column=1)
            temp_name_label.bind("<Button 1>", lambda event, actor=self.actors[i][0]:
                                 self.open_detail_view(actor))
            temp_init_label.bind("<Button 1>", lambda event, actor=self.actors[i][0]:
            self.open_detail_view(actor))

        self.next_button = Button(self, text="Next", command=self.next_actor)
        self.update_button = Button(self, text="Update", command=self.update)
        row = len(self.actors) + last_row + 1
        self.update_button.grid(row=row, column=0)
        self.next_button.grid(row=row, column=1)

    def open_detail_view(self, actor: str):
        extra_window = tk.Toplevel(root)
        ActorDetailView(actor, extra_window)

    def next_actor(self):
        self.current_turn = (self.current_turn + 1) % (len(self.actors))
        self.render_actors()

    def update(self, **kwargs):
        self.actors = self.get_actors()
        self.render_actors()

    def get_actors(self) -> List[Tuple[str, int]]:
        actors = self.presenter.get_actor_list()
        initiative = self.presenter.get_initiative_list()
        return [(x, y) for (x, y) in sorted(zip(actors, initiative), key=lambda pair: pair[1], reverse=True)]


root = tk.Tk()
style = Style()
style.theme_use('clam')

style.configure("DEFAULT.TLabel")
bold_button_font = get_font(tk.Button(None), ["weight"], ["bold"])
style.configure("BLUE.TLabel", background="#adc8ef", font=bold_button_font)
italic_font = get_font(tk.Label(None), ["slant"], ["italic"])
style.configure("ITALIC.TLabel", font=italic_font)
title_font = get_font(tk.Label(None), ["weight", "underline"], ["bold", "true"])
style.configure("TITLE.TLabel", font=title_font, anchor="center")

app = CombatTurnOrderView(root)
root.mainloop()
