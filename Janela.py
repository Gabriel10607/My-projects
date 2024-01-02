from tkinter import *

janela = Tk()
janela.title('Média de dois números')
num1 = Label(janela, text='Insira um número:')
num1.grid(column=0, row=0)
num2 = Label(janela, text='Insira outro número:')
num2.grid(column=0, row=1)
janela.geometry('400x400')
texto = Entry(janela, background='white', width=9, font='Arial 9')
texto.place(x=107, y=4)
texto2 = Entry(janela, background='white', width=9, font='Arial 9')
texto2.place(x=115, y=24)
janela.mainloop()
