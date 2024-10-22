from model.dbconn import DBconnection
from tkinter import messagebox


def uptade_patient(patient,id):

    connection = DBconnection()
    sql = f"""UPDATE Patient SET 
             birth = '{patient.birth}', 
             phone = '{patient.phone}', 
             name = '{patient.name}', 
             job = '{patient.job}',
             gender = '{patient.gender}', 
             id_card = '{patient.id_card}', 
             background = '{patient.background}' 
             WHERE id_card = '{id}'
          """
    if (patient.birth == '' or patient.phone == '' or patient.name == '' 
        or patient.job == '' or patient.gender == '' 
        or patient.id_card == '' or patient.background == '' or id == None):

        title = 'Editar Paciente'
        message = 'Error al Editar Paciente'
        messagebox.showerror(title,message)
        return

    try:
        connection.cur.execute(sql)
        connection.close_connection()

        title = 'Editar Paciente'
        message = 'Paciente Editado Exitosamente'
        messagebox.showinfo(title,message)
    except :
        title = 'Editar Paciente'
        message = 'Error al Editar Paciente' 
        messagebox.showerror(title,message)

def save_patient(patient):

    connection = DBconnection()
    sql = f"""INSERT INTO Patient (birth,phone,name,job,gender,id_card,background) VALUES
             ('{patient.birth}', '{patient.phone}', '{patient.name}', '{patient.job}'
             , '{patient.gender}', '{patient.id_card}', '{patient.background}') 
          """
    if (patient.birth == '' or patient.phone == '' or patient.name == '' 
        or patient.job == '' or patient.gender == '' 
        or patient.id_card == '' or patient.background == ''):

        title = 'Registrar Paciente'
        message = 'Error al Registrar Paciente'
        messagebox.showerror(title,message)
        return

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

def show_patients():
    connection = DBconnection()
    array_patients = []

    
    sql =  f""" SELECT id_card ,name ,job,phone,gender,background,
            (strftime('%Y', 'now') - strftime('%Y', birth)) - 
            (strftime('%m-%d', 'now') < strftime('%m-%d', birth)) AS Edad,
            birth, id_patient
            FROM Patient
            """
    try:
        connection.cur.execute(sql)
        array_patients = connection.cur.fetchall()
        connection.close_connection()
      
    except:
        title = 'DATOS'
        message = 'No existen Registros'
        messagebox.showwarning(title,message)

    return array_patients

def search_condition(where):
    connection = DBconnection()
    array_patients = []
    sql =  f""" SELECT id_card ,name ,job,phone,gender,background,
            (strftime('%Y', 'now') - strftime('%Y', birth)) - 
            (strftime('%m-%d', 'now') < strftime('%m-%d', birth)) AS Edad
            , birth , id_patient
            FROM Patient
            """

    if where != '':
        sql+= f' WHERE {where}'
    
    try:
        connection.cur.execute(sql)
        array_patients = connection.cur.fetchall()
        connection.close_connection()
      
    except:
        title = 'DATOS'
        message = 'No existen Registros'
        messagebox.showwarning(title,message)
    
    return array_patients

class Patient:
     
    def __init__(self,birth,phone,name,job,gender,id_card,background):
        self.birth = birth
        self.phone = phone
        self.name = name
        self.job = job
        self.gender = gender
        self.id_card = id_card
        self.background = background

