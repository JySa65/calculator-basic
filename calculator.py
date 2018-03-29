#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import pyttsx3

speak = pyttsx3.init("espeak",True)
speak.setProperty('voice',"spanish")

class Calculator():
    """ Una pequeña calculadora que que te el resultado de operaciones basica"""
    def __init__(self):
        """ Iniciamos la el pyttsx3 y el tkinter """
        print("Esta Corriendo")
        self.hablar = speak
        self.raiz = Tk()
        self.raiz.geometry('240x300')
        self.raiz.resizable(width=False,height=False)
        self.raiz.title('Calculadora V=2018 :D')
        self.raiz.config(bg="white")
        self.form(self.raiz)
        self.raiz.mainloop()
        print("Fin App")

    def form(self, raiz):
        """ Se crea el form que estara dentro de la ventana"""
        self.text1en = StringVar()
        self.text1 = Text(raiz,font="12")
        self.text1.place(x=20, y=20, height=30, width=200)
        self.button1 = Button(self.raiz, text='1', command = lambda : self.say(1), font="12").place(x=20,y=60,width=40,height=40)
        self.button2 = Button(self.raiz, text='2', command = lambda : self.say(2), font="12").place(x=70,y=60,width=40,height=40)
        self.button3 = Button(self.raiz, text='3', command = lambda : self.say(3), font="12").place(x=120,y=60,width=40,height=40)
        self.buttonmas = Button(self.raiz, text='+', command = lambda : self.say("mas", "+"), font="12").place(x=170,y=60,width=40,height=40)
        self.button4 = Button(self.raiz, text='4', command = lambda : self.say(4), font="12").place(x=20,y=110,width=40,height=40)
        self.button5 = Button(self.raiz, text='5', command = lambda : self.say(5), font="12").place(x=70,y=110,width=40,height=40)
        self.button6 = Button(self.raiz, text='6', command = lambda : self.say(6), font="12").place(x=120,y=110,width=40,height=40)
        self.buttonmenos = Button(self.raiz, text='-', command = lambda : self.say("menos", "-"), font="12").place(x=170,y=110,width=40,height=40)
        self.button7 = Button(self.raiz, text='7', command = lambda : self.say(7), font="12").place(x=20,y=160,width=40,height=40)
        self.button8 = Button(self.raiz, text='8', command = lambda : self.say(8), font="12").place(x=70,y=160,width=40,height=40)
        self.button9 = Button(self.raiz, text='9', command = lambda : self.say(9), font="12").place(x=120,y=160,width=40,height=40)
        self.buttonpor = Button(self.raiz, text='*', command = lambda : self.say("porr", "*"), font="12").place(x=170,y=160,width=40,height=40)
        self.buttonigual = Button(self.raiz, text='=', command = lambda : self.say("igual", "="), font="12").place(x=20,y=210,width=40,height=40)
        self.buttonborrar = Button(self.raiz, text='Borrar', command = lambda : self.say("Borrar", "b"), font="12").place(x=70,y=210,width=90,height=40)
        self.buttonborrar = Button(self.raiz, text='/', command = lambda : self.say("entre", "/"), font="12").place(x=170,y=210,width=40,height=40)

    def say(self, number, tipo=None):
        """Al precionar el boton dice la opcion"""
        self.habla(number)
        if (tipo =="+"): number = "+"
        elif (tipo =="-"): number = "-" 
        elif (tipo =="*"): number = "*"
        elif (tipo =="/"): number = "/"
        elif (tipo =="b"): 
            self.borrar() 
            number=""
        elif (tipo =="="): 
            self.resultado() 
            number=""
        self.text1.insert(END, number)

    def borrar(self): self.text1.delete("1.0", END)

    def resultado(self):
        """ Muestra el resultado en la pantalla """
        a = self.text1.get("1.0", END)
        if len(a) != 1:
            if "+" in a: self.valor("+", "mas", a)
            elif "-" in a: self.valor("-", "menos", a)
            elif "*" in a: self.valor("*", "porr", a)
            elif "/" in a: self.valor("/", "entre", a)
        else: self.habla("Falta de Datos")

    def valor(self, signo, letra, a):
        """Se encarga de Ver los datos que estar dentro del textbox y ver que esten correcto y manda el resultado"""
        try:
            resul = a.split("\n")[0].split(signo)
            if signo == "+": se = float(resul[0]) + float(resul[1])
            if signo == "-": se = float(resul[0]) - float(resul[1])
            if signo == "*": se = float(resul[0]) * float(resul[1])
            if signo == "/": se = float(resul[0]) / float(resul[1])
            self.habla("El Resultado {} {} {} es:{}".format(resul[0], letra, resul[1], se))
            self.borrar()
            self.text1.insert(END, se)
        except ValueError as e:
            self.habla("Datos Incorrecto o Si Es Otra operacion intente despues")
            self.borrar()

    def habla(self, string):
        self.hablar.say(string)
        self.hablar.runAndWait()

if __name__ == '__main__':
    Calculator()