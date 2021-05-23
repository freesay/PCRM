"""
FIX IT NAHOOI

Классы. В первую очередь.
Что за херня с обновлением списка файлов? Разобрать.
База данных. Пора уже.
"""


import os
import shutil
from tkinter import *

window = Tk()

three = os.walk('D:\Work')

path_work = "D:\Work\\"
path_process = path_work + 'Process\\'
path_ready = path_work + 'Ready\\'

status_wait = 'blue'
status_ready = 'green'
status_process = 'yellow'
status_alarm = 'red'


def change_status(file_name, status):
    current_path = path_work + status + '\\'
    name = file_name.cget('text')

    if status == 'Process':
        if file_statuses[name] == 'Work':
            shutil.move(path_work + name, current_path + name)
        if file_statuses[name] == 'Ready':
            shutil.move(path_ready + name, current_path + name)
        file_statuses[name] = status
        file_name.config(bg=status_process)
    if status == 'Ready':
        if file_statuses[name] == 'Work':
            shutil.move(path_work + name, current_path + name)
        if file_statuses[name] == 'Process':
            shutil.move(path_process + name, current_path + name)
        file_statuses[name] = status
        file_name.config(bg=status_ready)
    window.update_idletasks()


def show_files():
    i = 0
    for address, dirs, files in folders:
        if files:
            frame = LabelFrame(window, text=f'{address}')
            frame.grid()
            frame.update_idletasks()
            for file in files:
                file_name = Label(frame, text=file)
                file_name.grid(row=i, column=0)

                if file in os.listdir(path_work):
                    file_name.config(bg=status_wait)
                    file_statuses[file] = 'Work'

                if file in os.listdir(path_process):
                    file_name.config(bg=status_process)
                    file_statuses[file] = 'Process'

                if file in os.listdir(path_ready):
                    file_name.config(bg=status_ready)
                    file_statuses[file] = 'Ready'

                btn_alarm = Button(frame, text='Alarm',
                                   command=lambda file_name=file_name,
                                                  status='Alarm': change_status(file_name, status))
                btn_alarm.grid(row=i, column=1)

                btn_process = Button(frame, text='Process',
                                     command=lambda file_name=file_name,
                                                    status='Process': change_status(file_name, status))
                btn_process.grid(row=i, column=2)

                btn_ready = Button(frame, text='Ready',
                                   command=lambda file_name=file_name,
                                                  status='Ready': change_status(file_name, status))
                btn_ready.grid(row=i, column=3)
                i += 1

    window.after(5000, show_files)
    print('work', file_statuses, len(file_statuses))
    print(folders)


file_statuses = {}
folders = []
for el in three:
    folders.append(el)


if __name__ == '__main__':
    show_files()
    window.mainloop()
