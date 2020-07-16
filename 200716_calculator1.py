from tkinter import *
#GUI

#main
main = Tk()
main.title("calculator1")
main.geometry()

#input section
entry_value = Entry(main, width=40, justify=RIGHT)
entry_value.grid(row=0, column=0, columnspan=3)
entry_value.focus_set()



def input_value(val) :
    entry_value.insert('end',val)

def clear_all():
    entry_value.delete(0,'end')

def get_result():
    return_value = eval(entry_value.get())

    entry_value.delete(0,'end')
    entry_value.insert(0,return_value)


#generating button
Button(main,text="=",width=20,command=lambda : get_result()).grid(row=5,column=2,columnspan=2)
Button(main,text="AC",width=10,command=lambda : clear_all()).grid(row=4,column=0)
Button(main,text="+",width=10,command=lambda :input_value('+')).grid(row=1,column=3)
Button(main,text="-",width=10,command=lambda :input_value('-')).grid(row=2,column=3)
Button(main,text="x",width=10,command=lambda :input_value('*')).grid(row=3,column=3)
Button(main,text="/",width=10,command=lambda :input_value('/')).grid(row=4,column=2)
Button(main,text="(",width=10,command=lambda :input_value('(')).grid(row=5,column=0)
Button(main,text=")",width=10,command=lambda :input_value(')')).grid(row=5,column=1)
Button(main,text="7",width=10,command=lambda :input_value(7)).grid(row=1,column=0)
Button(main,text="8",width=10,command=lambda :input_value(8)).grid(row=1,column=1)
Button(main,text="9",width=10,command=lambda :input_value(9)).grid(row=1,column=2)
Button(main,text="4",width=10,command=lambda :input_value(4)).grid(row=2,column=0)
Button(main,text="5",width=10,command=lambda :input_value(5)).grid(row=2,column=1)
Button(main,text="6",width=10,command=lambda :input_value(6)).grid(row=2,column=2)
Button(main,text="1",width=10,command=lambda :input_value(1)).grid(row=3,column=0)
Button(main,text="2",width=10,command=lambda :input_value(2)).grid(row=3,column=1)
Button(main,text="3",width=10,command=lambda :input_value(3)).grid(row=3,column=2)
Button(main,text="0",width=10,command=lambda :input_value(0)).grid(row=4,column=1)


main.mainloop()

