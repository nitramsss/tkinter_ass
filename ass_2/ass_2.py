from tkinter import *
from logic_2 import operators_btn, clear_fields, close_window


def main():
    window = Tk()

    operator_frame = LabelFrame(window, text="Operators")
    operator_frame.grid(column=0, row=1)

    operation_frame = LabelFrame(window, text="Operation")
    operation_frame.grid(column=1, row=1)

    buttons_frame = Frame(window)
    buttons_frame.grid(column=1, row=2)

    Label(window, text="Simple Calculator", font=("Arial", 12, "bold")).grid(column=0, row=0, padx=20, pady=20)

    # Operators
    plus_btn = Button(operator_frame, text="+", width=5, command=lambda: operators_btn(result, operand_1, operand_2, operator, "+")).grid(column=0, row=0, padx=5, pady=5)
    minus_btn = Button(operator_frame, text="-", width=5, command=lambda: operators_btn(result, operand_1, operand_2, operator, "-")).grid(column=1, row=0, padx=5, pady=5)
    multiply_btn = Button(operator_frame, text="*", width=5, command=lambda: operators_btn(result, operand_1, operand_2, operator, "*")).grid(column=0, row=1, padx=5, pady=5)
    division_btn = Button(operator_frame, text="/", width=5, command=lambda: operators_btn(result, operand_1, operand_2, operator, "/")).grid(column=1, row=1, padx=5, pady=5)
    division_2_btn = Button(operator_frame, text="\\", width=5, command=lambda: operators_btn(result, operand_1, operand_2, operator, "\\")).grid(column=0, row=2, padx=5, pady=5)
    square_btn = Button(operator_frame, text="^", width=5, command=lambda: operators_btn(result, operand_1, operand_2, operator, "^")).grid(column=1, row=2, padx=5, pady=5)
    modulo_btn = Button(operator_frame, text="Mod", width=12,command=lambda: operators_btn(result, operand_1, operand_2, operator, "%")).grid(column=0, row=3, columnspan=2, padx=5, pady=5)

    # Operations
    label_1 = Label(operation_frame, text="Operand 1: ")
    label_1.grid(column=0, row=0, padx=5, pady=5)

    operand_1 = Entry(operation_frame, width=15)
    operand_1.grid(column=1, row=0, padx=5, pady=5)

    operator = Entry(operation_frame, width=5, state="readonly")
    operator.grid(column=1, row=1, padx=5, pady=5)

    label_2 = Label(operation_frame, text="Operand 2: ")
    label_2.grid(column=0, row=2, padx=5, pady=5)

    operand_2 = Entry(operation_frame, width=15)
    operand_2.grid(column=1, row=2, padx=5, pady=5)

    label_3 = Label(operation_frame, text="Result")
    label_3.grid(column=0, row=3, padx=5, pady=5)

    result = Entry(operation_frame, state="disabled", width=15)
    result.grid(column=1, row=3, padx=5, pady=5)


    # Buttons
    clear_btn = Button(buttons_frame, text="Clear", width=10, command=lambda: clear_fields(operator, operand_1, operand_2, result))
    clear_btn.grid(column=0, row=0, padx=10, pady=10)

    exit_btn = Button(buttons_frame, text="Exit", width=10, command=lambda: close_window(window))
    exit_btn.grid(column=1, row=0, padx=10, pady=10)

    window.mainloop()


if __name__ == "__main__":
    main()