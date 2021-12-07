from tkinter import filedialog as fd
import os

#returns file path
def select():
    file = fd.askopenfilename()

    #Changes label based on entered file
    if file == "":
        return "No file selected"
    else:
        return file

#compresses file
def compress(file_path):
    arr = []
    f = open(file_path,'r')
    text = f.readlines()
    for i in text:
        for x in i:
            arr.append(str(ord(x)))
            arr.append('@')
    compressed = ''.join(arr)
    return compressed