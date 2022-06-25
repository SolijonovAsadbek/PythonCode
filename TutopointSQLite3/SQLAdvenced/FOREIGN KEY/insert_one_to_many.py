import sqlite3

conn = sqlite3.connect('example.db')

conn.execute('''INSERT INTO DOCTOR (NAME, PHONE_NUMBER, TYPE ) VALUES ('John', '91-177 9112', 'Dermatologist')''')
conn.execute('''INSERT INTO DOCTOR (NAME, PHONE_NUMBER, TYPE ) VALUES ('Albert', '90-107 9210', 'Cardiologist')''')
conn.execute('''INSERT INTO DOCTOR (NAME, PHONE_NUMBER, TYPE ) VALUES ('Alex', '91-277 1111', 'Dentist')''')

conn.execute(
    '''INSERT INTO PATIENT (NAME, EMAIL_ADDRESS, PHONE_NUMBER, problem, DOCTOR_ID) 
    VALUES ('Jack', 'jack@gmail.com', '90-290 1234', 'skin burn', 1)''')

conn.execute(
    '''INSERT INTO PATIENT (NAME, EMAIL_ADDRESS, PHONE_NUMBER, problem, DOCTOR_ID) 
    VALUES ('Joe', 'joe@gmail.com', '91-230 2143', 'heart attack', 2)''')

conn.execute(
    '''INSERT INTO PATIENT (NAME, EMAIL_ADDRESS, PHONE_NUMBER, problem, DOCTOR_ID) 
    VALUES ('Ivan', 'ivan@gmail.com', '93-210 1264', 'heart attack', 2)''')

conn.commit()
conn.close()