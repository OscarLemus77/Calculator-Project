import tkinter as tk
from gui import CalculatorGUI


def main():
    window = tk.Tk()
    window.title('Calculator')
    window.geometry('500x750')
    window.resizable(False, False)

    application = CalculatorGUI(window)

    window.mainloop()

if __name__ == '__main__':
    main()
