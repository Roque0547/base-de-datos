import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk

ventana = tkinter.Tk()
ventana.title("DATOS")
ventana.geometry("300x250+500+280")
ventana.configure(bg= "SpringGreen2")
ventana.resizable(0,0)
tabla_botones = []

Label(ventana, text = "D.N.I.:").pack()
caja1 = Entry(ventana)
caja1.pack()

Label(ventana, text = "Nombre:").pack()
caja2 = Entry(ventana)
caja2.pack()

Label(ventana, text = "Apellido:").pack()
caja3 = Entry(ventana)
caja3.pack()

Label(ventana, text = "Color Favorito:").pack()
caja4 = Entry(ventana)
caja4.pack()


boton = ttk.Button(text="Guardar")
boton.place(x=110, y=200)


def DATOS():
 # Connect to database
 db = sqlite3.connect('/home/diego123/Escritorio/login.db')
 c = db.cursor()
ventana.mainloop()