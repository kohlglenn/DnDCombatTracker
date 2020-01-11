from tkinter import *
from tkinter.ttk import *
from presenter.GamePresenter import GamePresenter
from ui.views.IView import IView


class CreatePlayerView(IView, Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        if master is not None and hasattr(master, "presenter"):
            self.presenter = master.presenter
        else:
            self.presenter = GamePresenter()
        self.master = master
        self.row_end = 1
        self.player_name_entries = []
        self.player_class_entries = []
        self.submit_all_button = None
        self.add_player_button = None
        self.init_window()

    def init_window(self):
        self.master.title("Add Players")
        self.grid()

        name_label = Label(self, text="Player Name(s)")
        name_label.grid(row=0, column=0)

        class_label = Label(self, text="Player Class(es)")
        class_label.grid(row=0, column=1)

        self.submit_all_button = Button(self, text="Submit", command=self.send_data)
        self.add_player_button = Button(self, text="Add Player", command=self.add_player_row)

        self.add_player_row()

    def add_player_row(self):
        row = self.row_end
        name_entry = Entry(self)
        name_entry.grid(row=row, column=0)
        self.player_name_entries.append(name_entry)

        class_entry = Combobox(self, values=self.presenter.get_player_classes())
        class_entry.grid(row=row, column=1)
        self.player_class_entries.append(class_entry)

        row += 1

        self.add_player_button.grid(row=row, column=0)
        self.submit_all_button.grid(row=row, column=1)

        self.row_end = row

    def send_data(self):
        data_dict = dict()
        for idx in range(0, len(self.player_name_entries)):
            player_dict = dict()
            player_dict["name"] = self.player_name_entries[idx].get()
            player_dict["class"] = self.player_class_entries[idx].get()
        self.presenter.add_players_from_view(data_dict)

    def update(self, **kwargs):
        pass
