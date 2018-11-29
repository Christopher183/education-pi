#Primera version del programa salud plus
from tkinter import *

#--------------------Definir eventos------------------------
def funcion():
    aseo_ventana = Toplevel(raiz)
    raiz.iconify()


#------------------Fin definir eventos----------------------



raiz=Tk()


#----------------------background---------------------------
background_image=PhotoImage(file="fondo.png")
background_label=Label(raiz, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#----------------------Fin Background-----------------------
raiz.title("SaludPlus")

raiz.iconbitmap("saludplus.ico")

#.geometry("650x350")
fondo=PhotoImage(file="fondo.png")

raiz.config(bg="black", width=720, height=480)

texto=Label(raiz, text="Bienvenido a SaludPlus, aquí le enseñaremos cosas esenciales para su cuidado personal",font=(72))
texto.pack()

aseo=PhotoImage(file="aseo.png")
#aseo es el frame donde se daran temas de higiene personal
aseo=Frame()
aseo_image=PhotoImage(file="aseo.png")
btnaseo=Button(raiz, image=aseo_image, height=234, width=216, cursor="hand2").place(x=100, y=100)

#FIN ASEO

#Primeros Auxilios
texto_primerosauxilios=Label(raiz, text="Clic en una de las imagenes para ver las recomendaciones",font=(72), row=)
texto_primerosauxilios.pack()
primeros_auxilios=Frame()
primeros_auxilios_img=PhotoImage(file="primeros auxilios1.png")
btnpauxilios=Button(raiz, image=primeros_auxilios_img, height=234, width=216, cursor="hand2").place(x=400, y=100)

primeros_auxilios.config(cursor="hand2")
#Fin Primeros auxilios

#Enfermedades basicas
enfermedades_basicas=Frame()
enfermedades_basicas_img=PhotoImage(file="enfermedades basicas1.png")
btnebasicas=Button(raiz, image=enfermedades_basicas_img, height=234, width=216, cursor="hand2").place(x=700, y=100)
enfermedades_basicas.config(cursor="hand2")
#aseoboton=frame()
#aseoboton.config(image=aseo_image)
#aseoboton.pack()

#Funcion salir
#fin funcion Salir

#-------------Inicio ventanas nuevas------------------------




#------------------Fin ventanas nuevas----------------------

raiz.mainloop()
