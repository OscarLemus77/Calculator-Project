import tkinter as tk
import calculator

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x700")
        self.root.resizable(False, False)

        # Entry widget for the arithmetic calculator
        self.entry = tk.Entry(self.root, width=30, borderwidth=15, font=('Arial', 30), justify='right', bg="white", fg="red", state="readonly")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Configure grid layout for buttons
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1, uniform="equal")
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1, uniform="equal")
        #I took this idea from this video https://www.youtube.com/watch?v=rNBrbt90bRk

        # Create buttons for arithmetic operations
        self.create_buttons()

        # Add a Frame for Shape-Based Calculator
        self.frame_shape = tk.Frame(self.root)
        self.frame_shape.grid(row=5, column=0, columnspan=4, pady=20)

        # Add Radio buttons for selecting the shape
        self.radio_1 = tk.IntVar()
        self.radio_1.set(0)
        self.radio_circle = tk.Radiobutton(self.frame_shape, text="Circle", variable=self.radio_1, value=1, command=self.update_shape)
        self.radio_square = tk.Radiobutton(self.frame_shape, text="Square", variable=self.radio_1, value=2, command=self.update_shape)
        self.radio_rectangle = tk.Radiobutton(self.frame_shape, text="Rectangle", variable=self.radio_1, value=3, command=self.update_shape)
        self.radio_triangle = tk.Radiobutton(self.frame_shape, text="Triangle", variable=self.radio_1, value=4, command=self.update_shape)

        self.radio_circle.grid(row=0, column=0)
        self.radio_square.grid(row=0, column=1)
        self.radio_rectangle.grid(row=0, column=2)
        self.radio_triangle.grid(row=0, column=3)

        # Labels and entries for shape calculations
        self.label_first = tk.Label(self.frame_shape, text='')
        self.label_second = tk.Label(self.frame_shape, text='')
        self.entry_first = tk.Entry(self.frame_shape, width=15)
        self.entry_second = tk.Entry(self.frame_shape, width=15)

        self.label_first.grid(row=1, column=0)
        self.entry_first.grid(row=1, column=1)
        self.label_second.grid(row=2, column=0)
        self.entry_second.grid(row=2, column=1)

        # Calculate button for area calculation
        self.button_calculate = tk.Button(self.frame_shape, text="Calculate", command=self.calculate)
        self.button_calculate.grid(row=3, column=0, columnspan=4)

        self.label_result = tk.Label(self.frame_shape, text="", font=("Arial", 14), fg="black")
        self.label_result.grid(row=4, column=0, columnspan=4)



    def create_buttons(self):
        buttons = ['7', '8', '9', '/',
                   '4', '5', '6', '*',
                   '1', '2', '3', '-',
                   '0', 'C', '=', '+']

        row = 1
        col = 0
        for button in buttons:
            self.create_button(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    # I took this idea from this video https://www.youtube.com/watch?v=rNBrbt90bRk



    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, padx=15, pady=15, font=('Arial', 18),
                           fg="blue", state="normal", activebackground="black", relief='raised', bd=3,
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, sticky="nsew")


    def on_button_click(self, char):
        self.entry.config(state="normal")
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                result = self.calculation(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.entry.config(state="readonly")
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, f"Error: {str(e)}")
        else:
            self.entry.insert(tk.END, char)


    def calculation(self, expression):
        try:
            # First, check if the expression contains only numbers and valid operators
            valid_characters = "0123456789+-*/."
            for char in expression:
                if char not in valid_characters:
                    return "Invalid Expression"
            result = eval(expression)
            return result

        except ZeroDivisionError:
            return "Error: Division by Zero"
        except ValueError:
            return "Error: Invalid input"
        except SyntaxError:
            return "Error: Invalid syntax"
        except TypeError:
            return "Error: Invalid data type"


    def update_shape(self):
        # Reset the shape-related inputs and results
        self.entry_first.delete(0, tk.END)
        self.entry_second.delete(0, tk.END)
        self.label_result.config(text='')

        shape_type = self.radio_1.get()

        if shape_type == 1:  # Circle
            self.label_first.config(text="Radius")
            self.label_second.config(text="")
            self.entry_second.grid_forget()
        elif shape_type == 2:  # Square
            self.label_first.config(text="Side")
            self.label_second.config(text="")
            self.entry_second.grid_forget()
        elif shape_type == 3:  # Rectangle
            self.label_first.config(text="Length")
            self.label_second.config(text="Width")
            self.entry_second.grid(row=2, column=1)
        elif shape_type == 4:  # Triangle
            self.label_first.config(text="Base")
            self.label_second.config(text="Height")
            self.entry_second.grid(row=2, column=1)


    def calculate(self):
        try:
            first_num = self.entry_first.get()
            second_num = self.entry_second.get()
            shape = self.radio_1.get()

            if shape == 1:
                self.label_result.config(text=f'Circle area = {calculator.circle(first_num)}')
            elif shape == 2:
                self.label_result.config(text=f'Square area = {calculator.square(first_num)}')
            elif shape == 3:
                self.label_result.config(text=f'Rectangle area = {calculator.rectangle(first_num, second_num)}')
            elif shape == 4:
                self.label_result.config(text=f'Triangle area = {calculator.triangle(first_num, second_num)}')
            else:
                self.label_result.config(text='No operation selected')
        except ValueError:
            self.label_result.config(text='Enter numeric values')
        except TypeError:
            self.label_result.config(text='Values must be positive')
