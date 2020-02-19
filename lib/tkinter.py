import tkinter as info
import tkinter as tk

class Application(info.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = info.Button(self)
        self.hi_there["text"] = "Info: Numerology System   \n( - Click Here -)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.quit = info.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("                                                                                         ")
        print("                                                                                         ")
        print("                                                                                         ")
        print("=============================================================================")
        print(" ===  Numerology system ===  ")
        print("--------------------------------")
        print(" Every letter has a unique vibration and the numbers are assigned to "
              "letters on the vibrational value and the numbers only go from 1 to 9")
        print("   Numerology has numerous interpretations regarding each number,"
              " but it is always easier to work with one-digit numbers, the meaning"
              " is clearer and the personality puzzle is easier to assemble.")
        print("   In Numerology it is often needed to reduce all two and three-digit numbers"
              " to one digit.")
        print("=============================================================================")
        print("                                                                                         ")
        print("                                                                                         ")
        print("Quit window, and check your master-numbers")







root = info.Tk()
app = Application(master=root)
app.mainloop()


