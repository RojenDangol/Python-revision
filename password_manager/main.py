from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get().lower()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Empty field!', message='Please fill in all the fields.')
    else:
        try:
            with open('data.json', 'r') as file:
                # json.dump(new_data, file, indent=4)
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
                # file.write(f'{website} | {email} | {password}\n')
        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)


def find_password():
    website = website_input.get().lower()
    if len(website) == 0:
        messagebox.showinfo(title='Empty field!', message='Please fill in website name.')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title='Error', message='No data File Found')
        else:
            if website in data:
                messagebox.showinfo(title=website, message=f'Email: {data[website]['email']}\n'
                                                                 f'Password: {data[website]['password']}')
            else:
                messagebox.showinfo(title=website, message=f'No details for the {website} exists.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
search_button = Button(text='Search', highlightthickness=0, width=15, command=find_password)
search_button.grid(column=2, row=1)

generate_button = Button(text='Generate Password', highlightthickness=0, width=15, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=34, highlightthickness=0, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()