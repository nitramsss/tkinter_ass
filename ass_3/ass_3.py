from tkinter import *
from logic_3 import bagel_choice_logic, close_window, coffee_choice_logic, toppings_added

def main():
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


    bagel_value = IntVar()

    bagel_list = [("White", 1.25), ("Whole Wheat", 1.50)]

    for i, tup in enumerate(bagel_list):
        bagel_choice = Radiobutton(pick_a_bagel, text=f"{tup[0]} (${tup[1]})", variable=bagel_value, value=i)
        bagel_choice.config(command=lambda: bagel_choice_logic(bagel_value, pick_a_bagel))
        bagel_choice.grid(column=0, row=i, padx=10, pady=5, sticky="W")
        bagel_choice.config(command=lambda: toppings_added())

    # Pick Your Toppings
    pick_your_toppings = LabelFrame(left_body_frame, text="Pick Your Toppings", pady=5)
    pick_your_toppings.grid(column=0, row=1, sticky="W", padx=10, pady=10)

    toppings_list = [("Cream Chees", .50),
                            ("Butter", .25),
                            ("Blueberry Jam",.75),
                            ("Raspberry Jam", .75),
                            ("Peach Jelly", .75)]
    
    toppings_added = []

    for i, tup in enumerate(toppings_list):
        toppings_choice = Checkbutton(pick_your_toppings, text=f"{tup[0]} (${tup[1]})")
        
        toppings_choice.grid(column=0, row=i, sticky="W", padx=10, pady=5)


    # Want Coffee with That?
    want_coffee_with_that = LabelFrame(right_body_frame, text="Want Coffee with That?", padx=20)
    want_coffee_with_that.grid(column=1, row=0, sticky="W")

    coffee_list = [("None",),
                   ("Regular Coffee", 1.25),
                   ("Cappuccino", 2.00),
                   ("Caffe au lait", 1.75)]

    coffee_choice = IntVar()
    for i, tup in enumerate(coffee_list):
        coffee = Radiobutton(want_coffee_with_that, text=f"{tup[0]} (${tup[1]})" if len(tup) > 1 else f"{tup[0]}", variable=coffee_choice, value=i)
        coffee.config(command=lambda: coffee_choice_logic(coffee_choice, want_coffee_with_that, coffee_list))
        coffee.grid(column=0, row=i, sticky="W", padx=10, pady=5)



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

    calculate_btn = Button(button_frame, text="Calculate Total", width=10, padx=5, pady=5)
    calculate_btn.grid(column=0, row=0, padx=10)
    
    reset_btn = Button(button_frame, text="Reset Form", width=10, padx=5, pady=5)
    reset_btn.grid(column=1, row=0, padx=10)
    
    exit_btn = Button(button_frame, text="Exit", width=10, padx=5, pady=5)
    exit_btn.config(command=lambda: close_window(window))
    exit_btn.grid(column=2, row=0, padx=10)

    window.grid_columnconfigure(0, weight=1)
    window.mainloop()

if __name__ == "__main__":
    main()