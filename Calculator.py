# Shawn's Python Calculator
# Version 1.0

import tkinter, operator
w = tkinter.Tk()
w.resizable(False, False)

# initilize varibles

ui_fir_num = "" # User input first number
fir_num = False # True if the first number is input completely
ui_sec_num = "" # User input second number
sec_num = False # True if the second number is input completely
ui_op = "" # User input operation
ui_op_next = "" # Place holder for user input on additional calculations
ui_reset_num = False # True if a number is input and should replace current ui_fir_num
dml_num = False #True when decimal is pressed,

# Sending calculator and keyboard button presses to gathering function
def press_numpad_1():
    gather_user_input(1)

def press_numpad_2():
    gather_user_input(2)

def press_numpad_3():
    gather_user_input(3)

def press_numpad_4():
    gather_user_input(4)

def press_numpad_5():
    gather_user_input(5)

def press_numpad_6():
    gather_user_input(6)

def press_numpad_7():
    gather_user_input(7)

def press_numpad_8():
    gather_user_input(8)

def press_numpad_9():
    gather_user_input(9)

def press_numpad_0():
    gather_user_input(0)

def press_numpad_dml():
    gather_user_input(".")

def press_numpad_add():
    gather_user_input("+")

def press_numpad_sub():
    gather_user_input("-")

def press_numpad_mul():
    gather_user_input("x")

def press_numpad_div():
    gather_user_input("÷")

def press_numpad_eql():
    gather_user_input("=")

def press_numpad_ent(event): #pressed enter on keyboard
    gather_user_input("=")

def press_numpad_c():
    gather_user_input("C")

def press_numpad_bck():
    gather_user_input("BCK")


# Gather user input and process for calculations

def gather_user_input(ui):
    global ui_fir_num, fir_num, ui_sec_num, sec_num, ui_op, ui_op_next, ui_reset_num, dml_num
    if type(ui) == int or ui == "." or ui == "BCK": #User Input of Integer/Decimal/Backspace Handler
        if ui_reset_num == True: # Allows user number to be reset if = is used and then numbers are pressed
            ui_fir_num = ""
            fir_num=False
            ui_reset_num = False
        if fir_num == False:    # Allowes user input to build first number
            if ui == "." and dml_num == False:
                ui_fir_num=ui_fir_num+str(ui)
                dml_num = True
            elif ui == "." and dml_num == True:
                pass
            elif ui == "BCK":
                ui_fir_num = ui_fir_num[:-1]
            elif len(ui_fir_num) >= 13:
                pass
            else:
                ui_fir_num = ui_fir_num + str(ui)
            output_screen.config(text=ui_fir_num) # Show first number being built on screen
        elif sec_num == False and ui_op != "":  # Allows user input to build second number
            if ui == "." and dml_num == False:
                ui_sec_num = ui_sec_num + str(ui)
                dml_num = True
            elif ui == "." and dml_num == True:
                pass
            elif ui == "BCK":
                ui_sec_num = ui_sec_num[:-1]
            elif len(ui_sec_num) >= 13:
                pass
            else:
                ui_sec_num =ui_sec_num+str(ui)
            output_screen.config(text=ui_fir_num + " " + ui_op + " " + ui_sec_num)
    elif type(ui) != int: #User Input of Non-Integer Handler
        dml_num = False
        if ui == "C": # Reset all variables if True
            ui_fir_num = ""
            fir_num = False
            ui_sec_num = ""
            sec_num = False
            ui_op = ""
            output_screen.config(text="You Are The Answer")
        elif ui_reset_num == True: # Allows user input of operators if = is used to solve problem
            if ui != "=":
                ui_op = ui
                ui_reset_num = False
                output_screen.config(text=ui_fir_num + " " + ui_op)
            else:
                ui_op = ""
                calculate_user_input(ui_fir_num, "+", 0)

        elif fir_num == False and ui_fir_num != "": # If true, this will lock in the first number and the operation to be performed
            fir_num = True
            if ui == "=": #User pressed enter or = with no operators
                ui_op = ""
                calculate_user_input(ui_fir_num, "+", 0)
            else:   # User used an operator after entering the first number
                ui_op = ui
                output_screen.config(text=ui_fir_num + " " + ui_op)
        elif sec_num == False and ui_sec_num != "": #If true, this will lock in the second number and send everything to be calculated
            sec_num = True
            if ui == "=": #User pressed enter or = after entering the first number and operator and the second number
                ui_op_next = ""
                print(ui_op_next)
                ui_reset_num = True
                calculate_user_input(ui_fir_num, ui_op, ui_sec_num)
            else: #User pressed an operator, so it is saved for use after current calculations are made
                ui_op_next = ui
                calculate_user_input(ui_fir_num, ui_op, ui_sec_num)
        else: #User entered something before any numbers have been processed

            if ui == "=":
                ui_op = ""
                calculate_user_input(ui_fir_num, "+", 0)
            else:
                ui_op = ui
                output_screen.config(text=ui_fir_num + " " + ui_op)



