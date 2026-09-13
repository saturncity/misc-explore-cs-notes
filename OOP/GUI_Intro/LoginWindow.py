from pathlib import Path
from tkinter import *
from OOP.User_Model import User

HERE = Path(__file__).parent

class Login:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Advanced Login Systems")
        self.frame.geometry("500x500")
        self.users = []

        self.label_welcome = Label(text="Thank You for using Advanced Login Systems!", bg="aquamarine1", fg="black")
        self.label_welcome.pack()

        self.label_username = Label(text="\nEnter your username:")
        self.label_username.pack()

        self.text_username = Entry()
        self.text_username.pack()

        self.label_password = Label(text="Enter your password:")
        self.label_password.pack()

        self.text_password = Entry()
        self.text_password.pack()

        self.button_login = Button(text="Login")
        self.button_login.pack()

        self.label_status = Label(text="Please Press Login Above")
        self.label_status.pack()

        self.read_file(HERE.parent.parent / "Login System" / "accounts.txt")

    def run(self):
        self.frame.mainloop()


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
        account_name = self.text_username.get() #
        u_index = self.search_user(account_name)
        if u_index == -1:
            self.label_status.config(text="User doesn't exit. Please try again.", fg="red")
        else:
            auth_pass = self.authentication(u_index)
            if auth_pass:
                pass
                # launch_app()

app = Login()
app.run()