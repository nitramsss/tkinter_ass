from tkinter import *


def check_answer():
    if int(answer_entry.get()) == (15-(1+2+3+5)):
        answer_label.config(text="You got it!")
                            

window = Tk()

frame = Frame(window)
frame.grid(column=1, row=0, padx=20, pady=20)

question_label = Label(frame, text="Enter value of integer N : ")
question_label.grid(column=0, row=0)

answer_entry = Entry(frame, width=30)
answer_entry.grid(column=1, row=0)

answer_label = Label(frame, text="The sum is 1 + 2 + 3 + _ + 5 = 15", width=30)
answer_label.grid(column=1, row=1, pady=5)

submit_button = Button(frame, text="Validate", width=25, command=check_answer)
submit_button.grid(column=1, row=2)

window.mainloop()

