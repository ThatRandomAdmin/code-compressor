import tkinter as tk
from tkinter import *
from compression import *

def main():

    #Start of main GUI
    root = tk.Tk()
    root.title("File Compressor!")
    root.resizable(False, False)

    #Some labels
    label = tk.Label(master=root, width=20, height=2, text="Selected file:")
    label.config(font=("", 20))
    label.grid(row=0, column=0, columnspan=2, sticky="nsew")
    label1 = tk.Label(master=root, width=50, height=2, text="No file selected")
    label1.config(font=("", 20))
    label1.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def file_select():
        lbltxt = select()
        label1.configure(text=lbltxt)
        if lbltxt != "":
            btn1.configure(state="active")

    def run_compress():
        file_loc = label1.cget("text")
        compress(file_loc)

    #Re-select folder incase of error
    btn = tk.Button(master=root, width=20, height=2, text="Select file!", command=file_select)
    btn.grid(row=2, column=0, columnspan=2, sticky="nsew")

    #Run button
    btn1 = tk.Button(master=root, width=20, height=2, text="Compress!", command=run_compress)
    btn1.grid(row=3, column=0, columnspan=2, sticky="nsew")

    btn1.configure(state="disable")

    root.mainloop()

main()