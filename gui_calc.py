import tkinter as tk

def button_0():
    print("button 0 clicked")
    add_character_to_display("0")

def button_1():
    print("button 1 clicked")
    add_character_to_display("1")

def button_2():
    print("button 2 clicked")
    add_character_to_display("2")

def button_3():
    print("button 3 clicked")
    add_character_to_display("3")

def button_4():
    print("button 4 clicked")
    add_character_to_display("4")

def button_5():
    print("button 5 clicked")
    add_character_to_display("5")

def button_6():
    print("button 6 clicked")
    add_character_to_display("6")

def button_7():
    print("button 7 clicked")
    add_character_to_display("7")

def button_8():
    print("button 8 clicked")
    add_character_to_display("8")

def button_9():
    print("button 9 clicked")
    add_character_to_display("9")

def button_plus():
    print("button + clicked")
    do_operator_mode("plus")

def button_minus():
    print("button - clicked")
    do_operator_mode("minus")

    
def button_mutiply():
    print("button * clicked")
    do_operator_mode("mutiply")
    
def button_divide():
    print("button / clicked")
    do_operator_mode("divide")

def button_dot():
    print("button . clicked")
    add_character_to_display(".")

def button_equal():
    print("button = clicked")
    do_equal_mode() 

def on_enter(e):
    e.widget['background'] = '#fafafa'

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'


def create_button(root, text, row, col, command=None):
    button = tk.Button(root, text = text, padx = 20, pady = 20, command = command)
    button.grid(row = row, column = col)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    return button

def delete_display():
    display.delete(0, tk.END)

def add_display(text):
    display.insert(0, text)
    
def default_display():
    delete_display()
    add_display(0)
    
def is_string_only_zero(string):
    for idx in string:
        if idx != '0':
            return False
    return True

def add_character_to_display(new_number):
    if(mode == "operator_input"): 
        return
    current_text = display.get()
    delete_display()

    if(not current_text or is_string_only_zero(current_text)):
        if new_number == '.':
            add_display(current_text + new_number)
        else:
            add_display(new_number)
            
    else:
        add_display(current_text + new_number)
        
def do_operator_mode(input_mode):
    global mode
    global first_number
    if  mode == "number_input" or mode == "operator_input":
        first_number = float(display.get())
        mode = input_mode
        default_display()
        
def do_equal_mode():
    global mode
    global first_number
    second_number = float(display.get())

    if mode == "plus":
        result = first_number + second_number
    elif mode == "minus":
        result = first_number - second_number
    elif mode == "mutiply":
        result = first_number * second_number
    elif mode == "divide":
        result = first_number / second_number
        
    delete_display()
    add_display(str(result))
    first_number = result
    mode = "operator_input"
    
root = tk.Tk()

display = tk.Entry(root, width=30)
display.grid(row = 0, column = 0, columnspan=4)


global mode
mode = "number_input"
global first_number 
first_number = 0

default_display()

buttons = [
    ('7', 1, 0, button_7), ('8', 1, 1, button_8),   ('9', 1, 2, button_9),     ('/', 1, 3, button_divide),
    ('4', 2, 0, button_4), ('5', 2, 1, button_5),   ('6', 2, 2, button_6),     ('*', 2, 3, button_mutiply),
    ('1', 3, 0, button_1), ('2', 3, 1, button_2),   ('3', 3, 2, button_3),     ('-', 3, 3, button_minus),
    ('0', 4, 0, button_0), ('.', 4, 1, button_dot), ('=', 4, 2, button_equal), ('+', 4, 3, button_plus),
]
for button_data in buttons:
    create_button(root, *button_data)

root.mainloop()

