#!/usr/bin/python3
#myPythonApp.py by Michael Akintuyosi
#Copyright(c) 2016

""" Tkinter Freestyling"""


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class App():

    def __init__(self, master):

        master.title('Expense Calculator')
        master.configure(background = '#f4d7c4')
        master.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f4d7c4')
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
        self.style.configure('TLabel', background='#f4d7c4')
        

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, text='Calculate your Expense', style='Header.TLabel').grid(row=0,column=1)
        ttk.Label(self.frame_header, text='Enter the figures below').grid(row=1,column=1)

        self.frame_contents = ttk.Frame(master)
        self.frame_contents.pack()

        ttk.Label(self.frame_contents, text='Electricity').grid(row=0, column=0, sticky='sw', padx=5)
        ttk.Label(self.frame_contents, text='Gas').grid(row=1, column=0, sticky='sw', padx=5)
        ttk.Label(self.frame_contents, text='Rent/Mortgage').grid(row=2, column=0, sticky='sw', padx=5)
        ttk.Label(self.frame_contents, text='Tax').grid(row=3, column=0, sticky='sw', padx=5)

        self.entry_elec = ttk.Entry(self.frame_contents, width = 10)
        self.entry_gas = ttk.Entry(self.frame_contents, width = 10)
        self.entry_rent = ttk.Entry(self.frame_contents, width = 10)
        self.entry_tax = ttk.Entry(self.frame_contents, width = 10)

        self.entry_elec.grid(row=0, column=4, padx=10)
        self.entry_gas.grid(row=1, column=4, padx=10)
        self.entry_rent.grid(row=2, column=4, padx=10)
        self.entry_tax.grid(row=3, column=4, padx=10)
        
        

        ttk.Button(self.frame_contents, text = 'Result',command=self.submit).grid(row=6, column=0, sticky='e',padx=5)
        
        ttk.Button(self.frame_contents, text = 'Clear' ,command=self.clear).grid(row=6, column=3, sticky='e',padx=5)
        
    def submit(self):

        self.all = int(self.entry_elec.get()) + int(self.entry_gas.get()) + int(self.entry_rent.get()) + int(self.entry_tax.get())
        self.clear()
        messagebox.showinfo(title = 'Expense Calculator', message = 'This is your result : ' + repr (self.all))
        

    def clear(self):
        self.entry_elec.delete(0, 'end')
        self.entry_gas.delete(0, 'end')
        self.entry_rent.delete(0, 'end')
        self.entry_tax.delete(0, 'end')




def main():
   root = Tk()
   app = App(root)

   root.mainloop()



if __name__ == "__main__": main()
