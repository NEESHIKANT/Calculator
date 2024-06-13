import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Calculator')
frame = tk.Frame(master=window, bg="black", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=0,
                 width=30, bg="black", fg="white")
entry.grid(row=0, column=0, columnspan=3, ipady=25, pady=20)


def myclick(val):
    entry.insert(tk.END,f'{val} ')
    
def equal():
    try:
        elements = entry.get().split()
        result = eval(''.join(elements))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")


def clear():
    entry.delete(0, tk.END)

def backspace():
    current_text = entry.get()
    if current_text:
        entry.delete(len(current_text) - 1)

def add_decimal():
    current_text = entry.get()
    elements = current_text.split()
    if elements:
        if '.' not in elements[-1]:
            entry.insert(tk.END, '.')
    else:
        entry.insert(tk.END, '.')


button_1 = tk.Button(master=frame, text='1', padx=20,
                                        pady=5, width=3, command=lambda: myclick(1), bg='grey', fg='white',
                                        font=('Helvetica', '10', 'bold'))
button_1.grid(row=4, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2', padx=20,
                                        pady=5, width=3, command=lambda: myclick(2), bg='grey', fg='white',
                                        font=('Helvetica', '10', 'bold'))
button_2.grid(row=4, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3', padx=20,
                                        pady=5, width=3, command=lambda: myclick(3), bg='grey', fg='white',
                                        font=('Helvetica', '10', 'bold'))
button_3.grid(row=4, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4', padx=20,
                                        pady=5, width=3, command=lambda: myclick(4), bg='grey', fg='white',
                                        font=('Helvetica', '10', 'bold'))
button_4.grid(row=3, column=0, pady=2)
button_5 = tk.Button(master=frame, text='5', padx=20,
                                        pady=5, width=3, command=lambda: myclick(5), bg='grey', fg='white',
                                        font=('Helvetica', '10', 'bold'))
button_5.grid(row=3, column=1, pady=2)
button_6 = tk.Button(master=frame, text='6', padx=20,
                                        pady=5, width=3, command=lambda: myclick(6), bg='grey', fg='white',
                                        font=('Helvetica', '10', 'bold'))
button_6.grid(row=3, column=2, pady=2)
button_7 = tk.Button(master=frame, text='7', padx=20,
                                        pady=5, width=3, command=lambda: myclick(7), bg='grey', fg='white',
                                        font=('Helvetica', '10', 'bold'))
button_7.grid(row=2, column=0, pady=2)
button_8 = tk.Button(master=frame, text='8', padx=20,
                                        pady=5, width=3, command=lambda: myclick(8), bg='grey', fg='white',
                                        font=('Helvetica', '10', 'bold'))
button_8.grid(row=2, column=1, pady=2)
button_9 = tk.Button(master=frame, text='9', padx=20,
                                        pady=5, width=3, command=lambda: myclick(9), bg='grey', fg='white',
                                        font=('Helvetica', '10', 'bold'))
button_9.grid(row=2, column=2, pady=2)
button_0 = tk.Button(master=frame, text='0', padx=20,
                                        pady=5, width=3, command=lambda: myclick(0), bg='grey', fg='white',
                                        font=('Helvetica', '10', 'bold'))
button_0.grid(row=5, column=0, pady=2)

button_add = tk.Button(master=frame, text="+", padx=20,
                       pady=5, width=3, command=lambda: myclick('+'), bg='grey', fg='white',
                       font=('Helvetica', '10', 'bold'))
button_add.grid(row=4, column=3, pady=2)

button_subtract = tk.Button(
    master=frame, text="-", padx=20, pady=5, width=3, command=lambda: myclick('-'), bg='grey', fg='white',
    font=('Helvetica', '10', 'bold'))
button_subtract.grid(row=3, column=3, pady=2)

button_multiply = tk.Button(
    master=frame, text="X", padx=20, pady=5, width=3, command=lambda: myclick('*'), bg='grey', fg='white',
    font=('Helvetica', '10', 'bold'))
button_multiply.grid(row=2, column=3, pady=2)

button_div = tk.Button(master=frame, text="÷", padx=20,
                       pady=5, width=3, command=lambda: myclick('/'), bg='grey', fg='white',
                       font=('Helvetica', '10', 'bold'))
button_div.grid(row=1, column=3, pady=2)

button_clear = tk.Button(master=frame, text="AC",
                         padx=20, pady=5, width=3, command=clear, bg='red', fg='white',
                         font=('Helvetica', '10', 'bold'))
button_clear.grid(row=1, column=0, pady=2)

button_backspace = tk.Button(master=frame, text='←', padx=20, pady=5, width=3, command=backspace, bg='grey', fg='white',
                             font=('Helvetica', '10', 'bold'))
button_backspace.grid(row=1, column=2, pady=2)

button_decimal = tk.Button(master=frame, text='.', padx=20, pady=5, width=3, command=add_decimal, bg='grey', fg='white',
                           font=('Helvetica', '10', 'bold'))
button_decimal.grid(row=1, column=1, pady=2)


button_equal = tk.Button(master=frame, text="=", padx=20,
                         pady=5, width=19, command=equal, bg='orange', fg='white',
                         font=('Helvetica', '10', 'bold'))
button_equal.grid(row=5, column=1, columnspan=3, pady=2)

window.mainloop()
