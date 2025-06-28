import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        min_length = int(length_entry.get())
        if min_length<=0:
            messagebox.showerror("Invalid input", "length of password must be positive number.")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for length.")
        return
    
    num = number_var.get()
    special_char = special_var.get()

    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if num:
        characters += digits
    if special_char:
        characters += special

    if not characters:  #in case both options are unchecked
        characters = letters

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd)< min_length:
        if len(pwd) >= 100: #prevents excessively long passwords
            break

        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if num:
            meets_criteria = has_number
        if special_char:
            meets_criteria = meets_criteria and has_special

    result_label.config(text="Generated Password:" + pwd)

# gui setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.config(bg="#f5f5f5")

#password length
tk.Label(root, text="Minimum length:", bg="#f5f5f5", font=("Arial", 10)).pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

# frame for checkboxes to align them properly
checkbox_frame = tk.Frame(root, bg="#f5f5f5")
checkbox_frame.pack(pady=5)

# checkboxes for options
number_var = tk.BooleanVar()
special_var = tk.BooleanVar()

cb1 = tk.Checkbutton(
    checkbox_frame,
    text="Include numbers",
    variable=number_var,
    bg="#f5f5f5", 
    anchor='w',
    width=20
)
cb1.pack(side='top', anchor='w', padx=10, pady=2)

cb2 = tk.Checkbutton(
    checkbox_frame,
    text="include special characters",
    variable=special_var,
    bg="#f5f5f5",
    anchor='w',
    width=20
)
cb2.pack(side='top', padx=10, pady=2)

# generate button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white")
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=300, bg="#f5f5f5", font=("Bree Serif", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
