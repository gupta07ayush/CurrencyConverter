from currency_converter import CurrencyConverter
import tkinter as tk

a = CurrencyConverter()
# print(a.convert(12,"USD","INR"))

window = tk.Tk()
window.title("Currency Converter")
window.geometry("500x360")
window.configure(bg='#C1C1CD')

l1=tk.Label(window,bg="#FFACAC",text="Currency Converter", font= "Times 25 bold ").place(x=100,y=0)
l2=tk.Label(window,bg="#FFACAC",text="Enter Amount: ",font="Times, 13").place(x=50,y=50)
e1= tk.Entry(window,bg="#FFBFA9",font="Times 12")

l3=tk.Label(window,bg="#FFACAC",text="From Currency: ",font="Times, 13").place(x=50,y=100)
e2= tk.Entry(window,bg="#FFBFA9",font="Times 12")
l4=tk.Label(window,bg="#FFACAC",text="To Currency: ",font="Times, 13").place(x=50,y=145)

def clicked():
    amount = int(e1.get())
    cur1 = e2.get().upper()
    cur2 = e3.get().upper()
    data = a.convert(amount,cur1,cur2)
    l5 =tk.Label(window,font="Times 20 bold",text=data).place(x=200,y=290)

e3= tk.Entry(window,bg="#FFBFA9",font="Times 12")

b1 =tk.Button(window, bg="#FFACAC",font="arial 15 bold",text="Convert", command=clicked).place(x=230,y=240)

e1.place(x=220,y=55)
e2.place(x=220,y=105)
e3.place(x=220,y=150)

window.mainloop()