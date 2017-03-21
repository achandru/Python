#print "Hello"
#print ('Khandru'.replace('K','C'))
import MySQLdb
db = MySQLdb.connect("127.0.0.1","chandru","Chandru@1989","sys")
cursor = db.cursor()
sql = "INSERT into sys.student_details(s_name,s_class,s_school,s_address)" " VALUES(%s,%s,%s,%s);"
args = ('sekar','second','uhs','tyr')
cursor.execute (sql,args)
db.commit()
#data = cursor.fetchone ()
#print str(data)
cursor.close ()
db.close ()