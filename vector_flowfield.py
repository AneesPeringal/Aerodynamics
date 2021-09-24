import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


import numpy as np


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig, ax = plt.subplots()

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_press(event):
    print('you pressed', event.button, event.xdata, event.ydata)

fig.canvas.mpl_connect('button_press_event', on_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

#class flow:
#    def __init__(self, flow_number =0):
#        self.flow_number = flow_number
#class uniform(flow):
#    def __init__(self, flow_number, direction=np.array([1,0]), speed =1):
#        flow.__init__(self,flow_number)
#        self.direction = direction
#        self.speed = speed
    
#class source(flow):
#    def __init__(self, flow_number, position = np.array([0,0]), strength =1):
#       flow.__init__(self,flow_number)
#       self.position = position
#       self.strength = strength
def add_uniform():
    pass
#    uniform
def add_source():
    pass

button = tkinter.Button(master=root, text="Quit", command=_quit)
uniform_button = tkinter.Button(master=root, text = "Uniform Flow", command =add_uniform)
source_button = tkinter.Button(master = root, text = "source flow", command =add_source)
button.pack(side=tkinter.LEFT)
uniform_button.pack(side = tkinter.LEFT)
source_button.pack(side = tkinter.LEFT)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
