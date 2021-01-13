from tkinter import *
import tkinter.messagebox
from datetime import date


d0 = date.today()
d1 = date(2022, 10, 2)
deposto = d1 - d0

deposto.days

#criação da janela e titulo
menu_inicial = Tk()
menu_inicial.title('mais de 200 mil mortes...')

#tamanho e permissões quanto a dimensões, também setando quais as dimensões máximas e mínimas
menu_inicial.geometry('880x620')
menu_inicial.resizable(True, True)
menu_inicial.iconbitmap('imagens/icon.ico')
menu_inicial['bg'] = 'white'

#botão
bt = Button(menu_inicial, text='Quantos dias faltam pro bolsonaro sair do poder?', command=lambda: tkinter.messagebox.showinfo('faltam...', deposto.days))
bt.place(x=0, y=500)
bt.pack()



menu_inicial.mainloop()