import MySQLdb
db = MySQLdb.connect("127.0.0.1","chandru","Chandru@1989","sys")
cursor = db.cursor()
sql = "INSERT into sys.student_details(s_name,s_class,s_school,s_address)" " VALUES (%s,%s,%s,%s);"
args = ('Phani','sixth','KMC','Bang')
cursor.execute(sql,args)
#cursor.execute("INSERT into sys.student_details(s_name,s_class,s_school,s_address) VALUES (%s,%s,%s,%s),"('Suraj','fifth','KMC','Bang'))
db.commit()
cursor.close()
db.close()
