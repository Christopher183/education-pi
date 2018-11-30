from tkinter import*

raiz=Tk()

raiz.title("Juego Preguntas simples.")

raiz.resizable()

raiz.iconbitmap("alas.ico")
#ya esta hecho lo de arriba.
#raiz.geometry("720x480")

raiz.config(bg="gray")

miframe=Frame(raiz)

miframe.pack()

miframe.config(bg="white")

miframe.config(width="720",height="480")

miframe.config(bd=20)

miframe.config(relief="groove")

miframe.config(cursor="hand1")

miimagen=PhotoImage(file="")

milabel=Label(miframe, text="Hola",fg="blue")

milabel.place(x=100, y=200)



raiz.mainloop()


