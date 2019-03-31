import tkinter as tk
from tkinter import *
from tkinter import filedialog

import time
import Thomsons
import ThomsonsMap


class Main_Window:
    def __init__(self, master):
        """
        Create app ui.
        :param master: Root frame.
        """
        # create frame and add it to root.
        self.master = master
        self.frame = tk.Frame(self.master)
        # Header
        self.headerlabel = tk.Label(self.frame, text="Regex match using Thomson's construction", font=("Courier", 21),
                                    width="50")

        self.namelabel = tk.Label(self.frame, text="Graph Theory Project\n"
                                                   "Jose Ignacio Retamal\n"
                                                   "GMIT 2019", width="50")

        # Buttons
        self.button1 = tk.Button(self.frame, text='Single String Match', width=50, command=self.single_window)
        self.button2 = tk.Button(self.frame, text='Single String Match From File', width=50,
                                 command=self.single_window_file)
        self.button3 = tk.Button(self.frame, text='Search on file', width=50, command=self.search_window)
        self.button4 = tk.Button(self.frame, text='Match on file line by line', width=50 ,command=self.match_file_line)

        # Pack all components
        self.headerlabel.pack()
        self.namelabel.pack()
        self.button1.pack()
        self.button2.pack();
        self.button3.pack();
        self.button4.pack()
        self.frame.pack()

    def single_window_file(self):
        """
        Navigate to single string mathc.
        :return:
        """
        self.newWindow = tk.Toplevel(self.master)
        self.app = SingleWindowFile(self.newWindow)

    def single_window(self):
        """
        Navigate to match single on a file.
        :return:
        """
        self.newWindow = tk.Toplevel(self.master)
        self.app = SingleWindow(self.newWindow)

    def search_window(self):
        """
        Navigato to seacrh file.
        :return:
        """
        self.newWindow = tk.Toplevel(self.master)
        self.app = SearchFile(self.newWindow)

    def match_file_line(self):
        """
        Navigate to windows for match automaton on each line of a file.
        :return:
        """
        self.newWindow = tk.Toplevel(self.master)
        self.app = MatchFileLine(self.newWindow)

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
        self.check1 = Checkbutton(self.frameLeft, text="Algorithm 1", variable=self.var1, command=self.checkbox)
        self.var2 = IntVar()
        self.check2 = Checkbutton(self.frameLeft, text="Algorithm 2", variable=self.var2, command=self.checkbox2)

        self.label1 = tk.Label(self.frameLeft, text="Regex :")
        self.inReg = tk.Entry(self.frameLeft, width=50)

        self.label2 = tk.Label(self.frameLeft, text="String :")
        self.inStr = tk.Entry(self.frameLeft, width=50)

        self.matchButton = tk.Button(self.frameLeft, text='Match', width=25, command=self.match)
        self.quitButton = tk.Button(self.frameLeft, text='Quit', width=25, command=self.close_windows)

        # pack frame left
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


