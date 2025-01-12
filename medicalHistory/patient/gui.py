import tkinter as tk
from tkinter import ttk,scrolledtext, Toplevel
from model.patient import *
from model.history import *
import tkcalendar as tc
from tkcalendar import *
from datetime import datetime

pink = '#f9e7ed'

config = {
    'font': ('Roboto', 15, 'bold'),
    'bg': pink 
}

class Frame(tk.Frame):

    def __init__(self, root):

        super().__init__(root)
        self.root = root
        self.pack()
        self.config(bg=pink)
        self.root.config(bg=pink)
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

        #FILTERS

        self.label_filter_id = tk.Label(self,text='Buscar C.C: ')
        self.label_filter_id.config(config)
        self.label_filter_id.grid(column = 3, row = 1, padx= 10, pady = 5 ,sticky = 'e')
        
        self.label_filter_name = tk.Label(self,text='Buscar Nombre: ')
        self.label_filter_name.config(config)
        self.label_filter_name.grid(column = 3, row = 2, padx= 10, pady = 5 ,sticky = 'e')
        
        #INPUTS

        self.input_filter_id = tk.Entry(self, textvariable = tk.StringVar())
        self.input_filter_id.config(width = 30 , font = ('Roboto',15))
        self.input_filter_id.grid(column = 4 , row = 1 ,padx = 10 , pady = 5,columnspan = 2 )

        self.input_filter_name = tk.Entry(self, textvariable = tk.StringVar())
        self.input_filter_name.config(width = 30 , font = ('Roboto',15))
        self.input_filter_name.grid(column = 4 , row = 2 ,padx = 10 , pady = 5 ,columnspan = 2)

        self.input_id_card = tk.Entry(self, textvariable = tk.StringVar())
        self.input_id_card.config(width = 50 , font = ('Roboto',15))
        self.input_id_card.grid(column = 1 , row = 1 ,padx = 10 , pady = 5,columnspan = 2)

        self.input_name = tk.Entry(self, textvariable = tk.StringVar())
        self.input_name.config(width = 50 , font = ('Roboto',15))
        self.input_name.grid(column = 1 , row = 2 ,padx = 10 , pady = 5 ,columnspan = 2)

        self.input_birth = tk.Entry(self, textvariable = tk.StringVar())
        self.input_birth.config(width = 50 , font = ('Roboto',15))
        self.input_birth.grid(column = 1 , row = 3 ,padx = 10 , pady = 5,columnspan = 2)

        self.input_phone = tk.Entry(self, textvariable = tk.StringVar())
        self.input_phone.config(width = 50 , font = ('Roboto',15))
        self.input_phone.grid(column = 1 , row = 4 ,padx = 10 , pady = 5,columnspan = 2)

        self.input_job = tk.Entry(self, textvariable = tk.StringVar())
        self.input_job.config(width = 50 , font = ('Roboto',15))
        self.input_job.grid(column = 1 , row = 5 ,padx = 10 , pady = 5,columnspan = 2)

        self.input_gender = tk.Entry(self, textvariable = tk.StringVar())
        self.input_gender.config(width = 50 , font = ('Roboto',15))
        self.input_gender.grid(column = 1 , row = 6 ,padx = 10 , pady = 5,columnspan = 2)

        self.input_background = tk.Entry(self, textvariable = tk.StringVar())
        self.input_background.config(width = 50 , font = ('Roboto',15))
        self.input_background.grid(column = 1 , row = 7 ,padx = 10 , pady = 5,columnspan = 2)

        #BUTTONS

        self.add = tk.Button(self,text='NUEVO PACIENTE',command = self.patient_save)
        self.add.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff' , bg ='#77dd77',
                        cursor='hand2', activebackground='#358d6f')
        self.add.grid(column = 0,row = 8, padx=10,pady=5)

        self.save = tk.Button(self,text='GUARDAR CAMBIOS', command = self.patient_save)
        self.save.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff' , bg ='#84b6f4',
                        cursor='hand2', activebackground='#4574f7')
        self.save.grid(column =1 ,row = 8, padx=10,pady=5)

        self.cancel = tk.Button(self,text='CANCELAR', command=self.reset_inputs)
        self.cancel.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff' , bg ='#ff6961',
                        cursor='hand2', activebackground='#c43740')
        self.cancel.grid(column = 2 ,row = 8, padx=10,pady=5)

        self.search = tk.Button(self,text='BUSCAR PACIENTE', command = self.condition_search)
        self.search.config(width = 20 , font = ('Roboto',12,'bold'),fg = '#fff' , bg ='#a48fc6',
                        cursor='hand2', activebackground='#8672a7')
        self.search.grid(column = 4 ,row = 3, padx=10,pady=5 , sticky = 'e')
        
        self.calendar = tk.Button(self,text='CALENDARIO', command = self.calendar_view)
        self.calendar.config(width = 10, font = ('Roboto',12,'bold'),fg = '#fff' , bg ='#bc98f3',
                        cursor='hand2', activebackground='#8672a7')
        self.calendar.grid(column = 2 ,row = 3, padx=10,pady=5 , sticky = 'e')

    #FUNCTIONS FOR TOP BUTTONS
    
    def reset_inputs(self):
        self.inputs_patient()
    
    def calendar_view(self):
        view = Toplevel()
        view.title('CALENDARIO')
        view.config(bg=pink)  
        current_year = datetime.now().year
        input_date = tk.StringVar(value='1960-01-01')

        def update_calendar():
            selected_year = int(year_combobox.get())
            selected_month = month_combobox.current() + 1
            cal.selection_set(f"{selected_year}-{selected_month:02d}-01")
        
        cal = Calendar(view, selectmode='day', locale='es_US',
                    background='#fff', foreground='#bc98f3',
                    headersbackground='#f5d5e5',weekendbackground='#fce4ec',
                    weekendforeground='#bc98f3', othermonthbackground='#f5d5e5',
                    othermonthwebackground='#fce4ec',font=('Roboto', 12), 
                    selectbackground='#c6a2af',selectforeground='#000', 
                    normalbackground='#fff',normalforeground='#bc98f3', borderwidth=2,
                    textvariable=input_date, date_pattern='yyyy-mm-dd')
        cal.grid(row=1, column=0, padx=20, pady=20, columnspan=2, ipadx=30, ipady=30)
        

        years = list(range(1920, current_year+1))  
        year_combobox = ttk.Combobox(view, values=years, state="readonly", width=5, font=('Roboto', 12,'bold'))
        year_combobox.set(1960)  
        year_combobox.grid(row=0, column=1, padx=10)

        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        month_combobox = ttk.Combobox(view, values=months, state="readonly", width=10, font=('Roboto', 12,'bold'))
        month_combobox.set("Enero")
        month_combobox.grid(row=0, column=0, padx=10)

        update_button = tk.Button(view, text="Actualizar", command=update_calendar)
        update_button.config(font=('Roboto', 12, 'bold'), fg='#fff', bg='#77dd77',
                         cursor='hand2', activebackground='#358d6f')
        update_button.grid(row=0, column=2, padx=10,pady=5)

        def get_selected_date():
            input_date.set(cal.get_date())
            self.input_birth.delete(0,tk.END)
            self.input_birth.insert(0,cal.get_date())
            view.destroy()

        confirm_button = tk.Button(view, text="Confirmar Fecha", command=get_selected_date)
        confirm_button.config(font=('Roboto', 12, 'bold'), fg='#fff', bg='#84b6f4',
                         cursor='hand2', activebackground='#4574f7')
        confirm_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


    def condition_search(self):
        where = ''
        self.input_filter_id = self.input_filter_id.get() 
        self.input_filter_name = self.input_filter_name.get() 
        
        if self.input_filter_name != '':
            where = f'name LIKE "%{self.input_filter_name}%"'
        elif self.input_filter_id != '':
            where = f'id_card LIKE "%{self.input_filter_id}%"'
        elif self.input_filter_name != '' and self.input_filter_id != '':
            where = f'id_card LIKE "%{self.input_filter_id}%" and name LIKE "%{self.input_filter_name}%"'
        
        search_condition(where)
        self.inputs_patient()
        self.patients_table(where)


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

    # SHOWS A TABLE WITH PATIENTS  

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

        #BUTTONS ON THE BOTTOM

        self.edit_patient = tk.Button(self,text='EDITAR PACIENTE' ,command = self.edit)
        self.edit_patient.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff', 
                                 bg ='#6578a3',
                                 cursor='hand2', activebackground='#9379e0'
                                 )
        self.edit_patient.grid(row = 11,column = 0,padx = 10, pady = 5)
 
        self.history_patient = tk.Button(self,text='VER HISTORIAL PACIENTE',command=self.medical_history)
        self.history_patient.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff', 
                                 bg ='#007c79',
                                 cursor='hand2', activebackground='#a7ebeb'
                                 )
        self.history_patient.grid(row = 11,column = 1,padx = 10, pady = 5)
        
        self.close = tk.Button(self,text='CERRAR VENTANA', command = self.root.destroy)
        self.close.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff', 
                                 bg ='#a62520',
                                 cursor='hand2', activebackground='#ff6961'
                                 )
        self.close.grid(row = 11,column = 4,padx = 10, pady = 5)

    #FUNCTIONS FOR BOTTOM BUTTONS
    
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
            message = 'Error al editar paciente \n No hay Paciente Seleccionado' 
            messagebox.showerror(title,message)

    def medical_history(self):

        try:
              
            self.id_card= self.table.item(self.table.selection())['text']
            if not self.id_card:
                title = 'HISTORIA PACIENTE'
                message = 'Error al mostrar historial \n No hay Paciente Seleccionado' 
                messagebox.showerror(title,message)
                return
            mh_view = Toplevel()
            mh_view.title(' HISTORIAL MEDICO')
            mh_view.config(bg=pink)

            history = show_history(self.id_card)

            self.table_history = ttk.Treeview(mh_view,column = ('Fecha Visita',
                                                    'Motivo Consulta','Revision x Sistemas',
                                                    'TA', 'FC','FR','Peso','Talla','SAO2',
                                                    'Diagnostico','Tratamiento',
                                                    'Analisis Medico'
                                                    )
                                    )
            self.table_history.grid(column = 0 ,row = 0, columnspan = 9,sticky = 'nse')
            
            self.scroll_history = ttk.Scrollbar(mh_view, orient = 'vertical',command = self.table_history.yview)
            self.scroll_history.grid(row = 0 , column = 11 ,sticky = 'nse')

            self.table_history.configure(yscrollcommand = self.scroll_history.set)

            self.table_history.tag_configure('evenrow',background = '#c5eafe')

            self.table_history.heading('#0' ,text='Fecha Visita')
            self.table_history.heading('#1' ,text='Motivo Consulta')
            self.table_history.heading('#2' ,text='Revision x Sistemas')
            self.table_history.heading('#3' ,text='TA')
            self.table_history.heading('#4' ,text='FC')
            self.table_history.heading('#5' ,text='FR')
            self.table_history.heading('#6' ,text='Peso')
            self.table_history.heading('#7' ,text='Talla')
            self.table_history.heading('#8' ,text='SAO2')
            self.table_history.heading('#9' ,text='Diagnostico')
            self.table_history.heading('#10' ,text='Tratamiento')
            self.table_history.heading('#11' ,text='Analisis Medico')

            self.table_history.column('#0', anchor=tk.CENTER, width=100, stretch=False)
            self.table_history.column('#1', anchor=tk.CENTER, width=180, stretch=False)
            self.table_history.column('#2', anchor=tk.CENTER, width=150, stretch=False)
            self.table_history.column('#3', anchor=tk.CENTER, width=80, stretch=False)
            self.table_history.column('#4', anchor=tk.CENTER, width=80, stretch=False)
            self.table_history.column('#5', anchor=tk.CENTER, width=80, stretch=False)
            self.table_history.column('#6', anchor=tk.CENTER, width=80, stretch=False)
            self.table_history.column('#7', anchor=tk.CENTER, width=80, stretch=False)
            self.table_history.column('#8', anchor=tk.CENTER, width=80, stretch=False)
            self.table_history.column('#9', anchor=tk.CENTER, width=150, stretch=False)
            self.table_history.column('#10', anchor=tk.CENTER, width=150, stretch=False)
            self.table_history.column('#11', anchor=tk.CENTER, width=150, stretch=False)

            for data in history:
                self.table_history.insert('',0,text=data[2], 
                                values=(
                                        data[3],data[4],data[5],data[6],
                                        data[7],data[8],data[9],data[10],
                                        data[11],data[12],data[13]
                                        ),
                                tags=('evenrow',)
                                )


            add = tk.Button(mh_view,text='AGREGAR HISTORIA', command = self.view_add_history)
            add.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff' , bg ='#77dd77',
                            cursor='hand2', activebackground='#358d6f')
            add.grid(column = 0,row = 8, padx=10,pady=5)
         
            # edit_history= tk.Button(mh_view,text='EDITAR HISTORIA' )
            # edit_history.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff', 
            #                         bg ='#6578a3',
            #                         cursor='hand2', activebackground='#9379e0'
            #                         )
            # edit_history.grid(row =8 ,column = 1,padx = 10, pady = 5)
        
            close = tk.Button(mh_view,text='SALIR', command = mh_view.destroy)
            close.config(width = 20, font = ('Roboto',12,'bold'),fg = '#fff', 
                                    bg ='#a62520',
                                    cursor='hand2', activebackground='#ff6961'
                                    )
            close.grid(row = 8,column = 4,padx = 10, pady = 5)
        except:
            title = 'HISTORIA PACIENTE'
            message = 'Error al mostrar historial \n No hay Paciente Seleccionado' 
            messagebox.showerror(title,message)


    def view_add_history(self):

        view = Toplevel()
        view.title('AGREGAR HISTORIA')
        view.config(bg = pink)
        
        labels = [
        "Motivo Consulta", "Revisión x Sistemas", "TA", "FC", "FR", 
        "Peso", "Talla", "SAO2", "Diagnóstico", "Tratamiento", "Análisis Médico"
    ]
        date = datetime.now().strftime('%Y-%m-%d')
        entries = []

        for i, label_text in enumerate(labels):
            label = tk.Label(view, text=label_text, font=('Roboto', 12, 'bold'), bg=pink)
            label.grid(row=i, column=0, padx=10, pady=5, sticky='e')
            
            entry = tk.Entry(view, font=('Roboto', 12))
            entry.grid(row=i, column=1, padx=10, pady=5, sticky='w', columnspan = 3)
            entries.append(entry)

        save_button = tk.Button(view, text='GUARDAR', command=lambda: self.save_history(entries,date,self.id_card))
        save_button.config(width=15, font=('Roboto', 12, 'bold'), fg='#fff', bg='#77dd77',
                        cursor='hand2', activebackground='#358d6f')
        save_button.grid(row=len(labels), column=0, padx=10, pady=10, sticky='e')

        cie = tk.Button(view, text='CIE10', command = self.show_cie)
        cie.config(width=15, font=('Roboto', 12, 'bold'), fg='#fff', bg='#4c73ce',
                        cursor='hand2', activebackground='#358d6f')
        cie.grid(row=len(labels), column=1, padx=10, pady=10, sticky='e')
        
        medicines = tk.Button(view, text='MEDICAMENTOS', command = self.show_medicines)
        medicines.config(width=15, font=('Roboto', 12, 'bold'), fg='#fff', bg='#4c73ce',
                        cursor='hand2', activebackground='#358d6f')
        medicines.grid(row=len(labels), column=2, padx=10, pady=10, sticky='e')
        
        cancel_button = tk.Button(view, text='SALIR', command=view.destroy)
        cancel_button.config(width=15, font=('Roboto', 12, 'bold'), fg='#fff', bg='#ff6961',
                            cursor='hand2', activebackground='#c43740')
        cancel_button.grid(row=len(labels), column=4, padx=10, pady=10, sticky='w')


    def save_history(self,entries,date,id):

        history_data = MedicalHistory(
            id,
            date,
            entries[0].get(),
            entries[1].get(),
            entries[2].get(),
            entries[3].get(),
            entries[4].get(),
            entries[5].get(),
            entries[6].get(),
            entries[7].get(),
            entries[8].get(),
            entries[9].get(),
            entries[10].get()
        )
        history_save(history_data)
        for widget in entries[0].master.winfo_children():
            widget.destroy()
        entries[0].master.destroy()
        self.refresh_table_history(id)

    def refresh_table_history(self, id_card):
        updated_history = show_history(id_card)

        for item in self.table_history.get_children():
            self.table_history.delete(item)

        for data in updated_history:
            self.table_history.insert(
                '', 0, text=data[2], 
                values=(
                    data[3], data[4], data[5], data[6], data[7], data[8], 
                    data[9], data[10], data[11], data[12], data[13]
                ), tags=('evenrow',)
            )
    
    def show_cie(self):
        self.history_view = Toplevel()
        self.history_view.title('CIE10')
        self.history_view.config(bg=pink)
        
        search_code= tk.Label(self.history_view,text='Codigo: ')
        search_code.config(config)
        search_code.grid(column = 4, row = 1, padx= 10, pady = 5 ,sticky = 'e')
        
        search_name= tk.Label(self.history_view,text='Nombre: ')
        search_name.config(config)
        search_name.grid(column = 4, row = 2, padx= 10, pady = 5 ,sticky = 'e')

        self.input_code= tk.Entry(self.history_view, textvariable = tk.StringVar())
        self.input_code.config(width = 30 , font = ('Roboto',15))
        self.input_code.grid(column = 5 , row = 1 ,padx = 10 , pady = 5,columnspan = 2 )

        self.input_sickness= tk.Entry(self.history_view, textvariable = tk.StringVar())
        self.input_sickness.config(width = 30 , font = ('Roboto',15))
        self.input_sickness.grid(column = 5 , row = 2 ,padx = 10 , pady = 5 ,columnspan = 2)
        
        search = tk.Button(self.history_view,text='BUSCAR', command = self.condition_search_cie)
        search.config(width = 20 , font = ('Roboto',12,'bold'),fg = '#fff' , bg ='#a48fc6',
                        cursor='hand2', activebackground='#8672a7')
        search.grid(column = 5 ,row = 3, padx=10,pady=5 , sticky = 'e')
        
        self.cie_table()
    
    def condition_search_cie(self):
        where = ''
        code = self.input_code.get() 
        name = self.input_sickness.get() 
        
        if name != '':
            where = f'name LIKE "%{name}%"'
        elif code != '':
            where = f'code LIKE "%{code}%"'
        elif name != '' and code != '':
            where = f'code LIKE "%{code}%" and name LIKE "%{name}%"'
        
        search_cie(where)
        self.cie_table(where)

    def cie_table(self, where=''):
        # Eliminar cualquier tabla existente antes de crear una nueva
        for widget in self.history_view.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()

        if where != '':
            elements = search_cie(where)
        else:
            elements = all_cie()

        table = ttk.Treeview(self.history_view, columns=('Codigo', 'Nombre'))
        table.grid(column= 4, row=6, columnspan=7, sticky='nse')

        scroll = ttk.Scrollbar(self.history_view, orient='vertical', command=table.yview)
        scroll.grid(row=6, column=17, sticky='nse')

        table.configure(yscrollcommand=scroll.set)

        table.tag_configure('evenrow', background='#c5eafe')

        table.heading('#0', text='Codigo')
        table.heading('#1', text='Nombre')

        table.column('#0', anchor=tk.CENTER, width=150, stretch=False)
        table.column('#1', anchor=tk.CENTER, width=1050, stretch=False)

        for data in elements:
            table.insert('', 'end', text=data[0], values=(data[1:]), tags=('evenrow',))
    

    def show_medicines(self):
        self.medicines_view= Toplevel()
        self.medicines_view.title('MEDICAMENTOS')
        self.medicines_view.config(bg=pink)
        
        search_code= tk.Label(self.medicines_view,text='Nombre: ')
        search_code.config(config)
        search_code.grid(column = 4, row = 1, padx= 10, pady = 5 ,sticky = 'e')
        
        self.input_medicine= tk.Entry(self.medicines_view, textvariable = tk.StringVar())
        self.input_medicine.config(width = 30 , font = ('Roboto',15))
        self.input_medicine.grid(column = 5 , row = 1 ,padx = 10 , pady = 5,columnspan = 2 )

        
        search = tk.Button(self.medicines_view,text='BUSCAR', command = self.condition_search_medicines)
        search.config(width = 20 , font = ('Roboto',12,'bold'),fg = '#fff' , bg ='#a48fc6',
                        cursor='hand2', activebackground='#8672a7')
        search.grid(column = 5 ,row = 3, padx=10,pady=5 , sticky = 'e')
        
        self.medicines_table()
    
    def condition_search_medicines(self):
        where = ''
        code = self.input_medicine.get() 
    
        
        if code != '':
            where = f'Nombre LIKE "%{code}%"'
        
        search_medicine(where)
        self.medicines_table(where)

    def medicines_table(self, where=''):
        # Eliminar cualquier tabla existente antes de crear una nueva
        for widget in self.medicines_view.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()

        if where != '':
            elements = search_medicine(where)
        else:
            elements = all_medicines()

        table = ttk.Treeview(self.medicines_view, columns=('Via Administracion', 'Nombre','Concentracion','Unidad Medida'))
        table.grid(column= 4, row=6, columnspan=7, sticky='nse')

        scroll = ttk.Scrollbar(self.medicines_view, orient='vertical', command=table.yview)
        scroll.grid(row=6, column=17, sticky='nse')

        table.configure(yscrollcommand=scroll.set)

        table.tag_configure('evenrow', background='#c5eafe')

        table.heading('#0', text='Codigo')
        table.heading('#2', text='Nombre')
        table.heading('#3', text='Concentracion')
        table.heading('#4', text='Unidad Medida')

        table.column('#0', anchor=tk.CENTER, width=150, stretch=False)
        table.column('#1', anchor=tk.CENTER, width=1050, stretch=False)
        table.column('#2', anchor=tk.CENTER, width=200, stretch=False)
        table.column('#3', anchor=tk.CENTER, width=200, stretch=False)

        for data in elements:
            table.insert('', 'end', text=data[0], values=(data[1], data[2],data[3]), tags=('evenrow',))
