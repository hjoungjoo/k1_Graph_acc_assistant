# Simple GUI for Klipper graph_accelometer.
# Made by MagicFly
import os.path
from tkinter import *
from tkinter import filedialog
import calibrate_input_shaper
import graph_belts
import matplotlib
import matplotlib.ticker
import matplotlib.pyplot, matplotlib.dates, matplotlib.font_manager
from sys import exit

# Use TkAgg backend
matplotlib.rcParams.update({'figure.autolayout': True})
matplotlib.use('TkAgg')

def browse_file(label_file_explorer):
    filename = filedialog.askopenfilename(
        initialdir=os.path.abspath(__file__),#"/",
        title="Select a File",
        filetypes=(
            ("CSV files", "*.csv*"),
            ("all files", "*.*")
        )
    )
    # Change label contents
    if filename != "":
        label_file_explorer.configure(text="File Opened: " + filename)

def run_belt_plot():
    lognames = [label_file_explorer_1.cget("text").split(": ")[1],label_file_explorer_2.cget("text").split(": ")[1]]
    if os.path.basename(lognames[0]).find("raw_data_axis") == 0 and os.path.basename(lognames[1]).find("raw_data_axis") == 0:
        fig = graph_belts.belts_calibration(lognames,"~/klipper",200.,False,8,4.8)
        fig.tight_layout()
        fig.show()

def run_shaper(filename):
    max_freq = 200
    # Parse data
    args = [f'{filename}']
    datas = [calibrate_input_shaper.parse_log(fn) for fn in args]
    # Calibrate shaper and generate outputs
    selected_shaper, shapers, calibration_data = calibrate_input_shaper.calibrate_shaper(datas, None, None)
    # Draw graph
    calibrate_input_shaper.setup_matplotlib(None)
    fig = calibrate_input_shaper.plot_freq_response(args, calibration_data, shapers, selected_shaper, max_freq)
    fig.tight_layout()
    fig.show()
    # matplotlib.pyplot.show()

def run_input_plot():
    lognames = [label_file_explorer_1.cget("text").split(": ")[1],label_file_explorer_2.cget("text").split(": ")[1]]
    if os.path.basename(lognames[0]).find("calibration") == 0:
        run_shaper(lognames[0])
    if os.path.basename(lognames[1]).find("calibration") == 0:
        run_shaper(lognames[1])

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
    height=2,
    fg="blue"
)
label_file_explorer_2 = Label(
    window,
    text="File Opened: raw_data_axis=1.000,1.000_b.csv",
    width=100,
    height=2,
    fg="blue"
)

button_explore_1 = Button(window, text="Select CSV File", command=lambda:browse_file(label_file_explorer_1))
button_explore_2 = Button(window, text="Select CSV File", command=lambda:browse_file(label_file_explorer_2))
button_exit = Button(window, text="Exit", command=_exit)
button_input_run = Button(window, text="Input shaper graphs Run", command=lambda: run_input_plot())
button_belt_run = Button(window, text="Belt tension graphs Run", command=lambda: run_belt_plot())

# Grid
label_file_explorer_1.grid(column=1, row=1)
button_explore_1.grid(column=2, row=1)
label_file_explorer_2.grid(column=1, row=2)
button_explore_2.grid(column=2, row=2)
button_input_run.grid(column=1, row=3)
button_belt_run.grid(column=1, row=4)
button_exit.grid(column=1, row=6)
# Drive it like you stole it
window.mainloop()
