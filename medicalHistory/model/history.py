from model.dbconn import DBconnection
from tkinter import messagebox

def history_save(history):
    
    connection = DBconnection()
    sql = f""" INSERT INTO Consult (id_patient,day_of_visit,complaint,review,blood_pressure,heart_rate,respiratory_rate,weight,height,oxygen_saturation,diagnosis,treatment,assessment,discovers) 
              VALUES 
              ( 
              '{history.id_card}',
              '{history.day}',
              '{history.complaint}',
              '{history.review}',
              '{history.blood_pressure}',
              '{history.heart_rate}',
              '{history.respiratory_rate}',
              '{history.weight}',
              '{history.height}',
              '{history.oxygen_saturation}',
              '{history.diagnosis}',
              '{history.treatment}',
              '{history.assessment}',
              '{history.discovers}'
              )
              
          """ 

    try:
        connection.cur.execute(sql)
        connection.close_connection()

        title = 'Historia Clinica'
        message = 'Historia Clinica Registrada Exitosamente'
        messagebox.showinfo(title,message)
    except Exception as e :
        title = 'Historia Clinica'
        message = f'Error al Registrar Historia Clinica {e}'
        messagebox.showerror(title,message)


def show_history(id):
    history_array = []
    connection = DBconnection()

    sql = f"""SELECT h.id_patient ,p.name, h.day_of_visit,h.complaint,h.review,h.blood_pressure,h.heart_rate,h.respiratory_rate,h.weight,h.height,h.oxygen_saturation,h.discovers,h.diagnosis,h.treatment,h.assessment 
          FROM Consult h INNER JOIN Patient p 
          ON h.id_patient = p.id_card
          WHERE p.id_card = {id}
           """ 
  
    try:
        connection.cur.execute(sql)
        history_array = connection.cur.fetchall()
        connection.close_connection()
      
    except Exception as e:
        title = 'HISTORIA CLINICA'
        message = f'No existen Registros {e}'
        messagebox.showwarning(title,message)

    return history_array 


def all_cie():
    data = []
    connection = DBconnection()
    sql = f""" SELECT code , name FROM CIE10 ORDER BY code DESC"""
    try:
        connection.cur.execute(sql)
        data  = connection.cur.fetchall()
        connection.close_connection()
      
    except Exception as e:
        title = 'CIE10'
        message = f'No existen Registros {e}'
        messagebox.showwarning(title,message)

    return data 

def search_cie(where):
    connection = DBconnection()
    array_patients = []
    
    sql =  """ SELECT code, name FROM CIE10 
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

def all_medicines():
    data = []
    connection = DBconnection()
    sql = f""" SELECT ViaAdministracion,Nombre,Concentracion,UnidadMedida FROM Medicamentos"""
    try:
        connection.cur.execute(sql)
        data  = connection.cur.fetchall()
        connection.close_connection()
      
    except Exception as e:
        title = 'Medicamentos'
        message = f'No existen Registros {e}'
        messagebox.showwarning(title,message)

    return data 

def search_medicine(where):
    connection = DBconnection()
    array_patients = []
    
    sql = f""" SELECT ViaAdministracion,Nombre,Concentracion,UnidadMedida FROM Medicamentos"""

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

def all_test():
    data = []
    connection = DBconnection()
    sql = f""" SELECT nombre FROM Examenes"""
    try:
        connection.cur.execute(sql)
        data  = connection.cur.fetchall()
        connection.close_connection()
      
    except Exception as e:
        title = 'Examenes de Laboratorio'
        message = f'No existen Registros {e}'
        messagebox.showwarning(title,message)

    return data 

def search_test(where):
    connection = DBconnection()
    array_patients = []
    
    sql = f""" SELECT nombre FROM Examenes"""

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

class MedicalHistory:
    
    def __init__(self,id_card,day,complaint,review,blood_pressure,heart_rate,respiratory_rate,
                 weight,height,oxygen_saturation,diagnosis,treatment,assessment,discovers):


        self.id_card  = id_card
        self.day = day 
        self.complaint = complaint
        self.review = review
        self.blood_pressure = blood_pressure
        self.heart_rate = heart_rate
        self.respiratory_rate = respiratory_rate
        self.weight = weight
        self.height = height
        self.oxygen_saturation = oxygen_saturation
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.assessment = assessment
        self.discovers = discovers


    def __str__(self):
        return f'MedicalHistory[{self.id_card},{self.day},{self.complaint},{self.review},{self.blood_pressure},{self.heart_rate},{self.respiratory_rate},{self.weight},{self.height},{self.oxygen_saturation},{self.diagnosis},{self.treatment},{self.assessment},{self.discovers}]'
