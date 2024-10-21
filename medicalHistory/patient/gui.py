import tkinter as tk
from tkinter import ttk,scrolledtext, Toplevel
from model.patient import *

pink = '#f9e7ed'

config = {
    'font': ('Roboto', 15, 'bold'),
    'bg': pink 
}

class Frame(tk.Frame):

    def __init__(self, root):

        super().__init__(root,width= 1280, height=720)
        self.root = root
        self.pack()
        self.config(bg=pink)
        self.old_id = None
        self.inputs_patient()
        self.patients_table()

    def inputs_patient(self):

        #LABELS
        self.label_id_card = tk.Label(self,text='C.C: ')
        self.label_id_card.config(config)
        self.label_id_card.grid(column = 0, row = 1, padx= 10, pady = 5 ,sticky = 'e')
        
        self.label_name = tk.Label(self,text='Nombre: ')
        self.label_name.config(config)
        self.label_name.grid(column = 0, row = 2, padx= 10, pady = 5 ,sticky = 'e')


        self.label_birth = tk.Label(self,text='Fecha de Nacimiento: ')
        self.label_birth.config(config)
        self.label_birth.grid(column = 0, row = 3, padx= 10, pady = 5 ,sticky = 'e')

        self.label_phone = tk.Label(self,text='Telefono: ')
        self.label_phone.config(config)
        self.label_phone.grid(column = 0, row = 4, padx= 10, pady = 5 ,sticky = 'e')

        self.label_job = tk.Label(self,text='Ocupacion: ')
        self.label_job.config(config)
        self.label_job.grid(column = 0, row = 5, padx= 10, pady = 5 ,sticky = 'e')

        self.label_gender = tk.Label(self,text='Genero: ')
        self.label_gender.config(config)
        self.label_gender.grid(column = 0, row = 6, padx= 10, pady = 5 ,sticky = 'e')

        self.label_background = tk.Label(self,text='Antecedentes: ')
        self.label_background.config(config)
        self.label_background.grid(column = 0, row = 7, padx= 10, pady = 5 ,sticky = 'e')

        #INPUTS

        self.input_id_card = tk.Entry(self, textvariable = tk.StringVar())
        self.input_id_card.config(width = 30 , font = ('Roboto',15))
        self.input_id_card.grid(column = 1 , row = 1 ,padx = 10 , pady = 5,columnspan = 2)

        self.input_name = tk.Entry(self, textvariable = tk.StringVar())
        self.input_name.config(width = 30 , font = ('Roboto',15))
        self.input_name.grid(column = 1 , row = 2 ,padx = 10 , pady = 5 ,columnspan = 2)

        self.input_birth = tk.Entry(self, textvariable = tk.StringVar())
        self.input_birth.config(width = 30 , font = ('Roboto',15))
        self.input_birth.grid(column = 1 , row = 3 ,padx = 10 , pady = 5,columnspan = 2)

        self.input_phone = tk.Entry(self, textvariable = tk.StringVar())
        self.input_phone.config(width = 30 , font = ('Roboto',15))
        self.input_phone.grid(column = 1 , row = 4 ,padx = 10 , pady = 5,columnspan = 2)

        self.input_job = tk.Entry(self, textvariable = tk.StringVar())
        self.input_job.config(width = 30 , font = ('Roboto',15))
        self.input_job.grid(column = 1 , row = 5 ,padx = 10 , pady = 5,columnspan = 2)

        self.input_gender = tk.Entry(self, textvariable = tk.StringVar())
        self.input_gender.config(width = 30 , font = ('Roboto',15))
        self.input_gender.grid(column = 1 , row = 6 ,padx = 10 , pady = 5,columnspan = 2)

        self.input_background = tk.Entry(self, textvariable = tk.StringVar())
        self.input_background.config(width = 30 , font = ('Roboto',15))
        self.input_background.grid(column = 1 , row = 7 ,padx = 10 , pady = 5,columnspan = 2)

        #BUTTONS

        self.add = tk.Button(self,text='NUEVO PACIENTE',command = self.patient_save)
        self.add.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff' , bg ='#158645',
                        cursor='hand2', activebackground='#358d6f')
        self.add.grid(column = 0,row = 8, padx=10,pady=5)

        self.save = tk.Button(self,text='GUARDAR CAMBIOS', command = self.patient_save)
        self.save.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff' , bg ='#0737ba',
                        cursor='hand2', activebackground='#4574f7')
        self.save.grid(column =1 ,row = 8, padx=10,pady=5)

        self.cancel = tk.Button(self,text='CANCELAR')
        self.cancel.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff' , bg ='#b0020d',
                        cursor='hand2', activebackground='#c43740')
        self.cancel.grid(column = 2 ,row = 8, padx=10,pady=5)

    def patient_save(self):
        patient = Patient(
            self.input_birth.get(),
            self.input_phone.get(),
            self.input_name.get(),
            self.input_job.get(),
            self.input_gender.get(),
            self.input_id_card.get(),
            self.input_background.get()
        )
        if self.old_id == None:
            save_patient(patient)
        else:
            uptade_patient(patient,self.old_id)

        self.inputs_patient()
        self.patients_table()

    def patients_table(self,where = ''):

        if where != '':
            self.show_patient = search_condition(where)
        else:
            self.show_patient = show_patients()

        self.table = ttk.Treeview(self,column = ('Cedula','Nombre','Ocupacion','Telefono',
                                  'Genero', 'Antecedentes', 'Edad','Fecha de Nacimiento'
                                  ))
        self.table.grid(column = 0 ,row = 10, columnspan = 7,sticky = 'nse')
        
        self.scroll = ttk.Scrollbar(self, orient = 'vertical',command = self.table.yview)
        self.scroll.grid(row = 10 , column = 8 ,sticky = 'nse')

        self.table.configure(yscrollcommand = self.scroll.set)

        self.table.tag_configure('evenrow',background = '#c5eafe')

        self.table.heading('#0' ,text='C.C')
        self.table.heading('#1' ,text='Nombre')
        self.table.heading('#2' ,text='Ocupacion')
        self.table.heading('#3' ,text='Telefono')
        self.table.heading('#4' ,text='Genero')
        self.table.heading('#5' ,text='Antecedentes')
        self.table.heading('#6' ,text='Edad')
        self.table.heading('#7' ,text='Fecha de Nacimiento')

        self.table.column('#0', anchor=tk.CENTER, width=150, stretch=False)
        self.table.column('#1', anchor=tk.CENTER, width=200, stretch=False)
        self.table.column('#2', anchor=tk.CENTER, width=150, stretch=False)
        self.table.column('#3', anchor=tk.CENTER, width=150, stretch=False)
        self.table.column('#4', anchor=tk.CENTER, width=80, stretch=False)
        self.table.column('#5', anchor=tk.CENTER, width=550, stretch=False)
        self.table.column('#6', anchor=tk.CENTER, width=80, stretch=False)
        self.table.column('#7', anchor=tk.CENTER, width=200, stretch=False)

        for data in self.show_patient:
            self.table.insert('',0,text=data[0], 
                              values=(
                                    data[1],data[2],data[3],
                                    data[4],data[5],data[6],data[7]
                                    ),
                              tags=('evenrow',)
                             )
        self.edit_patient = tk.Button(self,text='EDITAR PACIENTE' ,command = self.edit)
        self.edit_patient.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff', 
                                 bg ='#1e0075',
                                 cursor='hand2', activebackground='#9379e0'
                                 )
        self.edit_patient.grid(row = 11,column = 0,padx = 10, pady = 5)
 
        self.history_patient = tk.Button(self,text='VER HISTORIAL PACIENTE')
        self.history_patient.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff', 
                                 bg ='#007c79',
                                 cursor='hand2', activebackground='#a7ebeb'
                                 )
        self.history_patient.grid(row = 11,column = 1,padx = 10, pady = 5)

    def edit(self):
        try:
            self.id_card = self.table.item(self.table.selection())['text']
            self.name = self.table.item(self.table.selection())['values'][0]
            self.job = self.table.item(self.table.selection())['values'][1]
            self.phone = self.table.item(self.table.selection())['values'][2]
            self.gender = self.table.item(self.table.selection())['values'][3]
            self.background = self.table.item(self.table.selection())['values'][4]
            self.birth = self.table.item(self.table.selection())['values'][6]
            
            self.old_id = self.id_card

            self.input_id_card.insert(0,self.id_card)
            self.input_name.insert(0,self.name)
            self.input_job.insert(0,self.job)
            self.input_phone.insert(0,self.phone)
            self.input_gender.insert(0,self.gender)
            self.input_background.insert(0,self.background)
            self.input_birth.insert(0,self.birth)

        except :
            title = 'EDITAR PACIENTE'
            message = 'Error al editar paciente' 
            messagebox.showerror(title,message)


