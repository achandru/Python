	#print "Hello"
	#print ('Khandru'.replace('K','C'))
# Library
import MySQLdb
# hostname,username,password,db name
db = MySQLdb.connect("127.0.0.1","chandru","Chandru@1989","sys")
# row by row
cursor = db.cursor()
#sql = "UPDATE sys.student_details SET s_school = 'scooj' WHERE s_name = 'ram' ;"
sql = "INSERT into sys.student_details(s_name,s_class,s_school,s_address)" " VALUES(%s,%s,%s,%s);"
args = ('kiran','LKG','KHSS','Bang')
cursor.execute (sql,args)
db.commit()
	#data = cursor.fetchone ()
	#print str(data)
cursor.close ()
db.close ()	