from currency_converter import CurrencyConverter
import tkinter as tk

a = CurrencyConverter()
# print(a.convert(12,"USD","INR"))

window = tk.Tk()
window.title("Currency Converter")
window.geometry("500x500")
window.configure(bg='#C1C1CD')

l1=tk.Label(window,bg="#ff9999",text="Currency Converter", font= "Verdana 27 bold ").place(x=0,y=28 , width=500, height=60)
l2=tk.Label(window,bg="#FFACAC",text="Enter Amount: ",font="Times, 15").place(x=50,y=105, width=150)
e1= tk.Entry(window,bg="#FFBFA9",font="Times 15 bold")

l3=tk.Label(window,bg="#FFACAC",text="From Currency: ",font="Times, 15").place(x=50,y=155)
e2= tk.Entry(window,bg="#FFBFA9",font="Times 15")
l4=tk.Label(window,bg="#FFACAC",text="To Currency: ",font="Times, 15").place(x=50,y=200, width=150)

def clicked():
    amount = int(e1.get())
    cur1 = e2.get().upper()
    cur2 = e3.get().upper()
    data = a.convert(amount,cur1,cur2)
    l5 =tk.Label(window,font="Times 20 bold",text=data, bg="pink", fg="black" ).place(x=0,y=350, width=500)

e3= tk.Entry(window,bg="#FFBFA9",font="Times 15")

b1 =tk.Button(window, bg="#FF8080",font="arial 18 bold",text="Convert", command=clicked).place(x=150,y=290,width=200)

e1.place(x=220,y=105)
e2.place(x=220,y=155)
e3.place(x=220,y=200)
e1.focus_set()
e2.insert(0,"USD")
e3.insert(0,"INR")

l7 =tk.Label(window,font="Times 12 bold",text="", bg="black", fg="black" ).place(x=0,y=0, width=500)
l6 =tk.Label(window,font="Times 15 bold",text="", bg="black", fg="black" ).place(x=0,y=475, width=500)

tk.mainloop()
