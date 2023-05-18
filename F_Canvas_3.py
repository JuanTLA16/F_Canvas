


#import la libreria tkinter, con el alias tk
import tkinter as tk
from tkinter import Frame, BOTH, Canvas, PhotoImage, Scale
# -------------------------------
# VENTANA PRINCIPAL
# -------------------------------



def modificar_arco(angulo):
    c.itemconfig(Arco1,start=angulo)  
    c.itemconfig(Arco2,start=int(angulo)+90) 
    c.itemconfig(Arco3,start=int(angulo)+180)
    c.itemconfig(Arco4,start=int(angulo)+270)


ventana_principal = tk.Tk()
ventana_principal.title("MOLINO")
ventana_principal.geometry("400x475")
ventana_principal.resizable(False, False)

BASE = 350
ALTURA = 350
RADIO = 100


#----------------------
# FRAME DE GRAFICACIÓN
#----------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg ="black", width=380, height=380)
frame_graficacion.place(x=10, y=10)

# creacion de canvas
c = Canvas(frame_graficacion, width=360, height=360)
c.place(x=10 , y=10)

triangulo = c.create_polygon(BASE*2/5,ALTURA, BASE/2, ALTURA/2, BASE*3/5, ALTURA, fill="green")

# Arco
Arco1 = c.create_arc(BASE/2-RADIO, ALTURA/2-RADIO, BASE/2+RADIO, ALTURA/2+RADIO, start=45, extent=45, fill="blue")
Arco2 = c.create_arc(BASE/2-RADIO, ALTURA/2-RADIO, BASE/2+RADIO, ALTURA/2+RADIO, start=135, extent=45, fill="yellow")
Arco3 = c.create_arc(BASE/2-RADIO, ALTURA/2-RADIO, BASE/2+RADIO, ALTURA/2+RADIO, start=225, extent=45, fill="orange")
Arco4 = c.create_arc(BASE/2-RADIO, ALTURA/2-RADIO, BASE/2+RADIO, ALTURA/2+RADIO, start=315, extent=45, fill="green")

frame_2=Frame(ventana_principal)
frame_2.config(bg="black",width=380,height=90)
frame_2.place(x=10,y=380)
barra_deslizamiento = Scale(frame_2, label='ÁNGULO', from_=0, to=360, orient="horizontal", length=355, command=modificar_arco, tickinterval=90)
barra_deslizamiento.place(x=10,y=10)

# desplegar ventana principal y queda a la espera de lo que el usuario haga 
ventana_principal.mainloop()