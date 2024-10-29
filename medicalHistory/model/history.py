from model.dbconn import DBconnection
from tkinter import messagebox

def save(history):
    
    conn = DBconnection()
    sql = f""" INSERT INTO Consult (id_patient,day_of_visit,complaint,review,blood_pressure,heart_rate,respiratory_rate,weight,height,oxygen_saturation,diagnosis,treatment,assessment) 
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
              '{history.assessment}'
              )
              
          """ 

    try:
        connection.cur.execute(sql)
        connection.close_connection()

        title = 'Historia Clinica'
        message = 'Historia Clinica Registrada Exitosamente'
        messagebox.showinfo(title,message)
    except:
        title = 'Historia Clinica'
        message = 'Error al Registrar Historia Clinica'
        messagebox.showerror(title,message)


def show_history(id):
    history_array = []
    connection = DBconnection()

    sql = f"""SELECT h.id_patient ,p.name, h.day_of_visit,h.complaint,h.review,h.blood_pressure,h.heart_rate,h.respiratory_rate,h.weight,h.height,h.oxygen_saturation,h.diagnosis,h.treatment,h.assessment 
          FROM Consult h INNER JOIN Patient p 
          ON h.id_patient = p.id_card
          WHERE p.id_card = {id}
           """ 
    print(id)
  
    try:
        connection.cur.execute(sql)
        history_array = connection.cur.fetchall()
        connection.close_connection()
      
    except Exception as e:
        title = 'HISTORIA CLINICA'
        message = f'No existen Registros {e}'
        messagebox.showwarning(title,message)

    return history_array 


class MedicalHistory:
    
    def __init__(self,id_card,day,complaint,review,blood_pressure,heart_rate,respiratory_rate,
                 weight,height,oxygen_saturation,diagnosis,treatment,assessment):


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


    def __str__(self):
        return f'MedicalHistory[{self.id_card},{self.day},{self.complaint},{self.review},{self.blood_pressure},{self.heart_rate},{self.respiratory_rate},{self.weight},{self.height},{self.oxygen_saturation},{self.diagnosis},{self.treatment},{self.assessment}]'
