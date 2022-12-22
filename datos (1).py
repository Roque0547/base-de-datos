import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3

def escribir():
    nombre = caja1.get()
    apellido = caja2.get()
    dni = caja3.get()
    colorfavorito = caja4.get()
    print(nombre, apellido, dni, colorfavorito)

#def leer():

    
#CREAR VENTANA
ventana = tkinter.Tk()
ventana.title("DATOS")
ventana.geometry("400x300+500+280")
ventana.configure(bg= "SpringGreen2")
ventana.resizable(0,0)
tabla_botones = []

#CAJAS DE TEXTOS
Label(ventana, text = "Nombre:", bg= "SpringGreen2").pack()
caja1 = Entry(ventana)
caja1.pack()

Label(ventana, text = "Apellido:", bg= "SpringGreen2").pack()
caja2 = Entry(ventana)
caja2.pack()

Label(ventana, text = "DNI:", bg= "SpringGreen2").pack()
caja3 = Entry(ventana)
caja3.pack()

Label(ventana, text = "Color Favorito:", bg= "SpringGreen2").pack()
caja4 = Entry(ventana)
caja4.pack()

   
#DESPLEGABLE
lista=["Python", "C", "C++", "Java"]
combo = ttk.Combobox(values=lista)
combo.place(x=115, y=185)


#CREAR BOTON
boton = tk.Button(text="Guardar", relief="ridge", borderwidth=5, command = escribir)
boton.place(x=110, y=220)

boton = tk.Button(text="Buscar", relief="ridge", borderwidth=5,)
boton.place(x=210, y=220)

 
ventana.mainloop()
