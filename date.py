import tkinter
import calendar
from tkinter import ttk
import datetime
class datum(ttk.Frame):
    dag = 0
    maand = 0
    jaar = 0
    def __init__(self, window):
        super().__init__(window)
        self.day_selected = tkinter.StringVar()
        # day_cb = ttk.Combobox, textvariable=self.day_selected)
        # day_cb.pack()
        self.months = list(calendar.month_name)
        self.months.pop(0)

        #diffrence calculator
            
        self.list1 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']

        self.days1 = []
        for z in range(1,32):
            self.days1.append(z)

        self.days2 = []
        for z in range(1,31):
            self.days2.append(z)

        self.days3 = []
        for z in range(1,30):
            self.days3.append(z)

        self.days4 = []
        for z in range(1,29):
            self.days4.append(z)



        self.Combo = ttk.Combobox(self, values = self.months, state='readonly')
        self.Combo.set("Kies een maand")
        self.Combo.pack(pady = 5)

        self.Combo2 = ttk.Combobox(self, values = self.days1, state='readonly', textvariable=self.day_selected)
        self.Combo2.set("Kies een dag")
        self.Combo2.pack(pady = 5)

        self.v = tkinter.StringVar()

        self.yearEntry = ttk.Entry(self, textvariable=self.v)
        self.yearEntry.configure(width= 23)
        self.yearEntry.pack(pady = 5)
        self.v.set("2000")
    


    def check(self):
        #checks the amount of days the month should have
        def retrieve(event):
            try:
                year = int(self.yearEntry.get())
            except:
                year = self.yearEntry.get()
                numeric_filter = filter(str.isdigit, year)
                numeric_string = "".join(numeric_filter)
                self.v.set(numeric_string)
            if '' == self.yearEntry.get():
                year = 0
            else:
                year = self.yearEntry.get()
                year = int(year[0:4])
                self.v.set(year)
            leapYear = False
            if year % 400 == 0 or  year % 100 != 0 and year % 4 == 0:
                leapYear = True
            y = 1
            for x in range(7):
                if self.Combo.get() == self.list1[x]:
                    self.Combo2["values"] = (self.days1)
                    break
                else:
                    self.Combo2["values"] = (self.days2)
                    if self.day_selected.get() == "31":
                        self.day_selected.set("30")
            if self.Combo.get() == "February" and leapYear == True:
                self.Combo2["values"] = (self.days3)
                if self.day_selected.get() == 'Kies een dag':
                    pass
                elif int(self.day_selected.get()) >= 30:
                    self.day_selected.set("29x")
            elif self.Combo.get() == "February":
                self.Combo2["values"] = (self.days4)
                if self.day_selected.get() == 'Kies een dag':
                    pass
                elif int(self.day_selected.get()) >= 29:
                    self.day_selected.set("28")
        self.Combo.bind("<<ComboboxSelected>>",retrieve)
        self.yearEntry.bind("<KeyRelease>", retrieve)
    
    def getDatum(self):
        ingevuld = datetime.date(int(self.yearEntry.get()), int(self.months.index(self.Combo.get()))+1, int(self.Combo2.get()))
        return ingevuld
    
    def leeftijd(self):
        if self.Combo.get() == "Kies een maand" or self.day_selected.get() == "Kies een dag":
            if self.Combo.get() == "Kies een maand":
                self.Combo.configure(foreground="red")
                self.Combo.after(5000, lambda: self.Combo.configure(foreground="black"))
            if self.Combo2.get() == "Kies een dag":
                self.Combo2.configure(foreground="red")
                self.Combo2.after(5000, lambda: self.Combo2.configure(foreground="black"))
            return False
        verjaardag = self.getDatum()
        today = datetime.date.today()
        age = today.year - verjaardag.year - ((today.month, today.day) < (verjaardag.month, verjaardag.day))
        return age