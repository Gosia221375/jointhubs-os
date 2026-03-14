import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.num1_label = tk.Label(root, text="First Number:")
        self.num1_label.pack()
        self.num1_entry = tk.Entry(root)
        self.num1_entry.pack()

        self.num2_label = tk.Label(root, text="Second Number:")
        self.num2_label.pack()
        self.num2_entry = tk.Entry(root)
        self.num2_entry.pack()

        self.result_label = tk.Label(root, text="Result:")
        self.result_label.pack()
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(root, textvariable=self.result_var, state='readonly')
        self.result_entry.pack()

        self.add_button = tk.Button(root, text="Add", command=self.add)
        self.add_button.pack(side=tk.LEFT)

        self.subtract_button = tk.Button(root, text="Subtract", command=self.subtract)
        self.subtract_button.pack(side=tk.LEFT)

        self.multiply_button = tk.Button(root, text="Multiply", command=self.multiply)
        self.multiply_button.pack(side=tk.LEFT)

        self.divide_button = tk.Button(root, text="Divide", command=self.divide)
        self.divide_button.pack(side=tk.LEFT)

    def get_numbers(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")
            return None, None

    def add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            result = add(num1, num2)
            self.result_var.set(str(result))

    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            result = subtract(num1, num2)
            self.result_var.set(str(result))

    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            result = multiply(num1, num2)
            self.result_var.set(str(result))

    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            result = divide(num1, num2)
            self.result_var.set(str(result))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()