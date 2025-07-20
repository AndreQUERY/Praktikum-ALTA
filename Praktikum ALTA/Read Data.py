import sqlite3

koneksi_ke_DB = sqlite3.connect('cars.db')

k = koneksi_ke_DB.cursor()

k.execute(""" 
          SELECT*FROM TBCars""")
print(k.fetchall())

koneksi_ke_DB.close()