import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0, calculation)


def evaluate_calcualtion():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")  
        text_result.insert(1.0, calculation) 

    except:
        clear_field()
        text_result.insert(1.0, "error")  


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")  



box = tk.Tk()
box.geometry("300x300")
box.title("Simple GUI Calculator")

text_result= tk.Text(box, height=2, width= 16, font=("Arial", 24) ,background="silver")
text_result.grid(columnspan=5)

button_1= tk.Button(box, text='1', command=lambda: add_to_calculation(1), width= 5, font= ("Arial", 14) , background= "yellow")
button_1.grid(row= 2, column=1)

button_2= tk.Button(box, text='2', command=lambda: add_to_calculation(2), width= 5, font= ("Arial", 14) , background= "grey")
button_2.grid(row= 2, column=2)

button_3= tk.Button(box, text='3', command=lambda: add_to_calculation(3), width= 5, font= ("Arial", 14) , background= "yellow")
button_3.grid(row= 2, column=3)

button_4= tk.Button(box, text='4', command=lambda: add_to_calculation(4), width= 5, font= ("Arial", 14), background= "grey")
button_4.grid(row= 3, column=1)

button_5= tk.Button(box, text='5', command=lambda: add_to_calculation(5), width= 5, font= ("Arial", 14) , background= "yellow")
button_5.grid(row= 3, column=2)

button_6= tk.Button(box, text='6', command=lambda: add_to_calculation(6), width= 5, font= ("Arial", 14) , background= "grey")
button_6.grid(row= 3, column=3)

button_7= tk.Button(box, text='7', command=lambda: add_to_calculation(7), width= 5, font= ("Arial", 14) , background= "yellow")
button_7.grid(row= 4, column=1)

button_8= tk.Button(box, text='8', command=lambda: add_to_calculation(8), width= 5, font= ("Arial", 14) , background= "grey")
button_8.grid(row= 4, column=2)

button_9= tk.Button(box, text='9', command=lambda: add_to_calculation(9), width= 5, font= ("Arial", 14) , background= "yellow")
button_9.grid(row= 4, column=3)

button_0= tk.Button(box, text='0', command=lambda: add_to_calculation(0), width= 5, font= ("Arial", 14) , background= "yellow")
button_0.grid(row= 5, column=2)

button_plus= tk.Button(box, text="+", command=lambda: add_to_calculation("+"), width= 5, font= ("Arial", 14) , background= "grey")
button_plus.grid(row= 2, column=4)

button_minus= tk.Button(box, text="-", command=lambda: add_to_calculation("-"), width= 5, font= ("Arial", 14) , background= "yellow")
button_minus.grid(row= 3, column=4)

button_multiply= tk.Button(box, text="x", command=lambda: add_to_calculation("*"), width= 5, font= ("Arial", 14) , background= "grey")
button_multiply.grid(row= 4, column=4)

button_divide= tk.Button(box, text="/", command=lambda: add_to_calculation("/"), width= 5, font= ("Arial", 14) , background= "yellow")
button_divide.grid(row= 5, column=4)

button_open= tk.Button(box, text="(", command=lambda: add_to_calculation("("), width= 5, font= ("Arial", 14) , background= "grey")
button_open.grid(row= 5, column=1)

button_close= tk.Button(box, text=")", command=lambda: add_to_calculation(")"), width= 5, font= ("Arial", 14) , background= "grey")
button_close.grid(row= 5, column=3)

button_equal= tk.Button(box, text="=", command= evaluate_calcualtion, width= 11, font= ("Arial", 14), background= "yellow")
button_equal.grid(row= 6, column= 1, columnspan=2)

button_clear= tk.Button(box, text="Clear", command= clear_field, width= 11, font= ("Arial", 14) , background= "grey")
button_clear.grid(row= 6, column=3, columnspan= 2)


box.mainloop()
