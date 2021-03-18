import smtplib
import re
from email.mime.text import MIMEText
from email.header    import Header
from datetime import date
userid = 'unknown@cisco.com' #any userid u can give
passid = "anypassword" #any password u can give
today = str(date.today())
#below is used to import file information
'''status = open('Todays_Status.txt','r')
str = status.read()
i = re.search(today,str).end()
for j in range(i,len(str)):
	if str[j] == ';':
		break
today_status = str[i:j]'''
today_status = "\nhello how r u\n"
Salutation = 'Hi,\n'
greeting = '\nRegards,\nDevil.'
today_status = Salutation + today_status + greeting
receivers = ['anyid1@cisco.com','anyid2@cisco.com'] #any valid userid uses cisco outlook mail.
message = MIMEText(today_status,'plain','utf-8')
message['subject'] = Header('U want any help?','utf-8')
message['from'] = userid
message['to'] = ', '.join(receivers)
smtpObj = smtplib.SMTP('mail.cisco.com')
#smtpObj.set_debuglevel(1)
try:
	print("Sending.....")
	smtpObj.starttls()
	smtpObj.sendmail(userid, receivers, message.as_string())
	print("Successfully sent email")
except Exception as e:
	print(e)
	print("Error: unable to send email")
finally:
	smtpObj.quit()