class SingleWindowFile:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frameLeft = tk.Frame(self.frame)
        self.frameRight = tk.Frame(self.frame)

        self.headerlabel = tk.Label(self.frame, text="Match regex agains a single string from file",
                                    font=("Courier", 21),
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
        self.filename = tk.Label(self.frameLeft, text="Please select file ^")

        self.matchButton = tk.Button(self.frameLeft, text='Match', width=25, command=self.match)
        self.quitButton = tk.Button(self.frameLeft, text='Quit', width=25, command=self.close_windows)

        # pack frame left
        self.check1.pack()
        self.check2.pack()
        self.label1.pack()
        self.inReg.pack()
        self.selectButton.pack()
        self.filename.pack()
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

        self.file = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        self.filename["text"] = "File: " + str(self.file);

    def match(self):
        if (self.file is None): return

        if (self.var1.get() == 1):
            start = time.perf_counter_ns()

            run = Thomsons.Runner(self.inReg.get().strip())
            try:

                file = open(self.file, encoding="utf-8")
                for line in file:
                    if (len(line) == 0): continue
                    run.runNext(line.strip())
            except:
                print("except")

            result = run.finish()

            end = time.perf_counter_ns()

            trant = end - start

            if (result == 1):
                self.otext.insert(INSERT,
                                  "[" + self.inReg.get() + "," + str(self.file) + "] -> " + "Yes\n" + " time: " + str(
                                      trant) + "\n")
            else:
                self.otext.insert(INSERT,
                                  "[" + self.inReg.get() + "," + str(self.file) + "] -> " + "No\n" + " time: " + str(
                                      trant) + "\n")



        else:
            start = time.perf_counter_ns()
            run = ThomsonsMap.Runner(self.inReg.get().strip())
            try:

                file = open(self.file, encoding="utf-8")
                for line in file:
                    if (len(line) == 0): continue
                    run.runNext(line.strip())
            except:
                print("except")

            result = run.finish()

            end = time.perf_counter_ns()

            trant = end - start

            if (result == 1):
                self.otext.insert(INSERT,
                                  "[" + self.inReg.get() + "," + str(self.file) + "] -> " + "Yes\n" + " time: " + str(
                                      trant) + "\n")
            else:
                self.otext.insert(INSERT,
                                  "[" + self.inReg.get() + "," + str(self.file) + "] -> " + "No\n" + " time: " + str(
                                      trant) + "\n")

class SearchFile:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frameLeft = tk.Frame(self.frame)
        self.frameRight = tk.Frame(self.frame)

        self.headerlabel = tk.Label(self.frame, text="Serach for match on a file",
                                    font=("Courier", 21),
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
        self.filename = tk.Label(self.frameLeft, text="Please select file ^")

        self.matchButton = tk.Button(self.frameLeft, text='Match', width=25, command=self.match)
        self.quitButton = tk.Button(self.frameLeft, text='Quit', width=25, command=self.close_windows)

        # pack frame left
        self.check1.pack()
        self.check2.pack()
        self.label1.pack()
        self.inReg.pack()
        self.selectButton.pack()
        self.filename.pack()
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

        self.file = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        self.filename["text"] = "File: " + str(self.file);

    def match(self):
        if (self.file is None): return



        starttime = time.perf_counter()
        # for save results
        matchs = list()


        if (self.var1.get() == 1):
        # Create object with automaton for un
            runc = Thomsons.RunChar(self.inReg.get().strip())
        else:
            runc = ThomsonsMap.RunChar(self.inReg.get().strip())

        try:
            # open file
            file = open(self.file, encoding="utf-8")

            linenum = 0
            pos = 0

            for line in file:
                linenum += 1
                if (len(line) == 0): continue

                i = 0
                while i < len(line):
                    runc.clear()
                    start = i;
                    stop = 0
                    for x in range(start, len(line)):
                        # print(x)
                        if (runc.run(line[x])):
                            stop = x
                            if (runc.check()):
                                # match
                                matchs.append((linenum, start, x))

                                i = stop
                                break
                        else:
                            break
                    i += 1
                    pos = i

        except:
            print("except")

        endtime = time.perf_counter()

        trant = endtime - starttime


        self.otext.insert(INSERT, "Match: " + str(len(matchs)) + "\n"+ "Result format : (line, start, end) : \n"+  " time: " +
                          str(trant) + "\n"+
                          str(matchs) + "\n")



class MatchFileLine:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frameLeft = tk.Frame(self.frame)
        self.frameRight = tk.Frame(self.frame)

        self.headerlabel = tk.Label(self.frame, text="Run on file line",
                                    font=("Courier", 21),
                                    width="50")
        self.headerlabel.pack()

        # frame left
        self.var1 = IntVar()
        self.check1 = Checkbutton(self.frameLeft, text="Algorithm 1", variable=self.var1, command=self.checkbox)
        self.var2 = IntVar()
        self.check2 = Checkbutton(self.frameLeft, text="Algorithm 2", variable=self.var2, command=self.checkbox2)
        self.var3 = IntVar()
        self.check3 = Checkbutton(self.frameLeft, text="Show result", variable=self.var3)

        self.label1 = tk.Label(self.frameLeft, text="Regex :")
        self.inReg = tk.Entry(self.frameLeft, width=50,font=("Courier", 18))

        self.selectButton = tk.Button(self.frameLeft, text='Select File', width=25, command=self.selectFile)
        self.filename = tk.Label(self.frameLeft, text="Please select file ^")

        self.matchButton = tk.Button(self.frameLeft, text='Match', width=25, command=self.match)
        self.quitButton = tk.Button(self.frameLeft, text='Quit', width=25, command=self.close_windows)

        # pack frame left
        self.check1.pack()
        self.check2.pack()
        self.check3.pack()
        self.label1.pack()
        self.inReg.pack()
        self.selectButton.pack()
        self.filename.pack()
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

        self.file = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        self.filename["text"] = "File: " + str(self.file);

    def match(self):
        if (self.file is None): return

        starttime = time.perf_counter()
        # for save results
        results = list()

        if (self.var1.get() == 1):
            # Create object with automaton for un
            runc = Thomsons.Runner(self.inReg.get().strip())
        else:
            runc = ThomsonsMap.Runner(self.inReg.get().strip())


        # open file
        file = open(self.file, encoding="utf-8")

        linenum = 0
        totalMatch = 0

        for line in file:

            linenum += 1
            runc.runNext(line.strip())
            res = bool(runc.finish())
            if(res): totalMatch += 1
            runc.clear()
            results.append((linenum,res))

        endtime = time.perf_counter()

        trant = endtime - starttime

        if(self.var3.get()==0):
            self.otext.insert(INSERT,
                              "Lines: " + str(len(results)) + "\n" +"Total match:"+str(totalMatch) + "\n" +  "Result format : (line,match?) : \n" + " time: " +
                              str(trant) + "\n")


        else:
            self.otext.insert(INSERT,
                              "Lines: " + str(len(results)) + "\n" + "Total match:" + str(
                                  totalMatch) + "\n" + "Result format : (line,match?) : \n" + " time: " +
                              str(trant) + "\n"+ str(results) + "\n")


def main():
    root = tk.Tk()
    app = Main_Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
