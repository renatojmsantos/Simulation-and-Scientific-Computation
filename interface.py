from tkinter import *
import simulador


def show_entry_fields():
    s = simulador.Simulador(float(e1.get()), float(e2.get()), float(e3.get()), float(e4.get()), float(e5.get()),
                            float(e6.get()), float(e7.get()), float(e8.get()), float(e9.get()), float(e10.get()),
                            float(e11.get()), float(e12.get()), float(e13.get()), float(e14.get()), float(e15.get()),
                            float(e16.get()), float(e17.get()), float(e18.get()))
    s.executa()


interface = Tk()
interface.title('SIMULADOR FÁBRICA DE MÓVEIS')

"""
titulo = Label(interface,text = "SIMULADOR FÁBRICA DE MÓVEIS")

fonte = ('helvetica',20,'bold')
titulo.configure(font=fonte,height=10,width = 40)
titulo.pack()
"""

Label(interface, text="Tempo de Simulacao: ").grid(row=2)

Label(interface, text="Media de Chegada A: ").grid(row=3)
Label(interface, text="Media de Chegada B: ").grid(row=4)

Label(interface, text="Media Perfuracao A: ").grid(row=5)
Label(interface, text="Desvio Perfuracao A: ").grid(row=6)

Label(interface, text="Media Polimento A: ").grid(row=7)
Label(interface, text="Desvio Polimento A: ").grid(row=8)

Label(interface, text="Media Perfuracao B: ").grid(row=9)
Label(interface, text="Desvio Perfuracao B: ").grid(row=10)

Label(interface, text="Media Polimento B: ").grid(row=11)
Label(interface, text="Desvio Polimento B: ").grid(row=12)

Label(interface, text="Media Envernizamento: ").grid(row=13)
Label(interface, text="Desvio Envernizamento: ").grid(row=14)

Label(interface, text="Numero de maquinas Perfuracao A: ").grid(row=15)
Label(interface, text="Numero de maquinas Polimento A: ").grid(row=16)

Label(interface, text="Numero de maquinas Perfuracao B: ").grid(row=17)
Label(interface, text="Numero de maquinas Polimento B: ").grid(row=18)

Label(interface, text="Numero de maquinas para Envernizamento: ").grid(row=19)

e1 = Entry(interface)
e2 = Entry(interface)
e3 = Entry(interface)
e4 = Entry(interface)
e5 = Entry(interface)
e6 = Entry(interface)
e7 = Entry(interface)
e8 = Entry(interface)
e9 = Entry(interface)
e10 = Entry(interface)
e11 = Entry(interface)
e12 = Entry(interface)
e13 = Entry(interface)
e14 = Entry(interface)
e15 = Entry(interface)
e16 = Entry(interface)
e17 = Entry(interface)
e18 = Entry(interface)

e1.insert(10, "9600")  #"Tempo de simulacao"   9600 min -> funcionamento durante um mes

e2.insert(10, "5")  # Media de chegada A"
e3.insert(10, "1.33") # media chegada B

e4.insert(10, "2")   # media perfuracao A
e5.insert(10, "0.7")   # desvio perf A

e6.insert(10, "4")  # Media pol A
e7.insert(10, "1.2") # desvio pol A

e8.insert(10, "0.75")  #media perf B
e9.insert(10, "0.3") #desvio perf B

e10.insert(10, "3")   # media pol B
e11.insert(10, "1")  # desvio pol B

e12.insert(10, "1.4") # media env
e13.insert(10, "0.3") # desvio env

e14.insert(10, "1") # numero maquinas perf A
e15.insert(10, "1") # num maquinas pol A

e16.insert(10, "1") # num maquinas perf B
e17.insert(10, "2") # num maquinas pol B

e18.insert(10,"2") # num maquinas Env

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row=4, column=1)
e4.grid(row=5, column=1)
e5.grid(row=6, column=1)
e6.grid(row=7, column=1)
e7.grid(row=8, column=1)
e8.grid(row=9, column=1)
e9.grid(row=10, column=1)
e10.grid(row=11, column=1)
e11.grid(row=12, column=1)
e12.grid(row=13, column=1)
e13.grid(row=14, column=1)
e14.grid(row=15, column=1)
e15.grid(row=16, column=1)
e16.grid(row=17, column=1)
e17.grid(row=18, column=1)
e18.grid(row=19, column=1)

Button(interface, text='Quit', command=interface.quit).grid(row=20, column=0, sticky=W, pady=6)
Button(interface, text='RUN', command=show_entry_fields).grid(row=20, column=2, sticky=W, pady=10)

mainloop()