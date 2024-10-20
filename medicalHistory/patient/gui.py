import tkinter as tk
from model.patient import Patient, save_patient

background = '#f9e7ed'

config = {
    'font': ('Roboto', 15, 'bold'),
    'bg': background
}

class Frame(tk.Frame):

    def __init__(self, root):

        super().__init__(root,width= 1280, height=720)
        self.root = root
        self.pack()
        self.config(bg=background)
        self.inputs_patient()


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

        self.input_name = tk.Entry(self, textvariable = tk.StringVar())
        self.input_name.config(width = 30 , font = ('Roboto',15))
        self.input_name.grid(column = 1 , row = 2 ,padx = 10 , pady = 5 ,columnspan = 2)

        self.input_id_card = tk.Entry(self, textvariable = tk.StringVar())
        self.input_id_card.config(width = 30 , font = ('Roboto',15))
        self.input_id_card.grid(column = 1 , row = 1 ,padx = 10 , pady = 5,columnspan = 2)

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

        self.save = tk.Button(self,text='GUARDAR')
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

        save_patient(patient)


