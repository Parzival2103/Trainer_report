from tkinter import *
import subprocess
import time

# Raiz del programa
root = Tk()
root.config()
root.title('Indice de aplicaciones')
frame = Frame(root)
frame.pack()
frame.config(width=350, height=90, bg="blanchedalmond")


def indice():
    subprocess.Popen("IndicedeOperaciones.py", shell=True)
    root.state(newstate="withdraw")
    time.sleep(5)
    root.state(newstate="normal")


def ef():
    subprocess.Popen('EficienciaPKG.py', shell=True)
    root.state(newstate="withdraw")
    time.sleep(5)
    root.state(newstate="normal")


Eboton = Button(root, text='EFICIENCIA')
Eboton.config(bg="limegreen", fg="black", height=2, width=14, font=1, command=ef)
Eboton.place(x=20, y=20)

Iboton = Button(root, text='INDICE')
Iboton.config(bg="limegreen", fg="black", height=2, width=14, font=1, command=indice)
Iboton.place(x=190, y=20)
root.mainloop()
