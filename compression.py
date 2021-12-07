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
            #Reads each character of the file, converts to Ascii number and adds it to an array
            arr.append(str(ord(x)))
            #Uses @ symbols to distinguish break-points
            arr.append('@')
    #Joins array into single string
    compressed = ''.join(arr)

    #Remove the extra @ generated at the end of the compression
    size = len(compressed)
    compressed = compressed[:size - 1]

    return compressed

#compresses file
def decompress(data):
    #Creates an array using the @ symbols
    arr = data.split('@')
    count = 0
    #Sets the number to its character form
    for i in arr:
        arr[count]= str(chr(int(i)))
        count += 1
    #Joins the array into a sting
    decompressed = ''.join(arr)

    return decompressed