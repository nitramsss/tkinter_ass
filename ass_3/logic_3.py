from tkinter import *

bagel_price = None
def bagel_choice_logic(bagel_value, tup):
    bagel_choice = bagel_value.get()
    if bagel_choice == 0:
        bagel_price = tup[1]
    else:
        bagel_price = tup[1]

coffee_price = None
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

toppings_price = []
def toppings_added(price):
    global toppings
    toppings.append(price)



def calculate():





def close_window(window):
    window.destroy()

def reset_form():
    pass