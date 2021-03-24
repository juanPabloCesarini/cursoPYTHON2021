from tkinter import *

root = Tk()
root.title("Matelab - mateGestion 1.0")
root.resizable(0,0)
root.iconbitmap("ISO_MATELAB.ico")

miFrame = Frame(root)
miFrame.config(bg="green")
miFrame.pack(fill="x", expand=1)
miFrame.config(width=800, height=600)
label=Label(miFrame, text="Nombre: ")
label.grid(row=0,column=0, padx=5,pady=5)

entrada = Entry(miFrame)
entrada.grid(row=0,column=1,padx=5,pady=5)
entrada.config(justify="center")

label2=Label(miFrame, text="Apellido: ")
label2.grid(row=1,column=0, padx=5,pady=5)

entrada2 = Entry(miFrame)
entrada2.grid(row=1,column=1,padx=5,pady=5)
entrada2.config(state="disable")

label3=Label(miFrame, text="Contraseña: ")
label3.grid(row=2,column=0, padx=5,pady=5)

entrada3 = Entry(miFrame)
entrada3.grid(row=2,column=1,padx=5,pady=5)
entrada3.config(show="*")

root.mainloop()