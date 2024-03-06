from tkinter import *  # label, entry, button

class Calculator:
    def __init__(self):
        root = Tk()
        root.title("CALCULATOR")
        root.iconphoto(False, PhotoImage(file="calculator icon.png"))
        # r.geometry("335x335") # for calculator

        self.input = Entry(root, bg= "white", fg="black", font=("Arial", 20))
        self.input.grid(ipady= 10, columnspan=4) #columnspan is for merging.. here 4 represents that 4 column boxes are merged

        row= 0
        col=0
        for i in range(1,10):
            #btn = Button(r, text=str(i), )
            btn= Button(root, text=str(i), bg="white", font=("Arial", 20), command= lambda var=str(i) : self.btn_to_sc(var))
            btn.grid(row = 4-row, column=col, ipadx=23)
            col+=1
            if col>2:
                row+=1
                col=0

        row_op=0
        op= "+ - * /".split(" ")
        for i in op:
            if i == "+":
                btn = Button(root, text=i, bg="white", fg="blue", font=("Arial", 20), command= lambda var= str(i) : self.btn_to_sc(var))
                btn.grid(row=row_op+1, column=3, ipadx=20)
                    
            else:
                btn = Button(root, text=i, bg="white", fg="blue", font=("Arial", 20), command= lambda var= str(i) : self.btn_to_sc(var))
                btn.grid(row=row_op+1, column=3, ipadx=23)
                
            row_op+=1

        btn0 = Button(text="0", bg="white", font=("Arial", 20), command= lambda: self.btn_to_sc("0"))
        btn0.grid(row = 5, column=0, ipadx=23)

        btn_decimal = Button(text=".", bg="white", font=("Arial", 20), command= lambda: self.btn_to_sc("."))
        btn_decimal.grid(row = 5, column=1, ipadx=26)

        btnC = Button(text="C", bg="white", fg= "blue", font=("Arial", 20), command= lambda: self.input.delete(0, END))
        btnC.grid(row = 1, column=0, columnspan=2, ipadx=63)

        btn_back = Button(text="<=", bg="white", fg= "blue", font=("Arial", 20), command= self.backButton)
        btn_back.grid(row = 1, column=2, ipadx=14)

        btn_equals = Button(text="=", bg="green", fg="white" ,font=("Arial", 20), command=  self.equals)
        btn_equals.grid(row = 5, column=2, columnspan=2, ipadx=63)

        root.mainloop()

    def btn_to_sc(self, text):
        self.input.insert(END, text)

    # def CButton(self):
    #     self.input.delete(0, END)

    def backButton(self):
        a=self.input.get()
        self.input.delete(len(a)-1)

    def equals(self):
        scr = self.input.get()
        try:
            calculated = eval(scr)
        except Exception as e:
            print(f"exception is => {type(e).__name__}:{e}")
            calculated= "Error"
        finally:
            self.input.delete(0, END)  
            self.input.insert(END,calculated)

          
calc= Calculator() 
#we don't have to call __init__() function. When class is assigned to object __init__() function is executed automatically.
