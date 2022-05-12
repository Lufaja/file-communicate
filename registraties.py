import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter.messagebox import showinfo
import os.path, os, yaml


window = tk.Tk()
window.title('Overzicht')
window.geometry('550x227')
window.resizable(False, False)
path = os.path.dirname(os.path.abspath(__file__))

# define columns
columns = ('file', 'creation')   

tree = ttk.Treeview(window, columns=columns, show='headings')

# define headings
tree.heading('file', text='Bestand')
tree.heading('creation', text='Achternaam')

def getData():
    with open(path + "/databron/data.yml", "r") as file:
        files = yaml.full_load(file)
    contacts = []
    for x in files:
        a = files[x]["naam"]
        b = files[x]["aanmaak"]
        contacts.append((f'{a}', f'{b}'))

    # add data to the treeview
    for contact in contacts:
        tree.insert('', tk.END, values=contact)

    return b, x

def refresh():
    for item in tree.get_children():
        tree.delete(item)
    date, amount = getData()
    date = "Meest recent:\n" + str(date)
    amount = "Aantal:\n" + str(amount)
    amountL.config(text=amount)
    dateL.config(text=date)


date, amount = getData()
date = "Meest recent:\n" + str(date)
amount = "Aantal:\n" + str(amount)
button = tkinter.Button(
    window,
    command=refresh,
    text="refresh"
)

amountL = tkinter.Label(
    window,
    text= amount
)

dateL = tkinter.Label(
    window,
    text=date
)

button.grid(row=2, column=2)
amountL.grid(row=0, column=2)
dateL.grid(row=1, column=2)
tree.grid(row=0, column=0, sticky='nsew', rowspan=3)

scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

window.mainloop()