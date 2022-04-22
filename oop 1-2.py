from tkinter import *
from tkinter import ttk
window = Tk()

window.title("Python GUI")
window.geometry("700x500+20+10")

# Insert button widget
btn = Button(window, text="Button", fg="Purple")
btn.place(relx=.5, y=260, anchor="center")
lbl = Label(window, text="Student Semestral Grade", font=("verdana", 11))
lbl.place(relx=.5, y=50, anchor="center")

lbl1 = Label(window, text="Prelim Grade")
lbl2 = Label(window, text="Midterm Grade")
lbl3 = Label(window, text="Final Grade")
lbl1.place(x=50, y=100)
lbl2.place(x=50, y=150)
lbl3.place(x=50, y=200)


# Insert Entry Widget
txtfld = Entry(window, bd=4)
txtfld2 = Entry(window, bd=4)
txtfld3 = Entry(window, bd=4)
txtfld.place(relx=.5, y=110, anchor="center")
txtfld2.place(relx=.5, y=160, anchor="center")
txtfld3.place(relx=.5, y=210, anchor="center")


# Add Selection Widget
# Radio button

var = IntVar()
var.set(1)

r1 = Radiobutton(window, text="Prelim", variable=var, value=1)
r2 = Radiobutton(window, text="Midterm", variable=var, value=2)
r3 = Radiobutton(window, text="Final", variable=var, value=3)
r1.place(x=420, y=95)
r2.place(x=420, y=145)
r3.place(x=420, y=195)

# Check button
c1 = Checkbutton(window, text="View Term Grade")
c2 = Checkbutton(window, text="View Semestral Grade")
c1.place(x=180, y=290)
c2.place(x=380, y=290)

# List box
data1 = "English"
data2 = "Filipino"
data3 = "Programming"
lb = Listbox(window, height=5, selectmode='multiple')
lb.insert(END, data1, data2, data3)
lb.place(x=500, y=105)


cb = ttk.Combobox(window, values=(data1, data2, data3))
cb.place(x=500, y=200)


window.mainloop()
