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
        self.hp_entry = None
        self.init_window()

    # TODO: Make it look nicer with headers and formatting
    def init_window(self):
        self.master.title("Actor Detail View")
        self.pack()

        class_name = self.presenter.get_actor_class_name(self.actor)
        size = self.presenter.get_actor_size(self.actor)
        type_subtype = self.presenter.get_actor_type_subtype(self.actor)
        alignment = self.presenter.get_actor_alignment(self.actor)
        armor_class = self.presenter.get_actor_armor_class(self.actor)
        # hp = self.presenter.get_actor_hp(self.actor)
        hp = "10"
        speed = self.presenter.get_actor_speed(self.actor)
        saving_throws = self.presenter.get_actor_save_throws(self.actor)
        immunities = self.presenter.get_actor_immunities(self.actor)
        resistances = self.presenter.get_actor_resistances(self.actor)
        senses = self.presenter.get_actor_senses(self.actor)
        languages = self.presenter.get_actor_languages(self.actor)

        self.hp_val.set(hp)
        sep = ", "
        saving_throws_str = sep.join(saving_throws)
        immunities_str = sep.join(immunities)
        resistances_str = sep.join(resistances)
        senses_str = sep.join(senses)
        languages_str = sep.join(languages)

        actor_name_label = Label(self, text=self.actor)
        actor_name_label.pack()
        class_name_label = Label(self, text=class_name)
        class_name_label.pack()
        size_alignment_label = Label(self, text=(size + " " + type_subtype + ", " + alignment).capitalize())
        size_alignment_label.pack()
        ac_label = Label(self, text="Armor Class " + armor_class)
        ac_label.pack()
        hp_label = Label(self, text="Hit Points")
        hp_label.pack()
        self.hp_entry = Entry(self, textvariable=self.hp_val)
        self.hp_entry.pack()
        speed_label = Label(self, text=speed.capitalize())
        speed_label.pack()
        self.pack_table(headers=["STR", "DEX", "CON", "INT", "WIS", "CHA"],
                        values=[self.presenter.get_stat_block_with_mods(self.actor)])
        save_label = Label(self, text="Saving throws: " + saving_throws_str)
        save_label.pack()
        damage_immunity_label = Label(self, text="Damage Immunities: " + immunities_str)
        damage_immunity_label.pack()
        damage_resistance_label = Label(self, text="Damage Resistances: " + resistances_str)
        damage_resistance_label.pack()
        senses_label = Label(self, text="Senses: " + senses_str)
        senses_label.pack()
        language_label = Label(self, text="Languages: " + languages_str)
        language_label.pack()
        special_abilities = self.presenter.get_actor_special_abilities(self.actor)
        for ability in special_abilities:
            temp_label = Label(self, text=ability)
            temp_label.pack()
        action_label = Label(self, text="Actions")
        action_label.pack()
        actions = self.presenter.get_actor_actions(self.actor)
        for action in actions:
            temp_label = Label(self, text=action)
            temp_label.pack()
        l_action_label = Label(self, text="Legendary Actions")
        l_action_label.pack()
        l_actions = self.presenter.get_actor_legendary_actions(self.actor)
        for action in l_actions:
            temp_label = Label(self, text=action)
            temp_label.pack()
        update_button = Button(self, text="Update HP", command=self.update_actor_stats)
        update_button.pack()

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

    def update_actor_stats(self):
        try:
            hp = int(self.hp_entry.get())
            self.presenter.update_actor_hp(self.actor, hp)
        except ValueError:
            # do nothing because the value was not a string TODO: Maybe error popup?
            dummy = 10


root = tk.Tk()
root.geometry("300x400")
style = Style()
style.theme_use('clam')
underline_label_font = get_font(tk.Label(None), ["underline"], ["true"])
style.configure("UNDERLINE.TLabel", font=underline_label_font)
app = ActorDetailView("Test", root)
root.mainloop()
