from tkinter import *

window = Tk()
window.geometry("500x450")

title_frame = Frame(window)
title_frame.grid(column=0, row=0, pady=30, padx=30)
title_frame.grid_columnconfigure(0, weight=1)
title_frame.grid_rowconfigure(0, weight=1)


body_frame = Frame(window)
body_frame.grid(column=0, row=1, sticky="N")

left_body_frame = Frame(body_frame)
left_body_frame.grid(column=0, row=0, sticky="N")
right_body_frame = Frame(body_frame)
right_body_frame.grid(column=1, row=0, sticky="N")

# Title
Label(window, text="Brandi's Bagel House", font=("Times New Roman", 20, "italic")).grid(column=0, row=0)

# Pick a Bagel
pick_a_bagel = LabelFrame(left_body_frame, text="Pick a Bagel")
pick_a_bagel.grid(column=0, row=0, sticky="W", padx=10)


radio_checker = IntVar()

pick_a_bagel_list = ["White ($1.25)", 
                     "Whole Wheat ($1.50)"]

for i in range(len(pick_a_bagel_list)):
    Radiobutton(pick_a_bagel, text=pick_a_bagel_list[i], variable=radio_checker).grid(column=0, row=i, padx=10, pady=5, sticky="W")


# Pick Your Toppings
pick_your_toppings = LabelFrame(left_body_frame, text="Pick Your Toppings", pady=5)
pick_your_toppings.grid(column=0, row=1, sticky="W", padx=10, pady=10)

pick_your_toppings_list = ["Cream Chees ($.50)",
                           "Butter ($.25)",
                           "Blueberry Jam ($.75)",
                           "Raspberry Jam ($.75)",
                           "Peach Jelly ($.75)"]

for i in range(len(pick_your_toppings_list)):
    Checkbutton(pick_your_toppings, text=pick_your_toppings_list[i]).grid(column=0, row=i, sticky="W", padx=10, pady=5)


# Want Coffee with That?
want_coffee_with_that = LabelFrame(right_body_frame, text="Want Coffee with That?", padx=20)
want_coffee_with_that.grid(column=1, row=0, sticky="W")

want_coffee_with_that_list = ["None",
                              "Regular Coffee ($1.25)",
                              "Cappuccino ($2.00)",
                              "Caffe au lait ($1.75)"]

for i in range(len(want_coffee_with_that_list)):
    Radiobutton(want_coffee_with_that, text=want_coffee_with_that_list[i]).grid(column=0, row=i, sticky="W", padx=10, pady=5)



# Price 
price = LabelFrame(right_body_frame, text="Price", padx=15, pady=14)
price.grid(column=1, row=1, sticky="W", pady=10)

Label(price, text="Subtotal: ").grid(column=0, row=0)
Entry(price, state="disabled", width=15).grid(column=1, row=0, padx=10, pady=5, sticky="W")

Label(price, text="Tax: ").grid(column=0, row=1)
Entry(price, state="disabled", width=15).grid(column=1, row=1, padx=10, pady=5)

Label(price, text="Total: ").grid(column=0, row=2)
Entry(price, state="disabled", width=15).grid(column=1, row=2, padx=10, pady=5)


# Buttons
button_frame = Frame(body_frame, pady=10)
button_frame.grid(column=0, row=2, columnspan=2)

Button(button_frame, text="Calculate Total", width=10, padx=5, pady=5).grid(column=0, row=0, padx=10)
Button(button_frame, text="Reset Form", width=10, padx=5, pady=5).grid(column=1, row=0, padx=10)
Button(button_frame, text="Exit", width=10, padx=5, pady=5).grid(column=2, row=0, padx=10)



window.grid_columnconfigure(0, weight=1)
window.mainloop()