from tkinter import filedialog as fd

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

#Decompresses file
def decompress(data):
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

#Encrypts file
def encrypt(file_path):
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

#Decrypts file
def decrypt(data):
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