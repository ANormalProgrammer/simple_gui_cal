import tkinter as tk

def create_button(root, text, row, col, command=None):
    button = tk.Button(root, text = text, padx = 20, pady = 20, command = command)
    button.grid(row = row, column = col)
    return button

def add_number_to_dispay(new_number):
    current_text = display.get()
    new_text = current_text + new_number
    display.delete(0, tk.END)
    display.insert(0, new_text)

def delete_display():
    display.delete(0, tk.END)
    
def add_display(text):
    display.insert(0, text)
    

global operation
operation = "none"
global first_number 
first_number = 0
    
def do_plus_operation():
    global operation
    global first_number
    if  operation == "none":
        first_number =  int(display.get())
        operation = "plus"
        delete_display()
        
        
def do_equal_operation():
    global operation
    global first_number
    if operation == "plus":
        second_number = int(display.get())
        result = first_number + second_number
        delete_display()
        add_display(str(result))
        first_number = result
        operation = "none"
    
def button_0():
    print("button 0 clicked")
    add_number_to_dispay("0")

def button_1():
    print("button 1 clicked")
    add_number_to_dispay("1")
    
def button_2():
    print("button 2 clicked")
    add_number_to_dispay("2")
    
def button_3():
    print("button 3 clicked")
    add_number_to_dispay("3")
    
def button_4():
    print("button 4 clicked")
    add_number_to_dispay("4")

def button_5():
    print("button 5 clicked")
    add_number_to_dispay("5")
    
def button_6():
    print("button 6 clicked")
    add_number_to_dispay("6")
    
def button_7():
    print("button 7 clicked")
    add_number_to_dispay("7")
    
def button_8():
    print("button 8 clicked")
    add_number_to_dispay("8")
    
def button_9():
    print("button 9 clicked")
    add_number_to_dispay("9")
    
def button_plus():
    print("button + clicked")
    do_plus_operation() 
    
def button_plus():
    print("button + clicked")
    do_plus_operation() 

def button_equal():
    print("button = clicked")
    do_equal_operation() 
    
root = tk.Tk()

display = tk.Entry(root, width=30)
display.grid(row = 0, column = 0, columnspan=4)

buttons = [
    ('7', 1, 0, button_7), ('8', 1, 1, button_8), ('9', 1, 2, button_9),
    ('4', 2, 0, button_4), ('5', 2, 1, button_5), ('6', 2, 2, button_6),
    ('1', 3, 0, button_1), ('2', 3, 1, button_2), ('3', 3, 2, button_3), ('+', 4, 3, button_plus),
    ('0', 4, 0, button_0), ('=', 4, 2, button_equal)
]
for button_data in buttons:
    create_button(root, *button_data)

root.mainloop()

