import tkinter as tk
from tkinter import *
from compression import *

def main():
    #Start of GUI
    root = tk.Tk()
    root.title("Main Menu!")
    root.resizable(False, False)

    #Menu 1
    button_1 = tk.Button(master=root, width=30, height=7, text="Compress a file", command=compress_menu)
    button_1.grid(row=0, column=0, sticky="nsew")

    #Menu 2
    button_2 = tk.Button(master=root, width=30, height=7, text="Decompress text", command=decompress_menu)
    button_2.grid(row=0, column=1, sticky="nsew")

    #Menu 3
    button_1 = tk.Button(master=root, width=30, height=7, text="Encrypt a file", command=encrypt_menu)
    button_1.grid(row=1, column=0, sticky="nsew")

    #Menu 4
    button_2 = tk.Button(master=root, width=30, height=7, text="Decrypt text", command=decrypt_menu)
    button_2.grid(row=1, column=1, sticky="nsew")

    root.mainloop()

def compress_menu():
    #Start of GUI
    root1a = tk.Tk()
    root1a.title("File Compressor!")
    root1a.resizable(False, False)

    #Some labels
    label = tk.Label(master=root1a, width=20, height=2, text="Selected file:")
    label.config(font=("", 20))
    label.grid(row=0, column=0, columnspan=2, sticky="nsew")
    label1 = tk.Label(master=root1a, width=50, height=2, text="No file selected")
    label1.config(font=("", 20))
    label1.grid(row=1, column=0, columnspan=2, sticky="nsew")

    #Select file and display in
    def file_select():
        lbltxt = select()
        label1.configure(text=lbltxt)
        if lbltxt != "No file selected":
            #Enable compression if valid
            btn1.configure(state="active")

    def run_compress():
        #gets file location, and compresses the text
        file_loc = label1.cget("text")
        content = compress(file_loc)
        #Opens view window with the compressed text
        view(content)

    #Destroy the Window
    def destroyit():
        root1a.destroy()

    #Re-select folder incase of error
    btn = tk.Button(master=root1a, width=20, height=2, text="Select file!", command=file_select)
    btn.grid(row=2, column=0, columnspan=2, sticky="nsew")

    #Run button
    btn1 = tk.Button(master=root1a, width=20, height=2, text="Compress!", command=run_compress)
    btn1.grid(row=3, column=0, columnspan=2, sticky="nsew")

    #Quit btn
    btn2 = tk.Button(master=root1a, width=20, height=2, text="Quit", command=destroyit)
    btn2.grid(row=4, column=0, columnspan=2, sticky="nsew")

    #Set compression btn to disabled by default
    btn1.configure(state="disable")

    root1a.mainloop()

def decompress_menu():
    #Start of GUI
    root1b = tk.Tk()
    root1b.title("File Decompressor!")
    root1b.resizable(False, False)

    #A label
    label = tk.Label(master=root1b, width=20, height=2, text="Decompress:")
    label.config(font=("", 20))
    label.grid(row=0, column=0, columnspan=2, sticky="nsew")

    #Input field
    inputvar = tk.Text(master=root1b, height = 5, width = 20)
    inputvar.grid(row=1, column=0, columnspan=2, sticky="nsew")

    #Run the decompression
    def run_decompress():
        data = inputvar.get(1.0, "end-1c")
        content = decompress(data)
        view(content)

    #Destroy the Window
    def destroyit():
        root1b.destroy()

    #Run button
    btn1 = tk.Button(master=root1b, width=20, height=2, text="Text to decompress!", command=run_decompress)
    btn1.grid(row=2, column=0, columnspan=2, sticky="nsew")

    #Quit btn
    btn2 = tk.Button(master=root1b, width=20, height=2, text="Quit", command=destroyit)
    btn2.grid(row=3, column=0, columnspan=2, sticky="nsew")

    root1b.mainloop()

