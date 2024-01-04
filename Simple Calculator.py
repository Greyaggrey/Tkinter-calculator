#importing tkinter module
from tkinter import*
window =Tk()
window.title('Calculator')

#calculator window width and height
window.geometry('355x475')

#background color and icon 
window.configure(bg='#8cff1a')
window.iconbitmap('calc.ico')

#static calculator size
window.resizable(False,False)


#press function when user clicks on a button to display variables
expression=''
def press(num):
    global expression

    expression=expression + str(num)

    equation.set(expression)

#Built in function eval solves expression and returns value to string format.When equal is pressed it returns total
#try and except solves values solves equations that cannot be expressed.e.g 2/0
def equalpress():
    global expression

    try:

        total=str(eval(expression))
        equation.set(total)

        expression=''
    except:
      equation.set('error')
      expression=''
      
#This function clears content when clicked hence displays '0'    
def clear():
    global expresssion

    expression=''
    equation.set('0')

#Creation of frame for easy entry of buttons in the entry box 
button_frame=Frame(window,bg='#8cff1a')
button_frame.pack()

equation=StringVar()
equation.set('0')

#textvariable takes user entry and justify for display of figures to the right
expression_field =Entry(button_frame,textvariable=equation,
                        justify='right',font=('arial',20,'bold'))
expression_field.pack()


#Creation of buttons ,relief for border type and lambda to pass a press function 
button1 = Button(button_frame,text='1',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press(1))

button2 = Button(button_frame,text='2',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press(2))

button3 = Button(button_frame,text='3',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press(3))

addition = Button(button_frame,text='+',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press('+'))

button4 = Button(button_frame,text='4',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press(4))

button5 = Button(button_frame,text='5',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press(5))

button6 = Button(button_frame,text='6',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press(6))

subtract = Button(button_frame,text='-',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press('-'))

button7 = Button(button_frame,text='7',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press(7))

button8 = Button(button_frame,text='8',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press(8))

button9 = Button(button_frame,text='9',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press(9))

multiply = Button(button_frame,text='*',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press('*'))

button0 = Button(button_frame,text='0',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press(0))

decimal = Button(button_frame,text='.',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press('.'))

clear = Button(button_frame,text='C',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=clear)

division = Button(button_frame,text='/',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=8,height=3,command=lambda:press('/'))

equal = Button(button_frame,text='=',font=('times new roman',12),
                 relief='ridge',bd=1,bg='#59b300',width=35,height=3,command=equalpress)

#Grid for columns and rows for button position ipad x and y for separation of buttons from display
expression_field.grid(row=0,column=0,columnspan=4,ipadx=8,ipady=25,pady=15)

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
addition.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
subtract.grid(row=2,column=3)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
multiply.grid(row=3,column=3)

button0.grid(row=4,column=0)
decimal.grid(row=4,column=1)
clear.grid(row=4,column=2)
division.grid(row=4,column=3)

equal.grid(row=5,column=0,columnspan=4)

window.mainloop()
