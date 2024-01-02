# Simple GUI for Klipper graph_accelometer.
# Made by MagicFly
import os.path
from tkinter import *
from tkinter import filedialog
import graph_accelerometer
import matplotlib
import matplotlib.ticker
import matplotlib.pyplot, matplotlib.dates, matplotlib.font_manager

# Use TkAgg backend
matplotlib.rcParams.update({'figure.autolayout': True})
matplotlib.use('TkAgg')

def run_graph(filename):
    max_freq = 200
    #args = [f'{filename}']
    datas = [graph_accelerometer.parse_log(fn,None) for fn in filename]
    fig = graph_accelerometer.plot_compare_frequency(datas, filename, max_freq, 'all')
    fig.tight_layout()
    fig.show()

def _exit():
    exit()


# GUI root window
window = Tk()
window.title("Belt tensioning procedure Assistant by MagicFly")

label_file_explorer = Label(
    window,
    text="Run Belt tensioning procedure",
    width=100,
    height=4,
    fg="blue"
)
button_exit = Button(window, text="Exit", command=_exit)
button_run = Button(
    window,
    text="Run",
    command=lambda: run_graph(['raw_data_axis=1.000,-1.000_a.csv','raw_data_axis=1.000,1.000_b.csv'])
)

# Grid
label_file_explorer.grid(column=1, row=1)
button_run.grid(column=1, row=2)
button_exit.grid(column=1, row=3)
# Drive it like you stole it
window.mainloop()
