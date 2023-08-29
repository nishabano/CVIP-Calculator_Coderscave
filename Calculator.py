import tkinter as tk
calculation=""
def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
    
        calculation=str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")

root=tk.Tk()
root.geometry("275x290")
root.resizable(0,0)
root.title("Calculator")
root.configure(background="black")
root.iconbitmap(r'C:\Users\Lenovo\Documents\Python\Tkinter\icon.ico')

text_result=tk.Text(root,bg="black",fg="white",height=2,width=15,font=("Arial",24))
text_result.grid(columnspan=5)

b1=tk.Button(root,text="1",bg="#2a2d36",fg="white", command=lambda: add_to_calculation(1),width=5,font=("Arial",14))
b1.grid(row=2,column=1 ,pady=2)

b2=tk.Button(root,text="2",bg="#2a2d36",fg="white",command=lambda: add_to_calculation(2),width=5,font=("Arial",14))
b2.grid(row=2,column=2)

b3=tk.Button(root,text="3",bg="#2a2d36",fg="white",command=lambda: add_to_calculation(3),width=5,font=("Arial",14))
b3.grid(row=2,column=3)

b4=tk.Button(root,text="4",bg="#2a2d36",fg="white",command=lambda: add_to_calculation(4),width=5,font=("Arial",14))
b4.grid(row=3,column=1)

b5=tk.Button(root,text="5",bg="#2a2d36",fg="white",command=lambda: add_to_calculation(5),width=5,font=("Arial",14))
b5.grid(row=3,column=2,pady=2)

b6=tk.Button(root,text="6",bg="#2a2d36",fg="white",command=lambda: add_to_calculation(6),width=5,font=("Arial",14))
b6.grid(row=3,column=3)

b7=tk.Button(root,text="7",bg="#2a2d36",fg="white",command=lambda: add_to_calculation(7),width=5,font=("Arial",14))
b7.grid(row=4,column=1,pady=2)

b8=tk.Button(root,text="8",bg="#2a2d36",fg="white",command=lambda: add_to_calculation(8),width=5,font=("Arial",14))
b8.grid(row=4,column=2)

b9=tk.Button(root,text="9",bg="#2a2d36",fg="white",command=lambda: add_to_calculation(9),width=5,font=("Arial",14))
b9.grid(row=4,column=3,pady=2)

b0=tk.Button(root,text="0",bg="#2a2d36",fg="white",command=lambda: add_to_calculation(0),width=5,font=("Arial",14))
b0.grid(row=5,column=2)

btn_plus=tk.Button(root,text="+",bg="darkorange",fg="white",command=lambda: add_to_calculation("+"),width=5,font=("Arial",14,"bold"))
btn_plus.grid(row=2,column=4)

btn_minus=tk.Button(root,text="-",bg="darkorange",fg="white",command=lambda: add_to_calculation("-"),width=5,font=("Arial",14,"bold"))
btn_minus.grid(row=3,column=4)

btn_mul=tk.Button(root,text="*",bg="darkorange",fg="white",command=lambda: add_to_calculation("*"),width=5,font=("Arial",14 ,"bold"))
btn_mul.grid(row=4,column=4)

btn_div=tk.Button(root,text="/",bg="darkorange",fg="white",command=lambda: add_to_calculation("/"),width=5,font=("Arial",14,"bold"))
btn_div.grid(row=5,column=4)

btn_open=tk.Button(root,text="(",bg="#2a2d36",fg="white",command=lambda: add_to_calculation("("),width=5,font=("Arial",14))
btn_open.grid(row=5,column=1,pady=2)

btn_close=tk.Button(root,text=")",bg="#2a2d36",fg="white",command=lambda: add_to_calculation(")"),width=5,font=("Arial",14))
btn_close.grid(row=5,column=3)

btn_clear=tk.Button(root,text="C",bg="red",fg="white",command=clear_field,width=11,font=("Arial", 14))
btn_clear.grid(row=6,column=1, columnspan=2)

btn_equals=tk.Button(root,text="=",bg="green",fg="white",command=evaluate_calculation,width=11,font=("Arial",14))
btn_equals.grid(row=6,column=3,columnspan=2)

root.mainloop()
