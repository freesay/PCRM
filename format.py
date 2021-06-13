import tkinter as tk
from tkinter import ttk
import os
import shutil


class ConfigureBar:
    def fill_folders(self):
        self.three = os.walk('D:\Work')
        self.folders = []

        for i in self.three:
            self.folders.append(i)

        # self.wheel = self.after(5000, self.fill_folders)
        print(self.folders)

    def change_status(self, file_name, status):
        self.current_path = self.path_work + status + '\\'
        self.name = file_name

        self.style = ttk.Style()

        if status == 'Process':
            if self.file_statuses[self.name] == 'Work':
                shutil.move(self.path_work + self.name, self.current_path + self.name)
            if self.file_statuses[self.name] == 'Ready':
                shutil.move(self.path_ready + self.name, self.current_path + self.name)
            self.file_statuses[self.name] = status
            self.style.configure('Name.TLabel', foreground='blue')

        if status == 'Ready':
            if self.file_statuses[self.name] == 'Work':
                shutil.move(self.path_work + self.name, self.current_path + self.name)
            if self.file_statuses[self.name] == 'Process':
                shutil.move(self.path_process + self.name, self.current_path + self.name)
            self.file_statuses[self.name] = status
            self.style.configure('Name.TLabel', foreground='green')

        print(file_name, status)
        self.update_ui()

    def make_bar(self):

        for address, dirs, files in self.folders:
            for file in files:
                if file in os.listdir(self.path_work):
                    self.file_statuses[file] = 'Work'

                if file in os.listdir(self.path_process):
                    self.file_statuses[file] = 'Process'

                if file in os.listdir(self.path_ready):
                    self.file_statuses[file] = 'Ready'

                self.bar_work = ttk.LabelFrame(self.main_frame, text=f'{address}')
                self.bar_work.pack(fill=tk.X, padx=5, pady=5)

                self.butt_more = ttk.Button(self.bar_work, text='>>>',
                                            command=lambda file=file: self.set_about_frame(file))
                self.butt_more.pack(side=tk.LEFT, padx=5, pady=10)

                self.butt_ready = ttk.Button(self.bar_work, text='Ready',
                                             command=lambda file_name=file,
                                                            status='Ready': self.change_status(file_name, status))
                self.butt_ready.pack(side=tk.RIGHT, padx=5, pady=10)

                self.butt_process = ttk.Button(self.bar_work, text='Process',
                                               command=lambda file_name=file,
                                                              status='Process': self.change_status(file_name, status))
                self.butt_process.pack(side=tk.RIGHT, padx=5, pady=10)

                self.butt_wait = ttk.Button(self.bar_work, text='ALARM!')
                self.butt_wait.pack(side=tk.RIGHT, padx=5, pady=10)

                self.label_file_name = ttk.Label(self.bar_work, text=f'{file}', style='Name.TLabel').pack(side=tk.LEFT, padx=20)
                self.label_time = ttk.Label(self.bar_work, text='Date').pack(side=tk.RIGHT, padx=20)
                self.sep = ttk.Separator(self.bar_work, orient='vertical').pack(side=tk.RIGHT, fill=tk.Y, padx=4, pady=4)
                self.label_creator_name = ttk.Label(self.bar_work, text='Creator').pack(side=tk.RIGHT, padx=20)

    def update_ui(self):
        for i in self.winfo_children():
            i.destroy()

        self.fill_folders()
        self.set_ui()
