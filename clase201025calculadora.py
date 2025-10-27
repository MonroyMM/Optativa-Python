import tkinter as tk
'''
def calculaoper(ss=0):
    i = ss.find('+')
    num1 = float(ss[0:i])
    num2 = float(ss[i+1:])
    print(num1+num2)
'''
def calculasuma(ss=0):
    numeros=[]
    operadores=[]
    num=''

    for i in ss:
        if i in '+-':
            numeros.append(float(num))
            operadores.append(i)
            num=''
        else:
            num=str(num)+str(i)
    numeros.append(float(num))
    
    res=numeros[0]
    i=0
    while i<len(operadores):
        if operadores[i] == '+':
            res = res + numeros[i+1]
        elif operadores[i]=='-':
            res = res - numeros[i+1]
        i=i+1
    print(res)
    return res

def button_click(button_name):
    global ss
    if button_name == '=':
        print(ss)
        resultado= calculasuma(ss)
        ss=''
    else:
        ss= ss + button_name

        
root = tk.Tk() #definir la ventana, en vez de window
root.title("Calculadora") #título de la ventana
ss=''
#lamdda ayuda a llamar a la función

b1 = tk.Button(root, text="1", command=lambda: button_click("1"))
b2 = tk.Button(root, text="2", command=lambda: button_click("2"))
b3 = tk.Button(root, text="3", command=lambda: button_click("3"))
b4 = tk.Button(root, text="4", command=lambda: button_click("4"))
b5 = tk.Button(root, text="5", command=lambda: button_click("5"))
b6 = tk.Button(root, text="6", command=lambda: button_click("6"))
b7 = tk.Button(root, text="7", command=lambda: button_click("7"))
b8 = tk.Button(root, text="8", command=lambda: button_click("8"))
b9 = tk.Button(root, text="9", command=lambda: button_click("9"))
b0 = tk.Button(root, text="0", command=lambda: button_click("0"))
mas = tk.Button(root, text="+", command=lambda: button_click("+"))
menos = tk.Button(root, text="-", command=lambda: button_click("-"))
igual = tk.Button(root, text="=", command=lambda: button_click("="))

b1.grid(row=0, column=0, padx=5, pady=5) 
b2.grid(row=0, column=1, padx=5, pady=5)
b3.grid(row=0, column=2, padx=5, pady=5)
b4.grid(row=1, column=0, padx=5, pady=5)
b5.grid(row=1, column=1, padx=5, pady=5)
b6.grid(row=1, column=2, padx=5, pady=5)
b7.grid(row=2, column=0, padx=5, pady=5)
b8.grid(row=2, column=1, padx=5, pady=5)
b9.grid(row=2, column=2, padx=5, pady=5)
b0.grid(row=3, column=0, padx=5, pady=5)
mas.grid(row=3, column=1, padx=5, pady=5)
menos.grid(row=3, column=2, padx=5, pady=5)
igual.grid(row=4, column=0, padx=5, pady=5)
# Start the Tkinter event loop
root.mainloop()