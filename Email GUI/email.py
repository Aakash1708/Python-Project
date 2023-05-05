'''from tkinter import *
import tkinter as tk
from tkinter.ttk import *
#import register as rg

# --------------------------- Normal GUi ---------------------------
root = tk.Tk()
root.title("My GUI")
root.geometry("200X200")
root.maxsize(300,300)
root.minsize(200,200)
root.mainloop()

'''
# --------------------------- Email GUI ---------------------------
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("Email Id")
root.geometry("250x150")
root.maxsize(270, 150)
root.minsize(270, 150)
root.configure(bg="cyan")



# --------------------------- Email Sign-In page ---------------------------


class SignInWin(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Sign-in")
        self.geometry("350x150")
        self.minsize(250, 150)
        self.configure(bg="cyan")

        l1 = tk.Label(self, text="Enter your Email:", bg="orange")
        l1.grid(row=1, column=1, pady=10, padx=15)
        l2 = tk.Label(self, text="Enter your Password:", bg="orange")
        l2.grid(row=2, column=1, pady=10, padx=15)
        e1 = tk.Entry(self, bg="palegoldenrod")
        e1.insert(0, "Enter your e-mail")
        e1.grid(row=1, column=2, pady=10)

        e2 = tk.Entry(self, bg="palegoldenrod")
        e2.insert(0, "Enter your password")
        e2.grid(row=2, column=2, pady=4)
        
        l5 = tk.Label(self, text="Aakash Gupta",bg="cyan",fg="blue")
        l5.grid(row=4, column=1, pady=10, padx=15)

        submit1 = tk.Button(self, text="Submit")
        submit1.grid(column=2, row=3, pady="3")


# --------------------------- Email Register page ---------------------------


class RegisterWin(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Register")
        self.geometry("400x200")
        self.minsize(250, 150)
        self.configure(bg="cyan")

        l3 = tk.Label(self, text="Enter your Email:", bg="orange")
        l3.grid(row=1, column=1, pady=10, padx=15)
        l4 = tk.Label(self, text="Enter your Password:", bg="orange")
        l4.grid(row=2, column=1, pady=10, padx=15)
        l6 = tk.Label(self, text="Enter your Password:", bg="orange")
        l6.grid(row=3, column=1, pady=10, padx=15)
        
        e3 = tk.Entry(self, bg="palegoldenrod")
        e3.insert(0, "Enter your e-mail")
        e3.grid(row=1, column=2, pady=10)

        e4 = tk.Entry(self, bg="palegoldenrod")
        e4.grid(row=2, column=2, pady=4)
        
        e5 = tk.Entry(self, bg="palegoldenrod")
        e5.grid(row=3, column=2, pady=4)
        
        l5 = tk.Label(self, text="Aakash Gupta", bg="cyan", fg="blue")
        l5.grid(row=4, column=1, pady=10, padx=15)

        submit2 = tk.Button(self, text="Submit")
        submit2.grid(column=2, row=4, pady="3")
        
l5 = Label(root, text="Aakash Gupta",bg="cyan",fg="blue")
l5.grid(column=3, row=4)

Sign_In = tk.Button(root, text="Sign-In", command=SignInWin)
Sign_In.grid(column=2, row=3, pady=(45, 0),padx=(80, 0))

Register = tk.Button(root, text="Register", command=RegisterWin)
Register.grid(column=3, row=3, pady=(45, 0),padx=(0, 80))

root.mainloop()
