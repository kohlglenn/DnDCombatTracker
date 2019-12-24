from tkinter import *
from tkinter.ttk import *
from presenter.GamePresenter import GamePresenter
from ui.views.IView import IView


class CreateNpcView(IView, Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        if master is not None and hasattr(master, "presenter"):
            self.presenter = master.presenter
        else:
            self.presenter = GamePresenter()
        self.master = master
        self.row_end = 1
        self.npc_name_entries = []
        self.npc_class_entries = []
        self.submit_all_button = None
        self.add_npc_button = None
        self.init_window()

    def init_window(self):
        self.master.title("Add NPCs")
        self.grid()

        name_label = Label(self, text="NPC Name(s)")
        name_label.grid(row=0, column=0)

        class_label = Label(self, text="NPC Class(es)")
        class_label.grid(row=0, column=1)

        self.submit_all_button = Button(self, text="Submit", command=self.send_data)
        self.add_npc_button = Button(self, text="Add NPC", command=self.add_npc_row)

        self.add_npc_row()

    def add_npc_row(self):
        row = self.row_end
        name_entry = Entry(self)
        name_entry.grid(row=row, column=0)
        self.npc_name_entries.append(name_entry)

        class_entry = Combobox(self, values=self.presenter.get_npc_classes())
        class_entry.grid(row=row, column=1)
        self.npc_class_entries.append(class_entry)

        row += 1

        self.add_npc_button.grid(row=row, column=0)
        self.submit_all_button.grid(row=row, column=1)

        self.row_end = row

    def send_data(self):
        data_dict = dict()
        for idx in range(0, len(self.npc_name_entries)):
            npc_dict = dict()
            npc_dict["name"] = self.npc_name_entries[idx].get()
            npc_dict["class"] = self.npc_class_entries[idx].get()
            data_dict[idx] = npc_dict
        self.presenter.add_npcs_from_view(data_dict)

    def update(self, **kwargs):
        pass


root = Tk()
style = Style()
style.theme_use('clam')
app = CreateNpcView(root)
root.mainloop()
