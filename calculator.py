import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator")

        self.expression = ""

        self.display = tk.Entry(root, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            ("%", 1, 0), ("CE", 1, 1), ("C", 1, 2), ("⌫", 1, 3),
            ("1/x", 2, 0), ("x²", 2, 1), ("√x", 2, 2), ("÷", 2, 3),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("×", 3, 3),
            ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("-", 4, 3),
            ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("+", 5, 3),
            ("±", 6, 0), ("0", 6, 1), (".", 6, 2), ("=", 6, 3)
        ]

        for (text, row, col) in buttons:
            if text == "=":
                button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), bg="blue", fg="white", command=self.calculate)
            else:
                button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        for i in range(7):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "CE":
            self.expression = self.expression[:-1]
        elif char == "±":
            if self.expression and self.expression[0] == "-":
                self.expression = self.expression[1:]
            else:
                self.expression = "-" + self.expression
        else:
            self.expression += char
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def calculate(self):
        try:
            result = eval(self.expression.replace("×", "*").replace("÷", "/"))
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.expression = ""
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()