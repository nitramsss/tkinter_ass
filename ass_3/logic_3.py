from tkinter import *

def bagel_choice_logic(bagel_value, pick_a_bagel):
    bagel_choice = bagel_value.get()
    if bagel_choice == 0:
        pick_a_bagel.config(text="white")
    else:
        pick_a_bagel.config(text="whole wheat")


def coffee_choice_logic(coffee_value, coffee_label, coffee_list):
    coffee_choice = coffee_value.get()
    if coffee_choice == 0:
        coffee_label.config(text=coffee_list[coffee_choice][0])
    elif coffee_choice == 1:
        coffee_label.config(text=coffee_list[coffee_choice][1])
    elif coffee_choice == 2:
        coffee_label.config(text=coffee_list[coffee_choice][1])
    else:
        coffee_label.config(text=coffee_list[coffee_choice][1])


def toppings_added():
    3






def close_window(window):
    window.destroy()

def reset_form():
    pass