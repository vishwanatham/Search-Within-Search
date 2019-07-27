import os
import re
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('Search')
root.geometry("770x350")



def txt_search(returnlist = False):
    global filepath
    global keyword1
    global caseSensitive
    global searchresult
    list1 = []
    file_number = 0
    files = [f for f in os.listdir(filepath) if os.path.isfile(filepath + "\\" + f)]
    for file in files:
        file_t = open(filepath + "\\" + file)
        file_text = file_t.read()
        if not(format(caseSensitive.get())):
            file_text = file_text.lower()
        file_t.close()
        if re.search(keyword1, file_text):
            if returnlist:
                list1.append(filepath+"\\"+file)
            else:
                result.insert("end", filepath+"\\"+file)
                result.insert("end","\n")

            file_number = file_number + 1
    print(keyword1 + " is found in " + str(file_number)+" files")
    if returnlist:
        return list1


def txt_search_in_list(filelist=[]):
    global filepath
    global keyword2
    global caseSensitive
    global searchresult
    file_number = 0
    files = [f for f in filelist if os.path.isfile(f)]
    for file in files:
        file_t = open(file)
        file_text = file_t.read()
        if not(format(caseSensitive.get())):
            file_text = file_text.lower()
        file_t.close()
        if re.search(keyword2, file_text):
            result.insert("end", file)
            result.insert("end","\n")
            file_number = file_number + 1
    print(keyword1 + " is found in " + str(file_number)+" files")


def searchtext():
    result.delete('1.0', "end")
    global filepath
    global keyword1
    global keyword2
    global searchresult
    keyword1 = FK.get()
    keyword2 = SK.get()
    filepath = filepath.replace("/", "\\")
    if keyword2 == "":
        txt_search()
    else:
        filelist = txt_search(True)
        txt_search_in_list(filelist)

def browsedirectory():
    global filepath
    filepath = filedialog.askdirectory()
    path.insert(0, filepath)


label1 = tk.Label(root, text="First level Keyword")
label1.place(x=10, y=25)

keyword1 = ""
FK = tk.Entry()
FK.insert(0, keyword1)
FK.place(x=150, y=25)

label1 = tk.Label(root, text="Second level Keyword")
label1.place(x=10, y=60)

keyword2 = ""
SK = tk.Entry()
FK.insert(0, keyword2)
SK.place(x=150, y=60)

filepath = "C:\\Users\\Vishwanatham\\Documents"
path = tk.Entry()
path.insert(0, filepath)
path.place(x=10, y=90, width="200", height="25")


browse = tk.Button(text="Browse", command=browsedirectory)
browse.place(x=220, y=90)

lblOPtions = tk.Label(text="Options")
lblOPtions.place(x=10, y=140)

caseSensitive = tk.BooleanVar()
caseSensitive.set(False)
cbCase = tk.Checkbutton(text="Match Case", var=caseSensitive)
cbCase.place(x=10, y=160)

tk.Button(text="Search", command=searchtext).place(x=220, y=140, width=50)

searchresult = ""
result = tk.Text()
result.insert("end",searchresult)
result.place(x=10, y=200, width="750", height="140")



root.mainloop()