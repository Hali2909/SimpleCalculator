import tkinter as tk
import backendcalculator

finestra = tk.Tk()
finestra.title("calcolatrice")
finestra.geometry("400x400")


input_text = tk.StringVar()
display = tk.Entry(finestra, textvariable=input_text, font="arial", justify="right", bg="#e6e6e6")
display.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=10)

def click(event):
    testo = event.widget.cget("text")
    if testo == '=':
        input_text.set((backendcalculator.calcola(input_text.get())))
    elif testo == 'C':
        input_text.set("")
    else:
        input_text.set(input_text.get() + testo)
    


#creo i bottoni
pulsanti = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    
]

for riga in pulsanti:
    frame = tk.Frame(finestra)
    frame.pack(expand=True)

    for simbolo in riga:    
        tk.Button()
        btn = tk.Button(frame, text=simbolo, font="Arial 18", width=5, heigh=2, bg="pink", fg="white")
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

finestra.mainloop()