import MySQLdb
fn = raw_input("Enter Your First_Name")
ln = raw_input("Enter Your Last_Name")
age = raw_input("Enter Your Age")
ms = raw_input("Enter Your Martial_Status")
qf = raw_input("Enter Your Qualification")
gn = raw_input("Enter Your Gender")
db = MySQLdb.connect("127.0.0.1","chandru","Chandru@1989","chandru")
cursor = db.cursor()
sql = "INSERT into chandru.registration_form(First_Name,Last_Name,Age,Martial_Status,Qualification,Gender)" " VALUES (%s,%s,%s,%s,%s,%s)" 
args = (fn,ln,age,ms,qf,gn)
cursor.execute(sql,args)
db.commit()
cursor.close()
db.close()

