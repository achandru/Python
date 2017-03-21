#user = raw_input("Enter the string: ")
import webbrowser
weburl = ("http://52.86.203.79/v1.4/app/questions/getquestions?use_case_id")
user = raw_input("Use case id")
webbrowser.open (weburl+user)