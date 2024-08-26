import tkinter as tk

# create a new window
root = tk.Tk()
root.title("Calculator")

# define the calculation function
def calculate():
    # get the first number from the user
    num1 = float(num1_var.get())
    
    # get the second number from the user
    num2 = float(num2_var.get())
    
    # perform the calculation based on the operation selected
    if operation_var.get() == "+":
        result = num1 + num2
    elif operation_var.get() == "-":
        result = num1 - num2
    elif operation_var.get() == "*":
        result = num1 * num2
    elif operation_var.get() == "/":
        result = num1 / num2
    else:
        result = "Invalid operation"
    
    # update the result label
    result_var.set(result)

# create the number input fields and labels
num1_label = tk.Label(root, text="Number 1:")
num1_label.grid(row=0, column=0)

num1_var = tk.StringVar()
num1_entry = tk.Entry(root, textvariable=num1_var)
num1_entry.grid(row=0, column=1)

num2_label = tk.Label(root, text="Number 2:")
num2_label.grid(row=1, column=0)

num2_var = tk.StringVar()
num2_entry = tk.Entry(root, textvariable=num2_var)
num2_entry.grid(row=1, column=1)

# create the operation check boxes and label
operation_label = tk.Label(root, text="Operation:")
operation_label.grid(row=2, column=0)

operation_var = tk.StringVar()
add_checkbox = tk.Checkbutton(root, text="+", variable=operation_var, onvalue="+")
add_checkbox.grid(row=2, column=1)

subtract_checkbox = tk.Checkbutton(root, text="-", variable=operation_var, onvalue="-")
subtract_checkbox.grid(row=2, column=2)

multiply_checkbox = tk.Checkbutton(root, text="*", variable=operation_var, onvalue="*")
multiply_checkbox.grid(row=2, column=3)

divide_checkbox = tk.Checkbutton(root, text="/", variable=operation_var, onvalue="/")
divide_checkbox.grid(row=2, column=4)

# create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=2)

# create the result label
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0)

result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var)
result_entry.grid(row=4, column=1)

# start the main event loop
root.mainloop()
