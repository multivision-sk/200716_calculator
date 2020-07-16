from tkinter import *
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


#GUI



class Calculator:
    def input_value(self,val) :
        self.entry_value.insert('end',val)

    def clear_all(self):
        self.entry_value.delete(0,'end')

    def get_result(self):
        return_value = eval(self.entry_value.get())

        self.entry_value.delete(0,'end')
        self.entry_value.insert(0,return_value)


    def __init__(self,main):


        main.title('calculator1')
        main.geometry()

        #input section
        self.entry_value = Entry(main, width=40, justify=RIGHT)
        self.entry_value.grid(row=0, column=0, columnspan=3)
        self.entry_value.focus_set()

        #generating button
        Button(main,text="=",width=20,command=lambda : self.get_result()).grid(row=5,column=2,columnspan=2)
        Button(main,text="AC",width=10,command=lambda : self.clear_all()).grid(row=4,column=0)
        Button(main,text="+",width=10,command=lambda :self.input_value('+')).grid(row=1,column=3)
        Button(main,text="-",width=10,command=lambda :self.input_value('-')).grid(row=2,column=3)
        Button(main,text="x",width=10,command=lambda :self.input_value('*')).grid(row=3,column=3)
        Button(main,text="/",width=10,command=lambda :self.input_value('/')).grid(row=4,column=2)
        Button(main,text="(",width=10,command=lambda :self.input_value('(')).grid(row=5,column=0)
        Button(main,text=")",width=10,command=lambda :self.input_value(')')).grid(row=5,column=1)
        Button(main,text="7",width=10,command=lambda :self.input_value(7)).grid(row=1,column=0)
        Button(main,text="8",width=10,command=lambda :self.input_value(8)).grid(row=1,column=1)
        Button(main,text="9",width=10,command=lambda :self.input_value(9)).grid(row=1,column=2)
        Button(main,text="4",width=10,command=lambda :self.input_value(4)).grid(row=2,column=0)
        Button(main,text="5",width=10,command=lambda :self.input_value(5)).grid(row=2,column=1)
        Button(main,text="6",width=10,command=lambda :self.input_value(6)).grid(row=2,column=2)
        Button(main,text="1",width=10,command=lambda :self.input_value(1)).grid(row=3,column=0)
        Button(main,text="2",width=10,command=lambda :self.input_value(2)).grid(row=3,column=1)
        Button(main,text="3",width=10,command=lambda :self.input_value(3)).grid(row=3,column=2)
        Button(main,text="0",width=10,command=lambda :self.input_value(0)).grid(row=4,column=1)



#연산 추가

class Calculator_upgrade(Calculator):
    def get_sqrt(self):
        return_value = eval(self.entry_value.get())

        calc_value = math.sqrt(return_value)
        self.entry_value.delete(0,'end')
        self.entry_value.insert(0,calc_value)

    def get_power(self):
        return_value = eval(self.entry_value.get())

        calc_value = math.pow(return_value,2)
        self.entry_value.delete(0,'end')
        self.entry_value.insert(0,calc_value)

    def __init__(self,main):
        super().__init__(main)
        main.title('calculator2')
        Button(main,text="√",width=10,command=lambda : self.get_sqrt()).grid(row=5,column=0)
        Button(main, text="x^2", width=10, command=lambda: self.get_power()).grid(row=5, column=1)

class Calculator_last(Calculator_upgrade) :
    x=[]
    y=[]
    fig = Figure(figsize=(3,3),dpi=100)
    ax = fig.add_subplot(111)
    canvas = None

    def get_sqrt(self):
        super().get_sqrt()
        for t in np.linspace(0,100,100):
            self.x.append(t)
            self.y.append(math.sqrt(t))
        self.ax.plot(self.x,self.y)
        self.canvas = FigureCanvasTkAgg(self.fig,main)
        self.canvas.get_tk_widget().grid(row=6,column=0,columnspan=4)

    def get_power(self):
        super().get_power()
        for t in np.linspace(1,100,100):
            self.x.append(t)
            self.y.append(math.pow(t,2))
        self.ax.plot(self.x,self.y)
        self.canvas = FigureCanvasTkAgg(self.fig,main)
        self.canvas.get_tk_widget().grid(row=6,column =0,columnspan=4)

#main
main = Tk()
calc = Calculator_last(main)
main.mainloop()

