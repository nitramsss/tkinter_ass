from tkinter import *

window = Tk()

operator_frame = LabelFrame(window, text="Operators")
operator_frame.grid(column=0, row=1)

operation_frame = LabelFrame(window, text="Operation")
operation_frame.grid(column=1, row=1)

buttons_frame = Frame(window)
buttons_frame.grid(column=1, row=2)

Label(window, text="Simple Calculator", font=("Arial", 12, "bold")).grid(column=0, row=0, padx=20, pady=20)

# Operators
Button(operator_frame, text="+", width=5).grid(column=0, row=0, padx=5, pady=5)
Button(operator_frame, text="-", width=5).grid(column=1, row=0, padx=5, pady=5)
Button(operator_frame, text="*", width=5).grid(column=0, row=1, padx=5, pady=5)
Button(operator_frame, text="/", width=5).grid(column=1, row=1, padx=5, pady=5)
Button(operator_frame, text="\\", width=5).grid(column=0, row=2, padx=5, pady=5)
Button(operator_frame, text="^", width=5).grid(column=1, row=2, padx=5, pady=5)
Button(operator_frame, text="Mod", width=12).grid(column=0, row=3, columnspan=2, padx=5, pady=5)

# Operations
Label(operation_frame, text="Operand 1: ").grid(column=0, row=0, padx=5, pady=5)
Entry(operation_frame, width=15).grid(column=1, row=0, padx=5, pady=5)
Entry(operation_frame, state="disabled", width=5).grid(column=1, row=1, padx=5, pady=5)

Label(operation_frame, text="Operand 2: ").grid(column=0, row=2, padx=5, pady=5)
Entry(operation_frame, width=15).grid(column=1, row=2, padx=5, pady=5)
Label(operation_frame, text="Result").grid(column=0, row=3, padx=5, pady=5)
Entry(operation_frame, state="disabled", width=15).grid(column=1, row=3, padx=5, pady=5)


# Buttons
Button(buttons_frame, text="Clear", width=10).grid(column=0, row=0, padx=10, pady=10)
Button(buttons_frame, text="Exit", width=10).grid(column=1, row=0, padx=10, pady=10)



window.mainloop()