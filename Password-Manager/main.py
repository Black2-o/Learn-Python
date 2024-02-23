import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json




#
COLOR = "#FFC6AC"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_pass():
    pass_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_letter = [random.choice(letters) for _ in range(nr_letters-1)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols-1)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers-1)]

    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)
    password = "".join(password_list)


    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- Search PASSWORD ------------------------------- #
def find_pass():
    website = website_input.get()
    try:
        with open("database.json", "r") as data:
            my_data = json.load(data)
            email = my_data[website]["email"]
            pasword = my_data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {pasword}")
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
            messagebox.showinfo(title="Error", message="No Data File Found")
    website_input.delete(0, END)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    website = website_input.get()
    username = email_input.get()
    password = pass_input.get()
    new_dict = {website:{
        "email":username,
        "password":password
    }}
    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="OOPS", message="Please don't leave any fields empty!")
    else:

        add_on_database = f"{website} | {username} | {password}\n"
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            try:
                with open("database.json", "r") as data:
                    # Reading Old Data
                    dataX = json.load(data)
                    # Updating Old Data With new Data
                    dataX.update(new_dict)
            except FileNotFoundError:
                with open("database.json", "w") as data:
                    json.dump(new_dict, data, indent=4)
            else:
                with open("database.json", "w") as data:
                    # Saving upadted Data
                    json.dump(dataX, data, indent=4)
            website_input.delete(0, END)
            pass_input.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:  ")
website_input = Entry(width=40)
website_input.focus()
website_search_button = Button(text="Search", width=14, command=find_pass, bg=COLOR,highlightbackground=COLOR)
email_label = Label(text="Email/Username: ")
email_input = Entry(width=40)
email_input.insert(0, "noob125690@gmail.com")
pass_label = Label(text="Password:  ")
pass_input = Entry(width=40)
generate_button = Button(text="Generate Password", width=14, command=generate_pass, bg=COLOR, highlightbackground=COLOR)
add_button = Button(text="Add", width=33, command=add, bg=COLOR, highlightbackground=COLOR)


website_label.grid(column=0, row=1)
website_input.grid(column=1, row=1, columnspan=2)
website_search_button.grid(column=2, row=1)
email_label.grid(column=0, row=2)
email_input.grid(column=1, row=2, columnspan=2)
pass_label.grid(column=0, row=3)
pass_input.grid(column=1, row=3, columnspan=2)
generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()