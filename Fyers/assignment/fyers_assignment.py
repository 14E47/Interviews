import pandas as pd
import mysql.connector as mysql


# data cleanse
file_path = "/home/vee/code/self/Interviews/Fyers/assignment/sample_data.txt"
df = pd.read_csv(file_path)
df.dropna(inplace=True)
df = df.reset_index(drop=True)
df.columns = df.columns.str.strip()
df = df.replace('\W','', regex=True)
r = df.shape[0]
c = df.shape[1]

#############################################################


#TODO : Create DB "emp" if not present

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "emp"
)

cursor = db.cursor()

cursor.execute("SHOW DATABASES")
databases = cursor.fetchall() ## it returns a list of all databases present


#TODO : Create database if db not present in databases
## cursor.execute("CREATE DATABASE emp")

cursor.execute("SHOW TABLES")
tables = cursor.fetchall() ## it returns a list of all tables present in db

# cursor.execute("DROP TABLE emp_details")

#TODO : Create table
## creating a table called 'emp_details' in the 'emp' database
# cursor.execute("CREATE TABLE emp_details (Id INT PRIMARY KEY, First_name VARCHAR(255), Last_Name VARCHAR(255), deparment VARCHAR(255), salary INT)")

for i in range(r):
    v = tuple(df.loc[i])
    values = (int(v[0]), str(v[1]), str(v[2]), str(v[3]), int(v[4]))
    try:
        query = "INSERT INTO emp_details (Id, First_name, Last_Name, deparment, salary) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, values)
        db.commit()
        print(cursor.rowcount, "records inserted")
    except:
        query = "REPLACE INTO emp_details (Id, First_name, Last_Name, deparment, salary) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, values)
        db.commit()
        print(cursor.rowcount, "records owerwritten")


query = "SELECT * FROM emp_details"
cursor.execute(query)
records = cursor.fetchall()
print(len(records),records)
