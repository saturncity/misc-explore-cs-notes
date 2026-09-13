from tkinter import *
class Window:
    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("920x420")
        self.frame.title("The truth")
        self.lbl_message = Label(text="Hello, world", bg="aquamarine1", fg="black")
        self.lbl_message.pack()

    def run(self):
        self.frame.mainloop()

app = Window()
app.run()