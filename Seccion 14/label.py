from tkinter import *

root = Tk()
root.title("Matelab - mateGestion 1.0")
root.resizable(0,0)
root.iconbitmap("ISO_MATELAB.ico")
root.config(width=800, height=600)

texto_nuevo = StringVar()
texto_nuevo.set("Name: ")
imagen = PhotoImage(file="MVC.png")
label = Label(root, image=imagen)
label.pack()

label = Label(root, text="Nombre: ")
label.place(x=100, y=50)
label.config(bg="lightblue", font=("consola",20), textvariable=texto_nuevo)

label = Label(root, text="Apellido: ")
label.place(x=100,y=120)
label.config(bg="black", fg="white", font=("times",20))


root.mainloop()