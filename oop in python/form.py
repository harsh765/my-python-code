import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Student Information")
root.geometry("400x250")

# create labels for the fields
roll_no_label = ttk.Label(root, text="Roll No:")
city_label = ttk.Label(root, text="City:")
gender_label = ttk.Label(root, text="Gender:")
hobbies_label = ttk.Label(root, text="Hobbies:")

# create entry field for roll no
roll_no_entry = ttk.Entry(root, width=30)

# create radio buttons for gender
gender_var = tk.StringVar()
male_radio = ttk.Radiobutton(root, text="Male", variable=gender_var, value="male")
female_radio = ttk.Radiobutton(root, text="Female", variable=gender_var, value="female")

# create dropdown menu for hobbies
hobbies_options = ["Reading", "Sports", "Music", "Travel"]
hobbies_var = tk.StringVar()
hobbies_combobox = ttk.Combobox(root, textvariable=hobbies_var, values=hobbies_options)

# create buttons for save and cancel
save_button = ttk.Button(root, text="Save")
cancel_button = ttk.Button(root, text="Cancel")

# place all the widgets on the screen using grid layout
roll_no_label.grid(column=0, row=0, padx=10, pady=10)
roll_no_entry.grid(column=1, row=0, padx=10, pady=10)
city_label.grid(column=0, row=1, padx=10, pady=10)
gender_label.grid(column=0, row=2, padx=10, pady=10)
male_radio.grid(column=1, row=2, padx=10, pady=10)
female_radio.grid(column=2, row=2, padx=10, pady=10)
hobbies_label.grid(column=0, row=3, padx=10, pady=10)
hobbies_combobox.grid(column=1, row=3, padx=10, pady=10)
save_button.grid(column=0, row=4, padx=10, pady=10)
cancel_button.grid(column=1, row=4, padx=10, pady=10)

root.mainloop()
