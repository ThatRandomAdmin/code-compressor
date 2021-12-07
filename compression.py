import tkinter as tk
from tkinter import filedialog as fd
import traceback

def error(errormsg):
    #Start of GUI
    root4 = tk.Tk()
    root4.title("Error!")
    root4.resizable(False, False)

    #A label
    label = tk.Label(master=root4, width=30, height=2, text="Error:")
    label.config(font=("", 20))
    label.grid(row=0, column=0, columnspan=2, sticky="nsew")

    #Content area
    txtarea = tk.Text(root4, width=40, height=10)
    txtarea.grid(row=1, columnspan=2, pady=20)

    #Add error messsage
    txtarea.insert(tk.END, errormsg)

    #Destroy the Window
    def destroyit():
        root4.destroy()

    #Quit button
    btn = tk.Button(master=root4, width=20, height=2, text="Quit", command=destroyit)
    btn.grid(row=2, column=0, columnspan=2, sticky="nsew")

    root4.mainloop()


#Returns file path
def select():
    file = fd.askopenfilename()

    #Changes label based on entered file
    if file == "":
        return "No file selected"
    else:
        return file

#Compresses file
def compress(file_path):
    try:
        arr = []
        f = open(file_path,'r')
        text = f.readlines()
        for i in text:
            for x in i:
                #Reads each character of the file, converts to Ascii number and adds it to an array
                arr.append(str(ord(x)))
        #Joins array into single string
        compressed = '|'.join(arr)

        return compressed
    except Exception as e:
        error(e)

#Decompresses file
def decompress(data):
    try:
        #Creates an array using the @ symbols
        arr = data.split('|')
        count = 0
        #Sets the number to its character form
        for i in arr:
            arr[count]= str(chr(int(i)))
            count += 1
        #Joins the array into a sting
        decompressed = ''.join(arr)

        return decompressed
    except Exception as e:
        error(e)

#Encrypts file
def encrypt(file_path):
    try:
        arr = []
        f = open(file_path,'r')
        text = f.readlines()
        sum = 0
        count = 0
        for i in text:
            for x in i:
                #Reads each character of the file, converts to Ascii number and adds it to an array
                arr.append(ord(x))
                sum = sum + ord(x)

        #Gets the length of the array + the sum to create the mean
        length = len(arr)
        key = (sum - length)-1024

        for i in arr:
            arr[count] = str((i + key)-10000)
            count += 1
        #Joins the array + key into a sting
        arr.append(str(key - 10000))
        decompressed = '|'.join(arr)

        return decompressed
    except Exception as e:
        error(e)

#Decrypts file
def decrypt(data):
    try:
        #Creates an array using the @ symbols
        arr = data.split('|')
        count = 0
        #Sets the number to its character form
        for i in arr:
            i = (int(i) + 10000) - (int(arr[-1]) + 10000)
            arr[count]= str(chr(int(i)))
            count += 1
        #Joins the array into a sting
        decompressed = ''.join(arr)

        return decompressed
    except Exception as e:
        error(e)