def encrypt_menu():
    #Start of GUI
    root2a = tk.Tk()
    root2a.title("File Encryptor!")
    root2a.resizable(False, False)

    #Some labels
    label = tk.Label(master=root2a, width=20, height=2, text="Selected file:")
    label.config(font=("", 20))
    label.grid(row=0, column=0, columnspan=2, sticky="nsew")
    label1 = tk.Label(master=root2a, width=50, height=2, text="No file selected")
    label1.config(font=("", 20))
    label1.grid(row=1, column=0, columnspan=2, sticky="nsew")

    #Select file and display in
    def file_select():
        lbltxt = select()
        label1.configure(text=lbltxt)
        if lbltxt != "No file selected":
            #Enable compression if valid
            btn1.configure(state="active")

    def run_encrypt():
        #gets file location, and compresses the text
        file_loc = label1.cget("text")
        content = encrypt(file_loc)
        #Opens view window with the compressed text
        view(content)

    #Destroy the Window
    def destroyit():
        root2a.destroy()

    #Re-select folder incase of error
    btn = tk.Button(master=root2a, width=20, height=2, text="Select file!", command=file_select)
    btn.grid(row=2, column=0, columnspan=2, sticky="nsew")

    #Run button
    btn1 = tk.Button(master=root2a, width=20, height=2, text="Encrypt!", command=run_encrypt)
    btn1.grid(row=3, column=0, columnspan=2, sticky="nsew")

    #Quit btn
    btn2 = tk.Button(master=root2a, width=20, height=2, text="Quit", command=destroyit)
    btn2.grid(row=4, column=0, columnspan=2, sticky="nsew")

    #Set compression btn to disabled by default
    btn1.configure(state="disable")

    root2a.mainloop()

def decrypt_menu():
    #Start of GUI
    root2b = tk.Tk()
    root2b.title("File Decryptor!")
    root2b.resizable(False, False)

    #A label
    label = tk.Label(master=root2b, width=20, height=2, text="Text to decrypt:")
    label.config(font=("", 20))
    label.grid(row=0, column=0, columnspan=2, sticky="nsew")

    #Input field
    inputvar = tk.Text(master=root2b, height = 5, width = 20)
    inputvar.grid(row=1, column=0, columnspan=2, sticky="nsew")

    #Run the decompression
    def run_decrypt():
        data = inputvar.get(1.0, "end-1c")
        content = decrypt(data)
        view(content)

    #Destroy the Window
    def destroyit():
        root2b.destroy()

    #Run button
    btn1 = tk.Button(master=root2b, width=20, height=2, text="Decrypt!", command=run_decrypt)
    btn1.grid(row=2, column=0, columnspan=2, sticky="nsew")

    #Quit btn
    btn2 = tk.Button(master=root2b, width=20, height=2, text="Quit", command=destroyit)
    btn2.grid(row=3, column=0, columnspan=2, sticky="nsew")

    root2b.mainloop()

def view(content):
    #Start of GUI
    root3 = tk.Tk()
    root3.title("Output!")
    root3.resizable(False, False)

    #A label
    label = tk.Label(master=root3, width=20, height=2, text="Output:")
    label.config(font=("", 20))
    label.grid(row=0, column=0, columnspan=2, sticky="nsew")

    #Content area
    txtarea = tk.Text(root3, width=40, height=10)
    txtarea.grid(row=1, columnspan=2, pady=20)

    #Add compressed content
    txtarea.insert(tk.END, content)

    #Destroy the Window
    def destroyit():
        root3.destroy()

    #Quit button
    btn = tk.Button(master=root3, width=20, height=2, text="Quit", command=destroyit)
    btn.grid(row=2, column=0, columnspan=2, sticky="nsew")

    root3.mainloop()

def error(errormsg):
    #Start of GUI
    root4 = tk.Tk()
    root4.title("Output!")
    root4.resizable(False, False)

    #A label
    label = tk.Label(master=root4, width=20, height=2, text="Output:")
    label.config(font=("", 20))
    label.grid(row=0, column=0, columnspan=2, sticky="nsew")

    #Error label
    label1 = tk.Label(master=root4, width=20, height=2, text=errormsg)
    label1.config(font=("", 20))
    label1.grid(row=1, column=0, columnspan=2, sticky="nsew")

    #Destroy the Window
    def destroyit():
        root4.destroy()

    #Quit button
    btn = tk.Button(master=root4, width=20, height=2, text="Quit", command=destroyit)
    btn.grid(row=2, column=0, columnspan=2, sticky="nsew")

    root4.mainloop()

main()