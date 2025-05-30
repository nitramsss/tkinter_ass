from tkinter import *

def operators_btn(result, operand_1, operand_2, operator_widget, operator):
    operator_widget.config(state="normal")
    operator_widget.delete(0, END)
    operator_widget.insert(0, operator)
    operator_widget.config(state="readonly")
    
    solve_result(result, operand_1, operand_2, operator)

def solve_result(result_widget, operand_1, operand_2, operator):
    operator_logic = operator
    operand_1_logic = operand_1.get()
    operand_2_logic = operand_2.get()

    if operator_logic == "+":
        result = float(operand_1_logic) + float(operand_2_logic) 
    elif operator_logic == "-":
        result = float(operand_1_logic) - float(operand_2_logic) 
    elif operator_logic == "*":
        result = float(operand_1_logic) * float(operand_2_logic) 
    elif operator_logic == "/":
        result = float(operand_1_logic) / float(operand_2_logic) 
    elif operator_logic == "\\":
        result = float(operand_1_logic) / float(operand_2_logic) 
    elif operator_logic == "^":
        result = float(operand_1_logic) ** float(operand_2_logic) 
    else:
        result = float(operand_1_logic) % float(operand_2_logic) 

    display_result(result, result_widget)
    
    
def display_result(result, result_widget):
    result_widget.config(state="normal")
    result_widget.delete(0, END)
    result_widget.insert(0, result)
    result_widget.config(state="readonly")

def clear_fields(operator, operand_1, operand_2, result_widget):
    operator.config(state="normal")
    operator.delete(0, END)
    operator.config(state="readonly")

    operand_1.config(state="normal")
    operand_1.delete(0, END)

    operand_2.config(state="normal")
    operand_2.delete(0, END)

    result_widget.config(state="normal")
    result_widget.delete(0, END)
    result_widget.config(state="readonly")

def close_window(root):
    root.destroy()