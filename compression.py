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
    f = open(file_path,'r')
    text = f.readlines()
    for i in text:
        print (i)

