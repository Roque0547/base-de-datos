import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk

#CREAR VENTANA
ventana = tkinter.Tk()
ventana.title("DATOS")
ventana.geometry("300x250+500+280")
ventana.configure(bg= "SpringGreen2")
ventana.resizable(0,0)
tabla_botones = []

#CAJAS DE TEXTOS
Label(ventana, text = "Nombre:").pack()
caja1 = Entry(ventana)
caja1.pack()

Label(ventana, text = "Apellido:").pack()
caja2 = Entry(ventana)
caja2.pack()

Label(ventana, text = "DNI:").pack()
caja3 = Entry(ventana)
caja3.pack()

Label(ventana, text = "Color Favorito:").pack()
caja4 = Entry(ventana)
caja4.pack()

#CREAR BOTON
boton = tk.Button(text="Guardar", relief="ridge", borderwidth=5)
boton.place(x=110, y=200)

sql = "INSERT INTO Datos (Nombre,Apellido, DNI, ColorFavorito) VALUES (%s, %s)"
val = ("Roque","Portillo","123456","Verde")
bd.execute(sql, val)
db.commit()
           
def DATOS():
 # CONECTAR A LA BASE DE DATOS
 db = sqlite3.connect('datos1.db')
 c = db.cursor()
ventana.mainloop()