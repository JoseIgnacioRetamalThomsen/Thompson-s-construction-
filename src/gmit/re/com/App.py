import tkinter as tk
from tkinter import *
import Thomsons
import ThomsonsMap

class Main_Window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.headerlabel = tk.Label(self.frame, text="Regex match using Thomson's construction",font=("Courier", 21),width="50")


        self.namelabel = tk.Label(self.frame, text="Graph Theory Project\n"
                                           "Jose Ignacio Retamal\n"
                                           "GMIT 2019",width="50")

        self.button1 = tk.Button(self.frame, text = 'Single String Match', width = 50, command = self.single_window)
        self.button2 = tk.Button(self.frame, text='Search on text', width=50, command=self.new_window)
        self.headerlabel.pack()
        self.namelabel.pack()
        self.button1.pack()
        self.button2.pack();
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

    def single_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = SingleWindow(self.newWindow)


class SingleWindow:



    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frameLeft = tk.Frame(self.frame)
        self.frameRight = tk.Frame(self.frame)

        self.headerlabel = tk.Label(self.frame, text="Match regex agains a single string", font=("Courier", 21),
                                    width="50")
        self.headerlabel.pack()

        # frame left
        self.var1 = IntVar()
        self.check1= Checkbutton(self.frameLeft, text="Algorithm 1", variable=self.var1, command=self.checkbox)
        self.var2 = IntVar()
        self.check2 = Checkbutton(self.frameLeft, text="Algorithm 2", variable=self.var2, command=self.checkbox2)

        self.label1 = tk.Label(self.frameLeft, text="Regex :")
        self.inReg = tk.Entry(self.frameLeft, width=50)

        self.label2 = tk.Label(self.frameLeft, text="String :")
        self.inStr = tk.Entry(self.frameLeft, width=50)

        self.matchButton = tk.Button(self.frameLeft, text ='Match', width = 25, command = self.match)
        self.quitButton = tk.Button(self.frameLeft, text ='Quit', width = 25, command = self.close_windows)

        #pack frame left
        self.check1.pack()
        self.check2.pack()
        self.label1.pack()
        self.inReg.pack()
        self.label2.pack()
        self.inStr.pack()
        self.matchButton.pack()
        self.quitButton.pack()

        # frame righ
        self.righheader = tk.Label(self.frameRight, text="Output:")

        self.otext = tk.Text(self.frameRight)


        self.righheader.pack()
        self.otext.pack()

        self.frame.pack()
        self.frameLeft.pack(side="left")
        self.frameRight.pack(side="left")

        self.var1.set(1)
        self.var2.set(0)

    def checkbox(self):
        print(self.var1.get())
        if self.var1.get()==0:
            print(self.var1.get())
            self.var2.set(1)
        else:
            self.var2.set(0)
            #self.var2.set(0)
        # else:
        #     self.var1.set(0)
        #     self.var2.set(1)

    def checkbox2(self):

        if self.var2.get() == 0:
            self.var1.set(1)

        else:
            self.var1.set(0)




    def close_windows(self):
            self.master.destroy()

    def match(self):
        if(self.var1.get()==1):
            result = Thomsons.match(self.inReg.get(),self.inStr.get())
            if(result == 1):
                self.otext.insert(INSERT,"["+self.inReg.get()+","+ self.inStr.get() +"] -> " + "Yes\n" )
            else:
                self.otext.insert(INSERT, "[" + self.inReg.get() + "," + self.inStr.get() + "] -> " + "No\n")
        else:
            nfa = ThomsonsMap.compile(self.inReg.get())
            result = nfa.run(self.inStr.get())
            if (result == 1):
                self.otext.insert(INSERT, "[" + self.inReg.get() + "," + self.inStr.get() + "] -> " + "Yes\n")
            else:
                self.otext.insert(INSERT, "[" + self.inReg.get() + "," + self.inStr.get() + "] -> " + "No\n")


class Demo2:


    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = Main_Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()