#Use processed user input and perform calculations
def calculate_user_input(ffnum, fop, fsnum):
    global ui_fir_num, fir_num, ui_sec_num,sec_num, ui_op, ui_op_next, ui_reset_num

    if fop == "+":
        curr_answer = operator.add(float(ffnum),float(fsnum))
    elif fop == "-":
        curr_answer = operator.sub(float(ffnum),float(fsnum))
    elif fop == "x":
        curr_answer = operator.mul(float(ffnum),float(fsnum))
    elif fop == "÷":
        curr_answer = operator.truediv(float(ffnum),float(fsnum))
    else:
        curr_answer = "ERROR"

    format(str(curr_answer))
    ui_fir_num = format(curr_answer, '.15g')

    if ui_op_next != "=":
        ui_op = str(ui_op_next)
        output_screen.config(text=ui_fir_num + " " + ui_op)
    else:
        ui_op = ""
        ui_reset_num = True
        output_screen.config(text=ui_fir_num)
    ui_sec_num = ""
    sec_num = False

# Numberpad for user input

numpad = tkinter.Frame(w)
numpad.pack(side="bottom")

numpad_button_height = 5
numpad_button_width = 10
numpad_button_font = "systemfixed"
numpad_button_font_size = 12


numpad_c = tkinter.Button(numpad, text="C", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width*2, command=press_numpad_c)
numpad_c.grid(row=0, column=0, columnspan=2, sticky="W")
numpad_bck = tkinter.Button(numpad, text="BCK", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_bck)
numpad_bck.grid(row=0, column=2, sticky="W")
numpad_add = tkinter.Button(numpad, text="+", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_add)
numpad_add.grid(row=0, column=3)


numpad_7 = tkinter.Button(numpad, text="7", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_7)
numpad_7.grid(row=1, column=0, sticky="W")
numpad_8 = tkinter.Button(numpad, text="8", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_8)
numpad_8.grid(row=1, column=1, sticky="W")
numpad_9 = tkinter.Button(numpad, text="9", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_9)
numpad_9.grid(row=1, column=2, sticky="W")
numpad_sub = tkinter.Button(numpad, text="-", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_sub)
numpad_sub.grid(row=1, column=3)

numpad_4 = tkinter.Button(numpad, text="4", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_4)
numpad_4.grid(row=2, column=0, sticky="W")
numpad_5 = tkinter.Button(numpad, text="5", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_5)
numpad_5.grid(row=2, column=1, sticky="W")
numpad_6 = tkinter.Button(numpad, text="6", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_6)
numpad_6.grid(row=2, column=2, sticky="W")
numpad_mul = tkinter.Button(numpad, text="x", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_mul)
numpad_mul.grid(row=2, column=3)


numpad_1 = tkinter.Button(numpad, text="1", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_1)
numpad_1.grid(row=3, column=0, sticky="W")
numpad_2 = tkinter.Button(numpad, text="2", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_2)
numpad_2.grid(row=3, column=1, sticky="W")
numpad_3 = tkinter.Button(numpad, text="3", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_3)
numpad_3.grid(row=3, column=2, sticky="W")


numpad_div = tkinter.Button(numpad, text="÷", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_div)
numpad_div.grid(row=3, column=3)

numpad_dml = tkinter.Button(numpad, text=".", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_dml)
numpad_dml.grid(row=4, column=0, sticky="W")
numpad_0 = tkinter.Button(numpad, text="0", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width, command=press_numpad_0)
numpad_0.grid(row=4, column=1, sticky="W")
numpad_eql = tkinter.Button(numpad, text="=", height=numpad_button_height, font=(numpad_button_font, numpad_button_font_size), width=numpad_button_width*2, command=press_numpad_eql)
numpad_eql.grid(row=4, column=2, columnspan=2, sticky="E")

#Keyboard monitor

def ui_keyboard(event):
    ui_keyboard_valid_num=["0","1","2","3","4","5","6","7","8","9"]
    ui_keyboard_valid_sym=["+","-","*","/","\b","."]
    if ui_keyboard_valid_num.count(event.char)> 0:
        run = "press_numpad_"+event.char+"()"
        exec(run)
    elif ui_keyboard_valid_sym.count(event.char)>0:
        if event.char == "+":
            press_numpad_add()
        if event.char == "-":
            press_numpad_sub()
        if event.char == "*":
            press_numpad_mul()
        if event.char == "/":
            press_numpad_div()
        if event.char == "\b":
            press_numpad_bck()
        if event.char == ".":
            press_numpad_dml()
    else:
        print(event.char)




#User input display area

display = tkinter.Frame(w)
display.pack(side="top")

display_height = 5
display_width = 30

output_screen = tkinter.Label(display, text="You Are The Answer", font=("SYSTEMFIXED", 16), borderwidth=5, relief="sunken", height= display_height, width=display_width, background="slate gray")
output_screen.pack()

w.bind("<Key>", ui_keyboard)
w.bind("<Return>", press_numpad_ent)
w.mainloop()
