import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

def main():

    #Start of main GUI
    root = tk.Tk()
    root.title("Code Compressor!")
    root.resizable(False, False)

    #Some labels
    label = tk.Label(master=root, width=20, height=2, text="Selected folder:")
    label.config(font=("", 20))
    label.grid(row=0, column=0, columnspan=2, sticky="nsew")
    label1 = tk.Label(master=root, width=50, height=2, text="No folder selected")
    label1.config(font=("", 20))
    label1.grid(row=1, column=0, columnspan=2, sticky="nsew")

    #Compression vaildateion and method call
    def go():
        print("yay")

    def select():
        fldr = fd.askdirectory()

        #Changes label based on entered file
        if fldr == "":
            label1.configure(text="No folder selected")
        else:
            label1.configure(text = fldr + "/")

    #Re-select folder incase of error
    btn = tk.Button(master=root, width=20, height=2, text="Select folder!", command=select)
    btn.grid(row=2, column=0, columnspan=2, sticky="nsew")

    #Run button
    btn1 = tk.Button(master=root, width=20, height=2, text="Compress!", command=go)
    btn1.grid(row=3, column=0, columnspan=2, sticky="nsew")
    root.mainloop()

main()