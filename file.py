from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename()
    return filepath

#This is a test comment

def openFiles():
    filepath = filedialog.askopenfilenames()
<<<<<<< HEAD
return(filepath)    
=======
    file_list = list(filepath)
    return file_list
    
>>>>>>> 63bbabdd635f0f96e1185e73e31f81f0312846bb

def window_input():
    window = Tk()
    window.title("File Reader")
    window.geometry("300x300")
    button = Button(text="Open", command=openFile)
    button2 = Button(text="Open Files", command=openFiles)
    button.pack()
    button2.pack()
    window.mainloop()
