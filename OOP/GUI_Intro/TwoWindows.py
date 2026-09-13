from pathlib import Path
from tkinter import *
from OOP.User_Model import User

HERE = Path(__file__).parent


class Login:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("Advanced Login Systems")
        self.current_window.geometry("500x500")

        self.users = []

        self.label_welcome = Label(self.current_window, text="Thank You for using Advanced Login Systems!",
                                   bg="aquamarine1", fg="black")
        self.label_welcome.pack()

        self.label_username = Label(self.current_window, text="\nEnter your username:")
        self.label_username.pack()

        self.text_username = Entry(self.current_window)
        self.text_username.pack()

        self.label_password = Label(self.current_window, text="Enter your password:")
        self.label_password.pack()

        self.text_password = Entry(self.current_window)
        self.text_password.pack()

        self.button_login = Button(self.current_window, text="Login", command=self.login_handle)
        self.button_login.pack()

        self.button_exit = Button(self.current_window, text="Exit", command=exit)
        self.button_exit.pack()

        self.label_status = Label(self.current_window, text="Please Press Login Above")
        self.label_status.pack() # t

        self.img = PhotoImage(file=HERE / "python.png")
        self.label_image = Label(self.current_window, image=self.img)
        self.label_image.pack()

        self.read_file(HERE.parent / "accounts.txt")

    def open_converter(self):
        Converter(self.root)
        self.current_window.destroy()

    def write_to_file(self, file_name):
        with open(file_name, 'w') as file_out:
            for user in self.users:
                user_account = user.get_username() + ',' + \
                               user.get_password() + ',' + \
                               user.get_email() + ',' + \
                               str(user.is_admin()) + ',' + '\n'
                file_out.write(user_account)
            self.label_status.config(text="File output done.", fg="orange")

    def read_file(self, file_name):
        with open(file_name, 'r') as file_in:
            lines = file_in.readlines()
            for line in lines:
                if line != '\n':
                    new_list = line.split(',')
                    new_user = User(new_list[0], new_list[1], new_list[2], new_list[3])
                    self.users.append(new_user)
            self.label_status.config(text="File input done.", fg="orange")

    def search_user(self, username):
        index = -1
        i = 0
        for user in self.users:
            if str(user.get_username()).lower() == username.lower():
                index = i
                break

            i = i + 1
        return index

    def authentication(self, user_index):
        correct_pass = False
        count = 0
        while not correct_pass and count < 3:
            user_password = self.text_password.get()
            user = self.users[user_index]
            if user.get_password() == user_password:
                self.label_status.config(text=f"Welcome, {user.get_username().title()}", fg="green")
                correct_pass = True
            else:
                count = count + 1
                if count == 3:
                    self.label_status.config(text="Authentication failed. Please try again.", fg="red")
                else:
                    self.label_status.config(text=f"Incorrect password. You have {3 - count} attempt(s) left.", fg="red")

        return correct_pass

    def login_handle(self):
        account_name = self.text_username.get()
        u_index = self.search_user(account_name)
        if u_index == -1:
            self.label_status.config(text="User doesn't exit. Please try again.", fg="red")
        else:
            auth_pass = self.authentication(u_index)
            if auth_pass:
                self.open_converter()


class Converter:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.title("Converter")
        self.current_window.geometry("960x420")

        self.label_title = Label(self.current_window, text="Welcome to Jason's Fahrenheit to Celsius Converter!", bg="aquamarine1",
                                 fg="black")

        self.label_input = Label(self.current_window, text="Input your number to convert here (Celsius or Fahrenheit):")
        self.text_input = Entry(self.current_window)

        self.button_celsius = Button(self.current_window, text="Convert Input (Fahrenheit) to Celsius", command=self.convert_to_celsius)
        self.button_fahrenheit = Button(self.current_window, text="Convert Input (Celsius) to Fahrenheit",
                                        command=self.convert_to_fahrenheit)

        self.button_logout = Button(self.current_window, text="Logout", command=self.open_login)
        self.button_exit = Button(self.current_window, text="Exit", command=exit)
        self.button_meme = Button(self.current_window, text="Show me a MEME!", command=self.open_cat_meme)
        self.label_result = Label(self.current_window, text="")

        self.label_title.pack()
        self.line_skip()
        self.label_input.pack()
        self.text_input.pack()
        self.line_skip()
        self.button_celsius.pack()
        self.button_fahrenheit.pack()
        self.line_skip()
        self.button_logout.pack()
        self.button_exit.pack()
        self.button_meme.pack()
        self.label_result.pack()

    def open_login(self):
        Login(self.root)
        self.current_window.destroy()

    def open_cat_meme(self):
        Cat(self.root)
        self.current_window.destroy()

    def line_skip(self):
        """Skip lines to improve the GUI experience."""
        self.label_line = Label(self.current_window, text="")
        self.label_line.pack()

    def convert_to_celsius(self):
        """Converts number given (presumably a number in fahrenheit) to celsius using ((intake - 32) * (5 / 9))."""
        try:
            intake = float(self.text_input.get())
            result = round(((intake - 32) * (5 / 9)), 1)
            self.label_result.config(text=f"{result}°c", bg="gold", fg="black")
        except ValueError:
            self.label_result.config(text="ERROR", bg="red", fg="black")

    def convert_to_fahrenheit(self):
        """Converts number given (presumably a number in celsius) to fahrenheit using ((intake * (9 / 5)) + 32)."""
        try:
            intake = float(self.text_input.get())
            result = round(((intake * (9 / 5)) + 32), 1)
            self.label_result.config(text=f"{result}°f", bg="gold", fg="black")
        except ValueError:
            self.label_result.config(text="ERROR", bg="red", fg="black")

class Cat:
    def __init__(self, root):
        global photo
        self.root = root
        self.root.withdraw()
        self.current_window = Toplevel()
        self.current_window.configure(bg="black")
        self.current_window.title("Cat Memez")

        photo = PhotoImage(file=HERE / "python.png")

        self.label_image = Label(self.current_window,
                      text="bro, do you even code?",
                      font=('Arial', 40, 'bold'),
                      fg='#00FF00',
                      bg='black',
                      relief=RAISED,
                      bd=10,
                      padx=20,
                      pady=20,
                      image=photo,
                      compound='bottom')
        self.label_image.pack()

root = Tk()
app = Login(root)
root.mainloop()