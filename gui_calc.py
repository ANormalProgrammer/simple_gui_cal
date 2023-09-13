import tkinter as tk


root = tk.Tk()

display = tk.Entry(root, width=30)
display.grid(row = 0, column = 0, columnspan=4)


global mode
mode = "none"
global first_number 
first_number = 0

display.insert(0, '0')

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

def is_string_only_zero(string):
    for idx in string:
        if idx != '0':
            return False
    return True

def add_character_to_dispay(new_number):
    current_text = display.get()
    delete_display()

    if(not current_text or is_string_only_zero(current_text)):
        if new_number == '.':
            add_display(current_text + new_number)
        else:
            add_display(new_number)
            
    else:
        add_display(current_text + new_number)
        

def do_plus_mode():
    global mode
    global first_number
    if  mode == "none":
        first_number = float(display.get())
        mode = "plus"
        delete_display()
        
def do_minus_mode():
    global mode
    global first_number
    if  mode == "none":
        first_number = float(display.get())
        mode = "minus"
        delete_display()

def do_mutiply_mode():
    global mode
    global first_number
    if  mode == "none":
        first_number = float(display.get())
        mode = "mutiply"
        delete_display()

def do_divide_mode():
    global mode
    global first_number
    if  mode == "none":
        first_number = float(display.get())
        mode = "divide"
        delete_display()

def do_equal_mode():
    global mode
    global first_number
    if mode == "plus":
        second_number = float(display.get())
        result = first_number + second_number
        delete_display()
        add_display(str(result))
        first_number = result
        mode = "none"
    elif mode == "minus":
        second_number = float(display.get())
        result = first_number - second_number
        delete_display()
        add_display(str(result))
        first_number = result
        mode = "none"
    elif mode == "mutiply":
        second_number = float(display.get())
        result = first_number * second_number
        delete_display()
        add_display(str(result))
        first_number = result
        mode = "none"
    elif mode == "divide":
        second_number = float(display.get())
        result = first_number / second_number
        delete_display()
        add_display(str(result))
        first_number = result
        mode = "none"



def button_0():
    print("button 0 clicked")
    add_character_to_dispay("0")

def button_1():
    print("button 1 clicked")
    add_character_to_dispay("1")

def button_2():
    print("button 2 clicked")
    add_character_to_dispay("2")

def button_3():
    print("button 3 clicked")
    add_character_to_dispay("3")

def button_4():
    print("button 4 clicked")
    add_character_to_dispay("4")

def button_5():
    print("button 5 clicked")
    add_character_to_dispay("5")

def button_6():
    print("button 6 clicked")
    add_character_to_dispay("6")

def button_7():
    print("button 7 clicked")
    add_character_to_dispay("7")

def button_8():
    print("button 8 clicked")
    add_character_to_dispay("8")

def button_9():
    print("button 9 clicked")
    add_character_to_dispay("9")

def button_plus():
    print("button + clicked")
    do_plus_mode() 

def button_minus():
    print("button - clicked")
    do_minus_mode() 
    
def button_mutiply():
    print("button * clicked")
    do_mutiply_mode()
    
def button_divide():
    print("button / clicked")
    do_divide_mode()

def button_dot():
    print("button . clicked")
    add_character_to_dispay(".")

def button_equal():
    print("button = clicked")
    do_equal_mode() 


buttons = [
    ('7', 1, 0, button_7), ('8', 1, 1, button_8),   ('9', 1, 2, button_9),     ('/', 1, 3, button_divide),
    ('4', 2, 0, button_4), ('5', 2, 1, button_5),   ('6', 2, 2, button_6),     ('*', 2, 3, button_mutiply),
    ('1', 3, 0, button_1), ('2', 3, 1, button_2),   ('3', 3, 2, button_3),     ('-', 3, 3, button_minus),
    ('0', 4, 0, button_0), ('.', 4, 1, button_dot), ('=', 4, 2, button_equal), ('+', 4, 3, button_plus),
]
for button_data in buttons:
    create_button(root, *button_data)

root.mainloop()

root.mainloop()

