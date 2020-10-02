from tkinter import ttk
from tkinter import *
import sqlite3


class Eficiencia:
    db_name = "Eficiencia.db"

    def __init__(self, window):
        self.wind = window
        self.wind.title("Eficiencia Automatizada")
        frame = Frame(self.wind)
        frame.place(x=0, y=0)
        frame.config(width=1920, height=1080, bg="blanchedalmond")

        def resultados2():
            self.Rate2.set(round((float(self.TE2.get()) + float(self.CE2.get())) / float(
                ((float(self.opn.get()) / 2) + float(self.opf.get())))))
            self.Meta2.set(round((3600 * float(self.HR2.get())) / float(self.Rate2.get())))
            self.UPHT2.set(round(float(self.UPH2.get()) + float(self.UPHOOB2.get())))
            self.PR2.set((round(100 * (float(self.UPHT2.get()) / float(self.Meta2.get())))))
            self.PJ2.set((round(
                (100 * (((float(self.TJ2.get()) * 60) / float(self.Rate2.get())) + float(self.UPHT2.get())) / float(
                    self.Meta2.get())))))
            self.MP2.set(
                round((60 * float(self.HR2.get())) - ((float(self.PR2.get()) / 100) * (60 * float(self.HR2.get())))))
            self.UP2.set(round(float(self.Meta2.get()) - float(self.UPHT2.get())))
            self.OP2.set(round(((float(self.opn.get()))/2)+float(self.opf.get())))

        def borrar2():
            self.TE2.set("")
            self.CE2.set("")
            self.HR2.set("")
            self.OP2.set("")
            self.UPH2.set("")
            self.UPHOOB2.set("")
            self.TJ2.set("")
            self.Rate2.set("")
            self.Meta2.set("")
            self.UPHT2.set("")
            self.PR2.set("")
            self.PJ2.set("")
            self.MP2.set("")
            self.UP2.set("")

        self.TE2 = StringVar()
        self.CE2 = StringVar()
        self.HR2 = StringVar()
        self.OP2 = StringVar()
        self.UPH2 = StringVar()
        self.UPHOOB2 = StringVar()
        self.TJ2 = StringVar()

        self.Rate2 = StringVar()
        self.Meta2 = StringVar()
        self.UPHT2 = StringVar()
        self.PR2 = StringVar()
        self.PJ2 = StringVar()
        self.MP2 = StringVar()
        self.UP2 = StringVar()

        self.Hr = StringVar()
        self.opn = StringVar()
        self.opf = StringVar()
        self.userentry = StringVar()

        self.TituloPKG = Label(self.wind, text="Eficiencia Empaque")
        self.TituloPKG.place(x=15, y=15)
        self.TituloPKG.config(bg="blanchedalmond", fg="navy", font=24)

        self.TE2label = Label(self.wind, text="Tiempo Estandar")
        self.TE2label.place(x=15, y=55)
        self.TE2label.config(bg="blanchedalmond", fg="black")
        self.TIEMPOSTENTRY = Entry(self.wind, justify="center", textvariable=self.TE2, width="5")
        self.TIEMPOSTENTRY.place(x=175, y=55)
        self.TIEMPOSTENTRY.focus()

        self.CE2label = Label(self.wind, text="Componente Extra")
        self.CE2label.place(x=215, y=55)
        self.CE2label.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.CE2, width="5").place(x=365, y=55)

        self.opnuevos = Label(self.wind, text="OP.Nuevos")
        self.opnuevos.place(x=405, y=55)
        self.opnuevos.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.opn, width="5").place(x=515, y=55)

        self.opfijos = Label(self.wind, text="OP.Fijos")
        self.opfijos.place(x=555, y=55)
        self.opfijos.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.opf, width="5").place(x=655, y=55)

        self.UPH2label = Label(self.wind, text="Unidades Producidas Stage")
        self.UPH2label.place(x=15, y=95)
        self.UPH2label.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.UPH2, width="5").place(x=175, y=95)

        self.UPHOOB2label = Label(self.wind, text="Unidades Producidas OOB")
        self.UPHOOB2label.place(x=215, y=95)
        self.UPHOOB2label.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.UPHOOB2, width="5").place(x=365, y=95)

        self.TJ2label = Label(self.wind, text="Tiempo Justificado")
        self.TJ2label.place(x=405, y=95)
        self.TJ2label.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.TJ2, width="5").place(x=515, y=95)

        self.Hora2label = Label(self.wind, text="Hora o 1/2 Hora")
        self.Hora2label.place(x=555, y=95)
        self.Hora2label.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.HR2, width="5").place(x=655, y=95)

        self.Rate2label = Label(self.wind, text="Rate")
        self.Rate2label.place(x=15, y=145)
        self.Rate2label.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.Rate2, state="disabled", width="5").place(x=55, y=145)

        self.Meta2label = Label(self.wind, text="Meta")
        self.Meta2label.place(x=125, y=145)
        self.Meta2label.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.Meta2, state="disabled", width="5").place(x=175, y=145)

        self.UPHT2label = Label(self.wind, text="Unidades producidas")
        self.UPHT2label.place(x=215, y=145)
        self.UPHT2label.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.UPHT2, state="disabled", width="5").place(x=365, y=145)

        self.PR2label = Label(self.wind, text="Porcentaje de unidades producidas")
        self.PR2label.place(x=405, y=145)
        self.PR2label.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.PR2, state="disabled", width="5").place(x=655, y=145)

        self.PJ2label = Label(self.wind, text="Porcentaje de Unidades Justificadas")
        self.PJ2label.place(x=165, y=185)
        self.PJ2label.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.PJ2, state="disabled", width="5").place(x=365, y=185)

        self.MP2label = Label(self.wind, text="Minutos Perdidos")
        self.MP2label.place(x=405, y=185)
        self.MP2label.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.MP2, state="disabled", width="5").place(x=515, y=185)

        self.UP2label = Label(self.wind, text="Unidades Perdidas")
        self.UP2label.place(x=555, y=185)
        self.UP2label.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.UP2, state="disabled", width="5").place(x=655, y=185)

        self.resultadosboton2 = Button(self.wind, text="RESULTADOS", command=resultados2)
        self.resultadosboton2.place(x=15, y=395)
        self.resultadosboton2.config(bg="chocolate", fg="black", height=1, width=10)

        self.reiniciarboton2 = Button(self.wind, text="REINICIAR", command=borrar2)
        self.reiniciarboton2.place(x=105, y=395)
        self.reiniciarboton2.config(bg="chocolate", fg="black", height=1, width=10)

        self.Hora = Label(self.wind, text="Hora")
        self.Hora.place(x=15, y=185)
        self.Hora.config(bg="blanchedalmond", fg="black")
        Entry(self.wind, justify="center", textvariable=self.Hr, width="5").place(x=55, y=185)

        self.userentry.set("BRANDON")
        self.user = Label(self.wind, text="Usuario")
        self.user.place(x=15, y=325)
        self.user.config(bg="blanchedalmond", fg="black")
        self.userentry = Entry(self.wind, justify=CENTER, width="13", textvariable=self.userentry)
        self.userentry.place(x=75, y=325)

        login = Button(text='INICIAR SESION', command=self.get_products)
        login.place(x=15, y=355)
        login.config(bg="chocolate", fg="black", height=1, width=15)

        guardar = Button(self.wind, text='GUARDAR HORA', command=self.add_product)
        guardar.place(x=215, y=395)
        guardar.config(bg="chocolate", fg="black", height=1, width=14)

        # Output Messages
        self.message = Label(text='', fg='red', bg="blanchedalmond")
        self.message.place(x=355, y=395)

        # Table
        self.tree = ttk.Treeview(height=12, columns=1)
        self.tree["columns"] = ("1", '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14')
        self.tree.place(x=15, y=425)
        self.tree.heading('#0', text='Hora', anchor=CENTER)
        self.tree.column('#0', anchor=CENTER, width=40)
        self.tree.heading("#1", text="Tiemp.Est.", anchor=CENTER)
        self.tree.column('#1', anchor=CENTER, width=60)
        self.tree.heading("#2", text="Comp.Ext.", anchor=CENTER)
        self.tree.column('#2', anchor=CENTER, width=60)
        self.tree.heading("#3", text="Op.Nuevo", anchor=CENTER)
        self.tree.column('#3', anchor=CENTER, width=65)
        self.tree.heading("#4", text="Op.Fijos", anchor=CENTER)
        self.tree.column('#4', anchor=CENTER, width=50)
        self.tree.heading("#5", text="Op. Cont", anchor=CENTER)
        self.tree.column('#5', anchor=CENTER, width=60)
        self.tree.heading("#6", text="Rate", anchor=CENTER)
        self.tree.column('#6', anchor=CENTER, width=40)
        self.tree.heading("#7", text="Meta", anchor=CENTER)
        self.tree.column('#7', anchor=CENTER, width=40)
        self.tree.heading("#8", text="UPH Stage", anchor=CENTER)
        self.tree.column('#8', anchor=CENTER, width=70)
        self.tree.heading("#9", text="UPH OOB", anchor=CENTER)
        self.tree.column('#9', anchor=CENTER, width=60)
        self.tree.heading("#10", text="UPH Total", anchor=CENTER)
        self.tree.column('#10', anchor=CENTER, width=60)
        self.tree.heading("#11", text="% Real", anchor=CENTER)
        self.tree.column('#11', anchor=CENTER, width=50)
        self.tree.heading("#12", text="% TM", anchor=CENTER)
        self.tree.column('#12', anchor=CENTER, width=40)
        self.tree.heading("#13", text="T.M.", anchor=CENTER)
        self.tree.column('#13', anchor=CENTER, width=40)
        self.tree.heading("#14", text="U.P.", anchor=CENTER)
        self.tree.column('#14', anchor=CENTER, width=40)

        # Buttons
        borrar = Button(text='BORRAR', command=self.delete_product)
        borrar.place(x=630, y=395)
        borrar.config(bg="chocolate", fg="black", height=1, width=10)
        editar = Button(text='EDITAR', command=self.edit_product)
        editar.place(x=720, y=395)
        editar.config(bg="chocolate", fg="black", height=1, width=9)

        # Filling the Rows
        self.get_products()

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # def validar_User(self):

    def get_products(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = "SELECT * FROM " + self.userentry.get() + " ORDER BY Hora DESC"
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=(row[2], row[3], row[4], row[5], row[6], row[7]
                                                         , row[8], row[9], row[10], row[11], row[12]
                                                         , row[13], row[14], row[15]))

    # User Input Validation
    def validation(self):
        return len(self.TE2.get()) != 0 and len(self.CE2.get()) != 0 and len(self.HR2.get()) != 0

    def add_product(self):
        if self.validation():
            query = "INSERT INTO " + self.userentry.get() + " VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            parameters = (self.Hr.get(), self.TE2.get(), self.CE2.get(), self.opn.get(),
                          self.opf.get(), self.OP2.get(), self.Rate2.get(), self.Meta2.get(), self.UPH2.get(),
                          self.UPHOOB2.get(), self.UPHT2.get(), self.PR2.get(), self.PJ2.get(), self.MP2.get(),
                          self.UP2.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Product {} added Successfully'.format(self.Hr.get())

        else:
            self.message['text'] = 'Llene Todos Los Campos'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM Eficiencia WHERE Hora = ?'
        self.run_query(query, (name,))
        self.message['text'] = 'Record {} deleted Successfully'.format(name)
        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Please, select Record'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Product'
        # Old Name
        Label(self.edit_wind, text='Old Name:').place(x=300, y=400)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=name), state='readonly').place(x=350, y=450)

        # New Name
        Label(self.edit_wind, text='New Price:').grid(row=1, column=1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row=1, column=2)

        # Old Price
        Label(self.edit_wind, text='Old Price:').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_price), state='readonly').grid(row=2,
                                                                                                              column=2)
        # New Price
        Label(self.edit_wind, text='New Name:').grid(row=3, column=1)
        new_price = Entry(self.edit_wind)
        new_price.grid(row=3, column=2)

        Button(self.edit_wind, text='Update',
               command=lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row=4,
                                                                                                         column=2,
                                                                                                         sticky=W)
        self.edit_wind.mainloop()

    def edit_records(self, new_name, name, new_price, old_price):
        query = 'UPDATE product SET Hora = ?, Mecanico/Familia = ? WHERE Hora = ? AND Mecanico/Familia = ?'
        parameters = (new_name, new_price, name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} updated successfylly'.format(name)
        self.get_products()


if __name__ == "__main__":
    window = Tk()
    window.geometry("820x900+0+0")
    aplicacion = Eficiencia(window)
    window.mainloop()
