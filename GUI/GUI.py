"""

GUI

In python we can create applications using GUI - Graphical user interface

We are going to create GUI using tkinter module.
There are other modules as well like - wxPython, PyQt, JPython

"""

from ast import Lambda
import tkinter as tk

# print(dir(tk))
######################
######functions#######


root = tk.Tk()  # create a window
root.geometry("1000x1000")

Welcome = tk.Label(root, text="Welcome to the GUI program output")

name = tk.Entry(root)


add = tk.Text(root)

# create image object
cm = tk.PhotoImage(file="F:\Python Dec 2021\GitHub\GUI\clickmeimg.png")

bye = tk.Button(root, text="Good bye", activeforeground="blue")
clickme = tk.Button(root,
                    activebackground="RED", image=cm, command=lambda: add.insert(tk.END, name.get()))  # create a button


var = tk.IntVar()

R1 = tk.Radiobutton(root, text="Male", variable=var, value=1,
                    command=lambda: print(var.get()))


R2 = tk.Radiobutton(root, text="Female", variable=var, value=2,
                    command=lambda: print(var.get()))


R3 = tk.Radiobutton(root, text="Option 3", variable=var, value=3,
                    command=lambda: print(var.get()))


Welcome.pack()
name.pack()
add.pack()
clickme.pack()  # add button to window
R1.pack(anchor=tk.W)
R2.pack(anchor=tk.W)
R3.pack(anchor=tk.W)
bye.pack()


# Welcome.grid(row=1, column=1)
# clickme.grid(row=2, column=2)
# bye.grid(row=3, column=3)

# 400 X 100 pixel will have the lable from topleft of the window
# Welcome.place(x=400, y=100)
# clickme.place(x=400, y=150)
# bye.place(x=500, y=150)


root.mainloop()
