import tkinter as tk
from tkinter import ttk
from format import ConfigureBar
from about_file import AboutFile


class Application(tk.Tk, ConfigureBar, AboutFile):
    def __init__(self):
        tk.Tk.__init__(self)
        self.path_work = 'D:\Work\\'
        self.path_process = self.path_work + 'Process\\'
        self.path_ready = self.path_work + 'Ready\\'

        self.file_statuses = {}

        self.update_ui()

    def set_ui(self):
        self.geometry('1000x500')
        self.minsize(800, 400)

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.make_bar()


if __name__ == '__main__':
    root = Application()
    root.mainloop()
    
