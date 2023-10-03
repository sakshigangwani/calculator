import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="light blue")

# Create an entry widget for input
entry = tk.Entry(root, width=20, borderwidth=5, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create and place buttons on the grid
row_val = 1
col_val = 0

for button_text in buttons:
    if button_text == '=':
        button = tk.Button(root, text=button_text, padx=20, pady=20, command=calculate, font=("Helvetica", 16))
    elif button_text == 'C':
        button = tk.Button(root, text=button_text, padx=20, pady=20, command=clear, font=("Helvetica", 16))
    else:
        button = tk.Button(root, text=button_text, padx=20, pady=20, command=lambda num=button_text: button_click(num), font=("Helvetica", 16))
    
    button.grid(row=row_val, column=col_val, padx=10, pady=10)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter main loop
root.mainloop()
