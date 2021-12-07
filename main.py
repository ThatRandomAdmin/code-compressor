import tkinter as tk
from tkinter import *
from compression import *

def compress_menu():
    #Start of GUI
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
        content = compress(file_loc)
        view(content)

    #Re-select folder incase of error
    btn = tk.Button(master=root, width=20, height=2, text="Select file!", command=file_select)
    btn.grid(row=2, column=0, columnspan=2, sticky="nsew")

    #Run button
    btn1 = tk.Button(master=root, width=20, height=2, text="Compress!", command=run_compress)
    btn1.grid(row=3, column=0, columnspan=2, sticky="nsew")

    #Quit btn
    btn2 = tk.Button(master=root, width=20, height=2, text="Quit", command=quit)
    btn2.grid(row=4, column=0, columnspan=2, sticky="nsew")

    btn1.configure(state="disable")

    root.mainloop()

def view(content):
    #Start of GUI
    root1 = tk.Tk()
    root1.title("File Compressor!")
    root1.resizable(False, False)

    #Some labels
    label = tk.Label(master=root1, width=20, height=2, text="Compressed content:")
    label.config(font=("", 20))
    label.grid(row=0, column=0, columnspan=2, sticky="nsew")

    #Content area
    txtarea = tk.Text(root1, width=40, height=10)
    txtarea.grid(row=1, columnspan=2, pady=20)

    #Add compressed content
    txtarea.insert(tk.END, content)

    #Destroy the Window
    def destroyit():
        root1.destroy()

    #Quit button
    btn = tk.Button(master=root1, width=20, height=2, text="Quit", command=destroyit)
    btn.grid(row=2, column=0, columnspan=2, sticky="nsew")

    root1.mainloop()

compress_menu()