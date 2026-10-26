import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("320x450")
        self.root.resizable(False, False)
        self.root.config(bg="#1e1e1e")

        self.expression = ""

        # Input/Output Display
        self.display_text = tk.StringVar()
        
        display_frame = tk.Frame(self.root, bg="#1e1e1e")
        display_frame.pack(expand=True, fill="both")

        self.display = tk.Entry(
            display_frame, 
            textvariable=self.display_text, 
            font=("Arial", 24, "bold"), 
            bg="#2d2d2d", 
            fg="white", 
            bd=0, 
            justify="right"
        )
        self.display.pack(expand=True, fill="both", padx=10, pady=20)

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#1e1e1e")
        btn_frame.pack(expand=True, fill="both")

        # Button Layout Configuration
        buttons = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2)
        ]

        # Style parameters
        btn_font = ("Arial", 16)
        
        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(btn_frame, text=text, font=btn_font, bg="#ff9500", fg="white", bd=0,
                                command=self.calculate)
                btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
            elif text == 'C':
                btn = tk.Button(btn_frame, text=text, font=btn_font, bg="#a6a6a6", fg="black", bd=0,
                                command=self.clear)
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            else:
                bg_color = "#333333" if text in ('/', '*', '-', '+', '(', ')') else "#505050"
                fg_color = "#d22424" if text in ('/', '*', '-', '+') else "white"
                
                btn = tk.Button(btn_frame, text=text, font=btn_font, bg=bg_color, fg=fg_color, bd=0,
                                command=lambda t=text: self.on_button_click(t))
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        # Make grid cells expandable
        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)
        for i in range(4):
            btn_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        self.expression += str(char)
        self.display_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.display_text.set("")

    def calculate(self):
        try:
            # eval() safely evaluates the math string
            result = str(eval(self.expression))
            self.display_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            self.display_text.set("Error: Div by zero")
            self.expression = ""
        except Exception:
            self.display_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()