from tkinter import *
root = Tk()
#Making text for the title bar
root.title('Simple calculator')

#Creating input space
e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

#Def function for what happens when you click a button
def button_click(number):
    #creating variable for current info in input space
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

#def function for clear button
def button_clear():
    e.delete(0, END)

#def function for add button
def button_add():
    first_number = e.get()
    #create global variable (can be called by multiple functions)
    global f_number
    global math
    math = 'addition'
    f_number = int(first_number)
    e.delete(0, END)

#def function for equal button
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == 'addition':
        e.insert(0, f_number + int(second_number))
    if math == 'subtraction':
        e.insert(0, f_number - int(second_number))
    if math == 'multiplication':
        e.insert(0, f_number * int(second_number))
    if math == 'division':
        e.insert(0, f_number / int(second_number))

def button_min():
    first_number = e.get()
    global math
    math = 'subtraction'
    f_number = int(first_number)
    e.delete(0, END)
    
def button_mul():
    first_number = e.get()
    global math
    math = 'multiplication'
    f_number = int(first_number)
    e.delete(0, END)
    
def button_div():
    first_number = e.get()
    global math
    math = 'division'
    f_number = int(first_number)
    e.delete(0, END)
    
    

#Creating buttons
butt_1 = Button(root, text = '7', padx = 40, pady = 20, command = lambda: button_click(7))
butt_2 = Button(root, text = '8', padx = 40, pady = 20, command = lambda: button_click(8))
butt_3 = Button(root, text = '9', padx = 40, pady = 20, command = lambda: button_click(9))
butt_4 = Button(root, text = '4', padx = 40, pady = 20, command = lambda: button_click(4))
butt_5 = Button(root, text = '5', padx = 40, pady = 20, command = lambda: button_click(5))
butt_6 = Button(root, text = '6', padx = 40, pady = 20, command = lambda: button_click(6))
butt_7 = Button(root, text = '1', padx = 40, pady = 20, command = lambda: button_click(1))
butt_8 = Button(root, text = '2', padx = 40, pady = 20, command = lambda: button_click(2))
butt_9 = Button(root, text = '3', padx = 40, pady = 20, command = lambda: button_click(3))
butt_0 = Button(root, text = '0', padx = 40, pady = 20, command = lambda: button_click(0))

butt_add = Button(root, text = '+', padx = 40, pady = 20, command = button_add)
butt_equal = Button(root, text = '=', padx = 40, pady = 20, command = button_equal)
butt_clear = Button(root, text = 'C', padx = 40, pady = 20, command = button_clear)
butt_min = Button(root, text = '-', padx = 40, pady = 20, command = button_min)
butt_mul = Button(root, text = '*', padx = 40, pady = 20, command = button_mul)
butt_div = Button(root, text = '/', padx = 40, pady = 20, command = button_div)

#Putting buttons in GUI
butt_1.grid(row = 1, column = 0)
butt_2.grid(row = 1, column = 1)
butt_3.grid(row = 1, column = 2)
butt_4.grid(row = 2, column = 0)
butt_5.grid(row = 2, column = 1)
butt_6.grid(row = 2, column = 2)
butt_7.grid(row = 3, column = 0)
butt_8.grid(row = 3, column = 1)
butt_9.grid(row = 3, column = 2)
butt_0.grid(row = 4, column = 1 )

butt_add.grid(row = 1, column = 3 )
butt_clear.grid(row = 4, column = 0 )
butt_equal.grid(row = 4, column = 2)
butt_min.grid(row = 2, column = 3)
butt_mul.grid(row = 3, column = 3)
butt_div.grid(row = 4, column = 3)

root.mainloop()
