import MySQLdb
import cgi
form = cgi.FieldStorage()
first_name = form.getvalue('First_Name','')
last_name = form.getvalue('Last_Name','')
age = form.getvalue('age',0)
martial_status = form.getvalue('Martial_Status','')
qualification = form.getvalue('Qualification','')
gender = form.getvalue('Gender')
db = MySQLdb.connect("127.0.0.1","chandru","Chandru@1989","chandru")
cursor = db.cursor()
sql = "INSERT into chandru.registration_form(First_Name,Last_Name,Age,Martial_Status,Qualification,Gender)" " VALUES (%s,%s,%s,%s,%s,%s)" 
args = ('mala','Sekar',27,'Single','MCA','Male') 
cursor.execute(sql,args)
db.commit()
cursor.close()
db.close()