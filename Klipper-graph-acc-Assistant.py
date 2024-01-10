# Simple GUI for Klipper graph_accelometer.
# Made by MagicFly
import os.path
from tkinter import *
from tkinter import filedialog
# import graph_accelerometer
import graph_belts
import matplotlib
import matplotlib.ticker
import matplotlib.pyplot, matplotlib.dates, matplotlib.font_manager
from sys import exit

# Use TkAgg backend
matplotlib.rcParams.update({'figure.autolayout': True})
matplotlib.use('TkAgg')

def browse_file_1():
    filename_1 = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(
            ("CSV files", "*.csv*"),
            ("all files", "*.*")
        )
    )
    # Change label contents
    label_file_explorer_1.configure(text="File Opened: " + filename_1)

def browse_file_2():
    filename_2 = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(
            ("CSV files", "*.csv*"),
            ("all files", "*.*")
        )
    )
    # Change label contents
    label_file_explorer_2.configure(text="File Opened: " + filename_2)

def run_plot():
    lognames = [label_file_explorer_1.cget("text").split(": ")[1],label_file_explorer_2.cget("text").split(": ")[1]]
#    max_freq = 200
    fig = graph_belts.belts_calibration(lognames,"~/klipper",200.,False,8,4.8)
    fig.tight_layout()
    fig.show()

def _exit():
    exit()


# GUI root window
window = Tk()
window.title("Belt tensioning procedure Assistant by MagicFly")
# Labels and buttons
label_file_explorer_1 = Label(
    window,
    text="File Opened: raw_data_axis=1.000,-1.000_a.csv",
    width=100,
    height=4,
    fg="blue"
)
label_file_explorer_2 = Label(
    window,
    text="File Opened: raw_data_axis=1.000,1.000_b.csv",
    width=100,
    height=4,
    fg="blue"
)

button_explore_1 = Button(window, text="Select CSV File", command=browse_file_1)
button_explore_2 = Button(window, text="Select CSV File", command=browse_file_2)
button_exit = Button(window, text="Exit", command=_exit)
button_run = Button(
    window,
    text="Run",
    #    command=lambda: run_graph(['raw_data_axis=1.000,-1.000_a.csv','raw_data_axis=1.000,1.000_b.csv'])
    command=lambda: run_plot()
)

# Grid
label_file_explorer_1.grid(column=1, row=1)
button_explore_1.grid(column=1, row=2)
label_file_explorer_2.grid(column=1, row=3)
button_explore_2.grid(column=1, row=4)
button_run.grid(column=1, row=5)
button_exit.grid(column=1, row=6)
# Drive it like you stole it
window.mainloop()
