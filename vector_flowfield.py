import tkinter
from tkinter import *

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np


X, Y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
U = 0
V = 0

fig, ax = plt.subplots(1,1)
Q = ax.quiver(X, Y, U, V, pivot='mid', color='r', units='meters')

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root) 
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

global flows
flows = []

##defining all the flows as classes
class Uniform:
    flow_type = "Uniform"
    def __init__(self, x_direction,y_direction):
        self.x_direction = x_direction
        self.y_direction = y_direction
        
        
        
class Source:
    flow_type = "Source"
    def __init__(self, strength, x_pos, y_pos):
        self.sterngth = strength
        self.x_pos = x_pos
        self.y_pos = y_pos

def animate(Q,X,Y):
    U = 0
    V = 0
    for i in flows:
        U = U + int(i.x_direction)
        V = V + int(i.y_direction)
    Q.set_UVC(U,V)
    
def on_press(event):
    print('you pressed', event.button, event.xdata, event.ydata)

fig.canvas.mpl_connect('button_press_event', on_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

def add_uniform():
    top = Tk()
    L1 = Label(top, text="x direcion of the uniform flow")
    L1.grid(row = 0,column = 0)
    x_uniform = Entry(top, bd =5)
    x_uniform.grid(row = 0,column = 1)
    L2 = Label(top, text="y direcion of the uniform flow")
    L2.grid(row = 1,column = 0)
    y_uniform = Entry(top, bd =5)
    y_uniform.grid(row = 1,column = 1)
    
    
    def close_window (): 
        a = Uniform(x_uniform.get(), y_uniform.get())
        flows.append(a)
        top.destroy()
    button = Button (top, text = "Okay", command = close_window)
    button.grid(row = 2, column = 1)
    
    #    uniform
def add_source():
    top = Tk()
    L1 = Label(top, text="strength of the uniform flow")
    L1.grid(row = 0,column = 0)
    x_uniform = Entry(top, bd =5)
    x_uniform.grid(row = 0,column = 1)
    L2 = Label(top, text="2sdaf")
    L2.grid(row = 1,column = 0)
    y_uniform = Entry(top, bd =5)
    y_uniform.grid(row = 1,column = 1)
    
    
    def close_window (): 
        print(x_uniform.get(), y_uniform.get())
        top.destroy()
    button = Button(top, text = "Okay", command = close_window)
    button.grid(row = 2, column = 1)
    


    

button = tkinter.Button(master=root, text="Quit", command=_quit)
uniform_button = tkinter.Button(master=root, text = "Uniform Flow", command =add_uniform)
source_button = tkinter.Button(master = root, text = "source flow", command =add_source)
button.pack(side=tkinter.LEFT)
uniform_button.pack(side = tkinter.LEFT)
source_button.pack(side = tkinter.LEFT)
animate = animation.FuncAnimation(fig, animate,fargs = (X,Y), interval =50,blit = False)
tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.

##defining all the flows as classes
class Uniform:
    flow_type = "Uniform"
    def __init__(self, x_direction,y_direction):
        self.x_direction = x_direction
        self.y_direction = y_direction
        
        
        
class Source:
    flow_type = "Source"
    def __init__(self, strength, x_pos, y_pos):
        self.sterngth = strength
        self.x_pos = x_pos
        self.y_pos = y_pos

    
