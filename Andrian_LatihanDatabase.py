#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE D3_TI_23")


# In[2]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "D3_TI_23"
)

cursorObject = dataBase.cursor()

tblMataKuliah = """CREATE TABLE MATA_KULIAH(
                    KODE_MATA_KULIAH VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA_MATA_KULIAH VARCHAR(50) NOT NULL,
                    WAKTU DATE,
                    RUANGAN VARCHAR(10)
                    )"""

tblMahasiswa = """CREATE TABLE MAHASISWA(
                    NIM VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA_MAHASISWA VARCHAR(30) NOT NULL,
                    ALAMAT VARCHAR(255),
                    MATA_KULIAH_DIIKUTI VARCHAR(10),
                    FOREIGN KEY (MATA_KULIAH_DIIKUTI) REFERENCES MATA_KULIAH(KODE_MATA_KULIAH)
                    )"""

tblDosen = """CREATE TABLE DOSEN(
                NIP VARCHAR(20) NOT NULL PRIMARY KEY,
                NAMA_DOSEN VARCHAR(50) NOT NULL,
                MATA_KULIAH_AJAR VARCHAR(50),
                FOREIGN KEY (MATA_KULIAH_AJAR) REFERENCES MATA_KULIAH(KODE_MATA_KULIAH)
                )"""

cursorObject.execute(tblMataKuliah)
cursorObject.execute(tblMahasiswa)
cursorObject.execute(tblDosen)

dataBase.commit()
dataBase.close()


# In[3]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "D3_TI_23"
)

cursorObject = dataBase.cursor()

insertMatkul = "INSERT INTO MATA_KULIAH (KODE_MATA_KULIAH, NAMA_MATA_KULIAH, WAKTU, RUANGAN) VALUES (%s, %s, %s, %s)"
valueMatkul = [
    ("MK01", "Praktik Basis Data", "2024-03-11", "L2R2"),
    ("MK02", "Praktik Pemrograman Python", "2024-03-11", "L2R2"),
    ("MK03", "Pemorgraman Berorientasi Objek", "2024-03-12", "L2R3"),
    ("MK04", "Praktik Cloud Computing", "2024-03-12", "L2R3"),
    ("MK05", "Praktik Sistem Operasi", "2024-03-13", "L2R2"),
    ("MK06", "Statistika dan Probabilitas", "2024-03-13", "L2R3")
]

insertMahasiswa = "INSERT INTO MAHASISWA (NIM, NAMA_MAHASISWA, ALAMAT, MATA_KULIAH_DIIKUTI) VALUES (%s, %s, %s, %s)"
valueMahasiswa = [
    ("V3923002", "Andrian", "Madiun", "MK01"),
    ("V3923003", "Arvin", "Madiun", "MK02"),
    ("V3923018", "Rossi", "Klaten", "MK03"),
    ("V3923007", "Dimas", "Madiun", "MK04"),
    ("V3923011", "Heigel", "Magetan", "MK05"),
    ("V3923021", "Eggar", "Wonosobo", "MK06")
]

insertDosen = "INSERT INTO DOSEN (NIP, NAMA_DOSEN, MATA_KULIAH_AJAR) VALUES (%s, %s, %s)"
valueDosen = [
    ("1234567891", "Masbahah", "MK01"),
    ("1234567892","Yusuf Fadila Rachman", "MK02"),
    ("1234567893", "Darmawan Lahru Riatma", "MK03"),
    ("1234567894", "Nur Azizul Haqimi", "MK04"),
    ("1234567895", "Nur Azizul Haqimi", "MK05"),
    ("1234567896", "Trisna Ari Roshinta", "MK06")
]

cursorObject.executemany(insertMatkul, valueMatkul)
cursorObject.executemany(insertMahasiswa, valueMahasiswa)
cursorObject.executemany(insertDosen, valueDosen)

dataBase.commit()
dataBase.close()


# In[4]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "D3_TI_23"
)

cursorObject = dataBase.cursor()
showMataKuliah = "SELECT * FROM MATA_KULIAH"
cursorObject.execute(showMataKuliah)
hasil = cursorObject.fetchall()

print("==>Data Tabel Mata Kuliah<==")
for x in hasil:
    print(x)

dataBase.close()


# In[5]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "D3_TI_23"
)

cursorObject = dataBase.cursor()
showMahasiswa = "SELECT * FROM MAHASISWA"
cursorObject.execute(showMahasiswa)
hasil = cursorObject.fetchall()

print("==>Data Tabel Mahasiswa<==")
for x in hasil:
    print(x)

dataBase.close()


# In[6]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "D3_TI_23"
)

cursorObject = dataBase.cursor()
showDosen = "SELECT * FROM DOSEN"
cursorObject.execute(showDosen)
hasil = cursorObject.fetchall()

print("==>Data Tabel Dosen<==")
for x in hasil:
    print(x)

dataBase.close()


# In[7]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "D3_TI_23"
)

cursorObject = dataBase.cursor()
query = """
    SELECT MATA_KULIAH.NAMA_MATA_KULIAH, MAHASISWA.NAMA_MAHASISWA, DOSEN.NAMA_DOSEN
    FROM MAHASISWA
    JOIN MATA_KULIAH ON MAHASISWA.MATA_KULIAH_DIIKUTI = MATA_KULIAH.KODE_MATA_KULIAH
    JOIN DOSEN ON DOSEN.MATA_KULIAH_AJAR = MATA_KULIAH.KODE_MATA_KULIAH
"""

cursorObject.execute(query)
hasil = cursorObject.fetchall()

for row in hasil:
    print("Mata Kuliah : ", row[0])
    print("Mahasiswa : ", row[1])
    print("Dosen : ", row[2])
    print()
    
dataBase.close()


# In[ ]:




