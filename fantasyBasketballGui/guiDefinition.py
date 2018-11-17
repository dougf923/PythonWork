from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(month.get())
        
        if value == 1:
            meters.set("Jan");
        elif value == 2:
            meters.set("Feb");
        else:
            meters.set("fuck");
    except ValueError:
        pass
    
def setday(*args):
    value = day.get()
    
#    if value == 1:
#        daylabel.set("1")
#    elif value == 2:
#        daylabel.set("2")
#    else:
#        daylabel.set("fuck")
    daylabel.set(str(value))   
    
root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

month = IntVar()
day = IntVar()
meters = StringVar()
daylabel = StringVar()


#feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
month_entry = ttk.Menubutton(mainframe, width=7, textvariable = meters)#text = "Month") #, textvariable=feet)
monthMenu = Menu(month_entry)
monthMenu.add_radiobutton(label="Jan", var=month, value=1, command = calculate)
monthMenu.add_radiobutton(label="Feb", var=month, value=2, command = calculate)
month_entry.config(menu=monthMenu)
month_entry.grid(column=2, row=1, sticky=(W, E))

day_entry = ttk.Menubutton(mainframe, width=7, textvariable = daylabel) #, textvariable=feet)
dayMenu = Menu(day_entry)
dayMenu.add_radiobutton(label="1", var=day, value=1, command = setday)
dayMenu.add_radiobutton(label="2", var=day, value=2, command = setday)
day_entry.config(menu=dayMenu)
day_entry.grid(column=3, row=1, sticky=(W, E))

#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
#ttk.Label(mainframe, textvariable=daylabel).grid(column=3, row=2, sticky=(W, E))
#ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Start Date: ").grid(column=1, row=1, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

month_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()