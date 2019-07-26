import os
import re
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('Search')
root.geometry("280x200")


class TextSearch:
    def __init__(self, string2, path1, i=None):
        self.path1 = path1
        self.string1 = string2
        self.i = i
        if self.i:
            string2 = string2.lower()
            self.string2 = re.compile(string2)

    def txt_search(self):
        file_number = 0

        files = [f for f in os.listdir(self.path1) if os.path.isfile(self.path1 + "\\" + f)]
        print(files)
        for file in files:
            file_t = open(self.path1 + "\\" + file)
            file_text = file_t.read()
            if self.i:
                file_text = file_text.lower()
            file_t.close()
            if re.search(self.string2, file_text):
                print("The text " + self.string1 + " found in ", file)
            file_number = file_number + 1


def browsedirectory():
    global filepath
    filepath = filedialog.askdirectory()
    path.insert(0, filepath)


label1 = tk.Label(root, text="First level Keyword")
label1.place(x=10, y=30)

FK = tk.Entry()
FK.place(x=150, y=30)

label1 = tk.Label(root, text="Second level Keyword")
label1.place(x=10, y=60)

SK = tk.Entry()
SK.place(x=150, y=60)

filepath = "C:\\Users\\Vishwanatham\\Documents"
path = tk.Entry()
path.insert(0, filepath)
path.place(x=10, y=90, width="200", height="25")


browse = tk.Button(text="Browse", command=browsedirectory)
browse.place(x=220, y=90)


lblOPtions = tk.Label(text="Options")
lblOPtions.place(x=10, y=150)

cbCase = tk.Checkbutton(text="Match Case")
cbCase.place(x=10, y=170)

def searchtext():
    text = FK.get()
    fp = filepath.replace("/", "\\")
    ts = TextSearch(text, fp, 1)
    ts.txt_search()


tk.Button(text="Search", command=searchtext).place(x=220, y=165, width=50)

root.mainloop()