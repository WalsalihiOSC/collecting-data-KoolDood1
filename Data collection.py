#Data collection (Andre)


from tkinter import *

class interface:
    def __init__(self):
        self.input1 = StringVar()
        self.input2 = StringVar()



class Data:
    def __init__(self):
        pass




if __name__ =="__main__":
    root = Tk()
    gui = interface(root)
    root.geometry("300x200")
    root.title("Data collection")
    root.mainloop()