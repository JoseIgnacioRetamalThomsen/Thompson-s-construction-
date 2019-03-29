import tkinter as tk
from tkinter import *
from tkinter import filedialog
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
        self.button2 = tk.Button(self.frame, text='Single String Match From File', width=50, command=self.single_window_file)
        self.headerlabel.pack()
        self.namelabel.pack()
        self.button1.pack()
        self.button2.pack();
        self.frame.pack()

    def single_window_file(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = SingleWindowFile(self.newWindow)

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

        self.oframe = tk.Frame(self.frameRight, width=600, height=600)

        self.otext = tk.Text(self.oframe)
        self.otext.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        self.scrollb = tk.Scrollbar(self.oframe, command=self.otext.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.otext['yscrollcommand'] = self.scrollb.set


        self.righheader.pack()
        self.oframe.pack(expand=True)

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


class SingleWindowFile:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frameLeft = tk.Frame(self.frame)
        self.frameRight = tk.Frame(self.frame)

        self.headerlabel = tk.Label(self.frame, text="Match regex agains a single string from file", font=("Courier", 21),
                                    width="50")
        self.headerlabel.pack()

        # frame left
        self.var1 = IntVar()
        self.check1 = Checkbutton(self.frameLeft, text="Algorithm 1", variable=self.var1, command=self.checkbox)
        self.var2 = IntVar()
        self.check2 = Checkbutton(self.frameLeft, text="Algorithm 2", variable=self.var2, command=self.checkbox2)

        self.label1 = tk.Label(self.frameLeft, text="Regex :")
        self.inReg = tk.Entry(self.frameLeft, width=50)

        self.selectButton = tk.Button(self.frameLeft, text='Select File', width=25, command=self.selectFile)

        self.matchButton = tk.Button(self.frameLeft, text='Match', width=25, command=self.match)
        self.quitButton = tk.Button(self.frameLeft, text='Quit', width=25, command=self.close_windows)

        # pack frame left
        self.check1.pack()
        self.check2.pack()
        self.label1.pack()
        self.inReg.pack()
        self.selectButton.pack()
        self.matchButton.pack()
        self.quitButton.pack()

        # frame righ
        self.righheader = tk.Label(self.frameRight, text="Output:")

        self.oframe = tk.Frame(self.frameRight, width=600, height=600)

        self.otext = tk.Text(self.oframe)
        self.otext.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        self.scrollb = tk.Scrollbar(self.oframe, command=self.otext.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.otext['yscrollcommand'] = self.scrollb.set

        self.righheader.pack()
        self.oframe.pack(expand=True)

        self.frame.pack()
        self.frameLeft.pack(side="left")
        self.frameRight.pack(side="left")

        self.var1.set(1)
        self.var2.set(0)

    def checkbox(self):
        print(self.var1.get())
        if self.var1.get() == 0:
            print(self.var1.get())
            self.var2.set(1)
        else:
            self.var2.set(0)
            # self.var2.set(0)
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

    def selectFile(self):

        my = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Text files","*.txt"),("all files", "*.*")))
        print(my)
        
    def match(self):
        if (self.var1.get() == 1):
            result = Thomsons.match(self.inReg.get(), self.inStr.get())
            if (result == 1):
                self.otext.insert(INSERT, "[" + self.inReg.get() + "," + self.inStr.get() + "] -> " + "Yes\n")
            else:
                self.otext.insert(INSERT, "[" + self.inReg.get() + "," + self.inStr.get() + "] -> " + "No\n")
        else:
            nfa = ThomsonsMap.compile(self.inReg.get())
            result = nfa.run(self.inStr.get())
            if (result == 1):
                self.otext.insert(INSERT, "[" + self.inReg.get() + "," + self.inStr.get() + "] -> " + "Yes\n")
            else:
                self.otext.insert(INSERT, "[" + self.inReg.get() + "," + self.inStr.get() + "] -> " + "No\n")


def main():
    root = tk.Tk()
    app = Main_Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()