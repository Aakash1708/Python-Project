from tkinter import * 
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import pyshorteners


class url_link_short:

        def create(self):
                if self.url.get() == "":
                        messagebox.showerror("Error","Please Paste an URL")
                        
                elif ".com" not in self.url.get():
                        messagebox.showerror("Error", "URL should contain \" .com \" ")
                else:
                        self.urls = self.url.get()
                        self.s = pyshorteners.Shortener()
                        self.short_url = self.s.tinyurl.short(self.urls)
                        
                        self.output = Entry(self.root,font=('verdana',10,'bold'),fg="indigo",bg="lightgrey",
                                            width=30,relief=GROOVE,borderwidth=2,border=2)
                        self.output.insert(END,self.short_url)
                        self.output.place(x=80,y=120)
        
        def __init__(self):
                self.root = tk.Tk()
                self.root.geometry('500x200')
                self.root.maxsize(500,200)
                self.root.minsize(500,200)
                self.root.title('URL Link Shortner')
                self.root['bg'] = "white"

                self.title = Label(self.root,text="URL Link Shortner",font=('verdana',15,'bold'),bg="white",fg="indigo")
                self.title.place(x=140,y=5)

                self.date = Label(self.root,text=datetime.now().date(),fg="indigo",font=('verdana',10,'bold'))
                self.date.place(x=400,y=5)


                Label(self.root,text="Paste Your Url Here ..",font=('verdana',10,'bold'),fg="indigo").place(x=50,y=50)

                self.url = Entry(self.root,width=50,bg="lightgrey",relief=GROOVE,borderwidth=2,border=2)
                self.url.place(x=50,y=80)

                self.button = Button(self.root,relief=GROOVE,text="Create",font=('verdana',8,'bold'),
                                     bg="indigo",fg="white",command=self.create)
                self.button.place(x=360,y=78)
                
                self.title = Label(self.root,text="Aakash Gupta",font=('verdana',10,'bold'),bg="white",fg="indigo")
                self.title.place(x=390,y=180)
                
                self.root.mainloop()



url_link_short()
        
    