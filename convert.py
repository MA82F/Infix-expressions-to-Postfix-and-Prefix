from tkinter import *
import re

expression = ""
#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----
class PostConversion:

    def __init__(self):
        self.top = -1
        self.stack = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

#------------------------------------
    def isEmpty(self):
        if self.top == -1:
            return True 
        else:
            return False
 
#------------------------------------
    def peek(self):
        return self.stack[-1]
 
#------------------------------------
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.stack.pop()
        else:
            return 
 
#------------------------------------
    def push(self, op):
        self.top += 1
        self.stack.append(op)
 
#------------------------------------
    def isNumber(self, ch):
        return ch.isdigit()

#------------------------------------
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

#------------------------------------
    def infixToPostfix(self, exp):

        result = re.split(r'(\D)', exp)
        flag = False

        for i in result:
            if i=='':
                continue

            if self.isNumber(i):
                self.output.append(i)
                flag = TRUE
 
            elif i == '(':
                self.push(i)
 
            elif i == ')':
                while((not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                self.pop()

            elif flag == False:
                self.output.append('~')

            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
                flag = False
 
        while not self.isEmpty():
            self.output.append(self.pop())
 
        equation_postfix.set(self.output)
 

#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----
class PreConversion:
 
    def __init__(self):
        self.top = -1
        self.stack = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

#------------------------------------
    def isEmpty(self):
        if self.top == -1:
            return True 
        else:
            return False
 
#------------------------------------
    def peek(self):
        return self.stack[-1]
 
#------------------------------------
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.stack.pop()
        else:
            return

#------------------------------------
    def push(self, op):
        self.top += 1
        self.stack.append(op)
 
#------------------------------------
    def isNumber(self, ch):
        return ch.isdigit()
 
#------------------------------------
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a < b else False
        except KeyError:
            return False
#------------------------------------
    def infixToPrefix(self, exp):

        if exp[0] == '-':
            exp = '~' + exp[1:]

        result = re.split(r'(\D)', exp)
        result = result[::-1]

        for i in result:
            
            if i=='':
                continue

            if self.isNumber(i):
                self.output.append(i)
 
            elif i == ')':
                self.push(i)
 
            elif i == '(':
                while((not self.isEmpty()) and
                      self.peek() != ')'):
                    a = self.pop()
                    self.output.append(a)
                self.pop()
 
            else:
                while(not self.isEmpty() and self.notGreater(i) ):
                    self.output.append(self.pop())
                if len(self.output) == len(self.stack) and self.peek()== '-':
                    self.output.append ('~')
                    self.pop()
                self.push(i)      
            
        while not self.isEmpty():
            self.output.append(self.pop())
 
        self.output = self.output[::-1]
        equation_prefix.set(" ".join(self.output))




#--------GUI HANDELING-------------------------------
def press(num):
    global expression
    expression += str(num)
    equation_infix.set(expression)

#------------------------------------
def equalpress():
 
    try:
        global expression
        objPost = PostConversion()
        objPost.infixToPostfix(expression)

        objPre = PreConversion()
        objPre.infixToPrefix(expression)

        total = str(eval(expression))
        equation_infix.set(total)
 
        expression = ""
 
    except:
 
        equation_infix.set(" error ")
        equation_prefix.set("")
        equation_postfix.set("")
        expression = ""
 
#------------------------------------
def clear():
    global expression
    expression = ""
    equation_infix.set("")
    equation_prefix.set("")
    equation_postfix.set("")
 
########################################################################################################################
if __name__ == "__main__":

    gui = Tk()
    gui.configure(background="light green")
    gui.title("Calculator for convert infix to postfix and prefix")
    gui.geometry("300x300")

    equation_infix = StringVar()
    equation_prefix = StringVar()
    equation_postfix = StringVar()
 
    expression_field_Infix = Entry(gui, textvariable=equation_infix)
    expression_field_prefix = Entry(gui, textvariable=equation_prefix)
    expression_field_postfix = Entry(gui, textvariable=equation_postfix)
 
    expression_field_Infix.grid(columnspan=4, ipadx=70)
    expression_field_prefix.grid(columnspan=4, ipadx=70)
    expression_field_postfix.grid(columnspan=4, ipadx=70)

    button1 = Button(gui, text=' 1 ', fg='black', bg='skyblue',
                    command=lambda: press(1), height=1, width=7)
    button1.grid(row=5, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='skyblue',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=5, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='skyblue',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=5, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='skyblue',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=6, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='skyblue',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=6, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='skyblue',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=6, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='skyblue',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=7, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='skyblue',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=7, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='skyblue',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=7, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='skyblue',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=8, column=0)
 
    plus = Button(gui, text=' + ', fg='black', bg='skyblue',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=5, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='skyblue',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=6, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='skyblue',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=7, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='skyblue',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=8, column=3)
 
    equal = Button(gui, text=' = ', fg='black', bg='skyblue',
                command=equalpress, height=1, width=7)
    equal.grid(row=8, column=2)
 
    clear = Button(gui, text='Clear', fg='black', bg='skyblue',
                command=clear, height=1, width=7)
    clear.grid(row=8, column='1')
 
    emtyBtn= Button(gui, fg='black', bg='skyblue', height=1, width=7)
    emtyBtn.grid(row=9, column=0)

    openParentheses= Button(gui, text='(', fg='black', bg='skyblue',
                    command=lambda: press('('), height=1, width=7)
    openParentheses.grid(row=9, column=1)

    closeParentheses= Button(gui, text=')', fg='black', bg='skyblue',
                    command=lambda: press(')'), height=1, width=7)
    closeParentheses.grid(row=9, column=2)

    gui.mainloop()