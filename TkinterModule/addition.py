import tkinter as tk

def add_numbers():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input")
        
def mul_numbers():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input")

window = tk.Tk()
window.title("Add Two Numbers")
window.geometry('300x200')

# First number input
label_num1 = tk.Label(window, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

# Second number input
label_num2 = tk.Label(window, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Add button
button_add = tk.Button(window, text="Add", command=add_numbers)
button_add.grid(row=2, column=0, columnspan=2, pady=10)
button_mul = tk.Button(window, text="Product", command=mul_numbers)
button_mul.grid(row=2, column=1, columnspan=2, pady=10)
# Result label
label_result = tk.Label(window, text="Result:")
label_result.grid(row=3, column=0, columnspan=2, pady=5)

window.mainloop()
