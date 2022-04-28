from tkinter import *

window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400")


def click():
    btn1 = Button(window, text="Click to Change Color", bg="Yellow")
    btn1.place(relx=.5, rely=.5, anchor="center")


btn = Button(window, text="Click to Change Color", command=click)
btn.place(relx=.5, rely=.5, anchor="center")


window.mainloop()
