import sqlite3
from domain import Patient

#service para conectarse con la BD

def get_patient_by_id(patient_id):
    con = sqlite3.connect("tf_backend_api.db")

    #ejecuta consulta
    cur = con.cursor()

    res = cur.execute("SELECT * FROM patient WHERE patient_id_pk = ? ", (patient_id,)).fetchone()
 
    if res:
          #elementos dentro de la respuesta y retornamos como diccionario
        return Patient(res[0], res[1], res[2]).__dict__()
    else:
        return None
    
def add_patient(patient):
    con = sqlite3.connect("tf_backend_api.db")
    cur = con.cursor()

    print(patient)

    try:
        cur.execute("INSERT INTO patient VALUES (?, ?, ?)", (patient.id, patient.name, patient.current_city))
        con.commit()
    except sqlite3.IntegrityError:
        return None
    finally:    
        con.close()