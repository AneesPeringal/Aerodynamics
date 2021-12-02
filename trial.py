## we will try to do the project using the pyplot widgets as the gui interface

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets import Button


fig, ax = plt.subplots()

class Uniform:
    flow_type = "uniform"
    def __init__(self, x_direction, y_direction):
        self.x_velocity = np.full((100,100),x_direction)
        self.y_velocity = np.full((100,100),y_direction)
        
class Source:
    flow_type = "source"
    def __init__(self, x_pos, y_pos, strength):
        w = 9
        Y, X = np.mgrid[-w:w:100j, -w:w:100j]
        self.x_pos = np.full((100,100),x_pos)
        self.y_pos = np.full((100,100),y_pos)
        self.strength = int(strength)
        V =self.strength*(Y - self.y_pos)/(2*np.pi*((Y - self.y_pos)**2 + (X - self.x_pos)**2))
        U =self.strength*(X - self.x_pos)/(2*np.pi*((Y - self.y_pos)**2 + (X - self.x_pos)**2))
        self.y_velocity = np.where(V !=np.inf, V, 0)
        self.x_velocity = np.where(U !=np.inf, U, 0)

        
class Vortex:
    flow_type = "vortex"
    def __init__(self, x_pos, y_pos, strength):
        w = 9
        Y, X = np.mgrid[-w:w:100j, -w:w:100j]
        self.x_pos = int(x_pos)
        self.y_pos = int(y_pos)
        self.strength = int(strength)
        V = self.strength*(X - self.x_pos)/(2*np.pi*((Y - self.y_pos)**2 + (X - self.x_pos)**2))
        U = -self.strength*(Y - self.y_pos)/(2*np.pi*((Y - self.y_pos)**2 + (X - self.x_pos)**2))
        self.y_velocity = np.where(V !=np.inf, V, 0)
        self.x_velocity = np.where(U !=np.inf, U, 0)

        
class Index:
    ind =0
    def uniform(self,event):
        add_unifrom()
    def source(self,event):
        add_source()
    def vortex(self,event):
        add_vortex()


def add_uniform():
    popup = Tk()
    popup.title("uniform flow definition")
    L1 = Label(popup, text="x direcion of the uniform flow")
    L1.grid(row = 0,column = 0)
    x_uniform = Entry(popup, bd =5)
    x_uniform.grid(row = 0,column = 1)
    L2 = Label(popup, text="y direcion of the uniform flow")
    L2.grid(row = 1,column = 0)
    y_uniform = Entry(popup, bd =5)
    y_uniform.grid(row = 1,column = 1)        
    def close_window ():
        plt.clf()
        plt.cla()
        plot1.clear()
        global flows
        a = Uniform(int(x_uniform.get()),int(y_uniform.get()))
        flows.append(a)
        print(x_uniform.get(), y_uniform.get())
        refresh()
        popup.destroy()
    button = Button(popup, text = "Okay", command = close_window)
    button.grid(row = 2, column = 1)
