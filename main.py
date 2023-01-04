from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import pyperclip

BLACK = '#323131'
GREY = '#c9c2c4'


# -----------------------------VIEW TXT WITH PASS---------------------------------#
def view_code():
    saved_passwords = Tk()
    saved_passwords.title("Saved Passwords")
    saved_passwords.config(pady=50, padx=50)
    with open("data.csv", "r") as file1:
        file = file1.readlines()
    r = 0
    for col in file:
        c = 0
        for row in col:
            label = Label(saved_passwords, text=row)
            label.grid(row=r, column=c)
            c += 1
        r += 1


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_random_password():
    password_generator = Tk()

    # New window

    password_generator.config(pady=50, padx=50)
    password_generator.overrideredirect(True)
    screen_width = password_generator.winfo_screenwidth()
    screen_height = password_generator.winfo_screenheight()
    x = (screen_width - password_generator.winfo_width()) // 2
    y = (screen_height - password_generator.winfo_height()) // 2
    password_generator.geometry(f"+{x}+{y}")

    if password_generator.winfo_exists():
        generate_password.config(state="disabled")

    def close_sub():
        password_generator.destroy()
        generate_password.config(state="normal")

    def do_nothing():
        pass

    password_generator.protocol("WM_DELETE_WINDOW", do_nothing)

    # Button to close window

    clear_button = Button(password_generator)
    clear_button.config(text="EXIT", command=close_sub)
    clear_button.grid(column=1, row=0, sticky="EW")

    # Labels

    password_generator.title("Password Generator")
    password_generator.resizable(0, 0)
    password_intro = Label(password_generator)
    password_intro.config(text="Password Generator", fg="red", font=("Arial", 20, "bold"))
    password_intro.grid(column=1, row=1)

    # Scale

    def char_scale_used(value):
        char_password_length.config(text=f" Your password will have {value} characters.")

    def num_scale_used(value):
        num_password_length.config(text=f" Your password will have {value} numbers.")

    def sym_scale_used(value):
        sym_password_length.config(text=f" Your password will have {value} symbols.")

    char_scale = Scale(password_generator, from_=0, to=12, sliderlength=5, orient="horizontal", command=char_scale_used)
    char_scale.grid(column=1, row=2)
    char_password_length = Label(password_generator)
    char_password_length.config(text=f" Your password will have {char_scale.get()} letters.")
    char_password_length.grid(column=1, row=3)
    num_scale = Scale(password_generator, from_=0, to=12, sliderlength=5, orient="horizontal", command=num_scale_used)
    num_scale.grid(column=1, row=4)
    num_password_length = Label(password_generator)
    num_password_length.config(text=f" Your password will have {num_scale.get()} numbers.")
    num_password_length.grid(column=1, row=5)
    sym_scale = Scale(password_generator, from_=0, to=12, sliderlength=5, orient="horizontal", command=sym_scale_used)
    sym_scale.grid(column=1, row=6)
    sym_password_length = Label(password_generator)
    sym_password_length.config(text=f" Your password will have {sym_scale.get()} symbols.")
    sym_password_length.grid(column=1, row=7)

    def make_pass():

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v',
                   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q',
                   'R',
                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_entry.delete(0, END)
        password_list = [choice(letters) for _ in range(char_scale.get())]
        password_list += [choice(numbers) for _ in range(num_scale.get())]
        password_list += [choice(symbols) for _ in range(sym_scale.get())]
        # Making the password random
        shuffle(password_list)
        # Join command
        password = "".join(password_list)
        # Make the password visible to GUI, copying it
        password_entry.insert(0, password)
        pyperclip.copy(password)

    generate_button = Button(password_generator)
    generate_button.config(text="Generate", command=make_pass)
    generate_button.grid(column=1, row=8, sticky="EW")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    user_name = username_entry.get()
    password_value = password_entry.get()

    if len(website_name) == 0 or len(password_value) == 0 or len(user_name) == 0:
        messagebox.showerror(title="Error", message="You should not leave blank spaces.")
    else:
        ok = messagebox.askokcancel(title=f"{website_name}",
                                    message=f"There are the info entered: \nEmail: {user_name}\n Password: "
                                            f"{password_value}. Shall we continue?")
        if ok:
            with open("data.csv", "a") as data:
                data.write(f"{website_name} | {user_name} | {password_value}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.resizable(0, 0)

photo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:")
website.grid(column=0, row=1)
username = Label(text="Email/Username:")
username.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(0, "youremail@email.com")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")


# Buttons
def clear():
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.delete(0, END)


generate_password = Button(text="Generate Password", command=generate_random_password)
generate_password.grid(column=2, row=3, sticky="EW")
add = Button(text="Add", command=save)
add.grid(column=1, row=4, columnspan=2, sticky="EW")
clear = Button(text="Clear", command=clear)
clear.grid(column=0, row=4)
view_button = Button(text="View Saved Passwords", command=view_code)
view_button.grid(column=1, row=5, columnspan=2, sticky="EW")
window.mainloop()
