from tkinter import *

main_window =Tk()

# labels
Label(main_window, text="Enter Link to text list").grid(row = 0, column = 0)

Label(main_window, text="Enter Link to YAML file").grid(row = 1,column =0)

 # Text Input

link = Entry(main_window, width=50, borderwidth = 5)
link.grid(row = 0, column = 1)

yaml = Entry(main_window, width=50, borderwidth = 5)
yaml.grid(row = 1, column = 1)

def on_click():
    print(f"{link.get()}, {yaml.get()}")

#Buttons
Button(main_window, text= "Execute Process(s)", command = on_click ).grid(row = 2, column = 1)
main_window.mainloop()