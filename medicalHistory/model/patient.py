from model.dbconn import DBconnection
from tkinter import messagebox


def save_patient(patient):

    connection = DBconnection()
    sql = f"""INSERT INTO Patient (birth,phone,name,job,gender,id_card,background) VALUES
             ('{patient.birth}', '{patient.phone}', '{patient.name}', '{patient.job}'
             , '{patient.gender}', '{patient.id_card}', '{patient.background}') 
          """
    try:
        connection.cur.execute(sql)
        connection.close_connection()

        title = 'Registrar Paciente'
        message = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title,message)
    except:
        title = 'Registrar Paciente'
        message = 'Error al Registrar Paciente'
        messagebox.showerror(title,message)

class Patient:
     
    def __init__(self,birth,phone,name,job,gender,id_card,background):
        self.birth = birth
        self.phone = phone
        self.name = name
        self.job = job
        self.gender = gender
        self.id_card = id_card
        self.background = background

