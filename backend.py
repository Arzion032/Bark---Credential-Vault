import mysql.connector
from tkinter import messagebox

host = "localhost"
user = "melvin_032"
password = "Immelvin_032mysql"
schema = "batman"
database = "crud"

def CreateDatabase():
    mysqldb = mysql.connector.connect(
    host=host,
    user=user,
    password=password
    )
    with mysqldb.cursor() as mycursor:
        mycursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
    
        mycursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {schema}.{database} (
            id VARCHAR(50) PRIMARY KEY,
            studname VARCHAR(255),
            contact VARCHAR(15),
            department VARCHAR(255))""")
    
    mysqldb.commit()
    mysqldb.close()
def Create(studid,studname,contact,department):

    mysqldb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    )
    
    with mysqldb.cursor() as mycursor_for_query:
        mycursor_for_query.execute(f"SELECT COUNT(*) FROM {schema}.{database} WHERE id = '{studid}'")
        result = mycursor_for_query.fetchone()
        
    id_exists = result[0] > 0
    
    if id_exists:
        messagebox.showerror("Error", "ID already exists")
    else:
        try:
            with mysqldb.cursor() as mycursor_for_insert:
                mycursor_for_insert.execute(f"INSERT INTO {schema}.{database} (id, studname, contact, department) VALUES (%s, %s, %s, %s)",
    (studid, studname, contact, department))
            mysqldb.commit()
            messagebox.showinfo("Information", "Employee inserted successfully...")
            
        except Exception as e:
            print(e)
            mysqldb.rollback()
            messagebox.showerror("Error", "An error occurred while inserting the record")
        finally:
            mysqldb.close()
            
def Read(studid, studname, contact, department):
    mysqldb = mysql.connector.connect(host=host, user=user, password=password, database=schema)
    mycursor = mysqldb.cursor()
    mycursor.execute(f"SELECT * FROM {schema}.{database}  WHERE id = %s OR studname = %s OR contact = %s OR department = %s", (studid,studname,contact,department))
    records = mycursor.fetchall()
    mysqldb.close()
    return records

def Update(studid,studname,contact,department):
    mysqldb = mysql.connector.connect(host=host, user=user, password=password, database=schema)
    
    try:
        with mysqldb.cursor() as myupdatecursor:
            myupdatecursor.execute(f"UPDATE {schema}.{database} SET studname = %s, contact = %s, department = %s WHERE id = %s", (studname,contact,department,studid))
            mysqldb.commit()
            myupdatecursor.close()
            mysqldb.close()
            messagebox.showinfo("Information", "Employee updated successfully...")
    except Exception as e:
        print(e)
        mysqldb.rollback()
        messagebox.showerror("Error", "An error occurred while updating the record")
        
    
    
    
def Delete(studid,studname,contact,department):
    mysqldb = mysql.connector.connect(host=host, user=user, password=password, database=schema)
    mycursor = mysqldb.cursor()
    mycursor.execute(f"DELETE FROM {schema}.{database} WHERE id = %s AND studname = %s AND contact = %s AND department = %s", (studid,studname,contact,department))
    mysqldb.commit()
    mysqldb.close()
    messagebox.showinfo("Information", "Employee deleted successfully...")
    
def Show():
    CreateDatabase()
    mysqldb = mysql.connector.connect(host=host, user=user, password=password, database=schema)
    mycursor = mysqldb.cursor()
    mycursor.execute(f"SELECT id, studname, contact, department FROM {schema}.{database}")
    records = mycursor.fetchall()
    mysqldb.close()
    return records