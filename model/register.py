import psycopg2
conn = psycopg2.connect(database="Eleves", user="postgres", password="250592",host="127.0.0.1", port="5050")
print ("Opened database successfully")
cur = conn.cursor()
cur.execute('''CREATE TABLE student(id_student SERIAL PRIMARY KEY ,nom_student TEXT NOT NULL,prenom_student CHAR(50));''')
cur.execute('''CREATE TABLE classes(id_class SERIAL PRIMARY KEY ,nom_class TEXT NOT NULL,class_places int);''')
print ("Table created successfully")
conn.commit()
conn.close()
