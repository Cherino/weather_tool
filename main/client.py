import tkinter as tk
import weatherlib as wl
from weatherlib import APIHandler

# --- GUI Functions ---
def newrep_dash():
    repdash = tk.Toplevel(root)
    repdash.title("WAT - New Report Dashboard")
    repdash.geometry("350x400")
    repdash.resizable(False,False)
    repdashtitle = tk.Label(repdash, text="Weather Analysis Tool WAT - Main Menu Selection")
    repdashtitle.place(x=10,y=10)

    citylabels = tk.Label(repdash, text="Please enter a City or two to compare:")
    citylabels.place(x=20,y=50)
    city1 = tk.Entry(repdash, width=20)
    city1.place(x=50,y=80)
    city2 = tk.Entry(repdash, width=20)
    city2.place(x=50,y=100)

    datelabels = tk.Label(repdash, text="Please enter a Date in (YYYY-MM-DD) format please:")
    datelabels.place(x=20,y=130)
    dateinput = tk.Entry(repdash, width=20)
    dateinput.place(x=50,y=160)


    submitdata = tk.Button(repdash, text="Submit Data")


# --- Main GUI Loop ---
root = tk.Tk()
root.title("WAT - Main Menu")
root.geometry("330x300")
root.resizable(False,False)

roottitle = tk.Label(root, text="Weather Analysis Tool WAT - Main Menu Selection")
roottitle.place(x=10,y=10)

repbutton = tk.Button(root, text="New Report", command=newrep_dash)
repbutton.place(x=115,y=50)

root.mainloop()