import tkinter as tk
from tkinter import ttk


class AboutFile:
    def set_about_frame(self, file):
        for i in self.winfo_children():
            i.destroy()

        self.about_frame = ttk.Frame(self)
        self.about_frame.pack(fill=tk.BOTH, expand=True)

        self.butt_back = ttk.Button(self.about_frame, width=5, text="<\n<\n<",
                                          command=self.update_ui)
        self.butt_back.pack(side=tk.LEFT, fill=tk.Y)

        self.info_frame = ttk.LabelFrame(self.about_frame, text=f'{file}')
        self.info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
