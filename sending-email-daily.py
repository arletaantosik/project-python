import yagmail #to send emails by gmail in Python
import os #environmental variables
import time
from datetime import datetime as dt

sender = '@gmail.com'
receiver = '@gmail.com'

subject = "this is the subject"


contents = """
this is the content of the email
content2
"""

while True:
  now = dt.now()
  if now.hour == 13 and now.minute == 15: #send email every day at 13:15
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD')) #creates SMTP object, Simple Mail Transfer Protocol, only to send email
    yag.send(to=receiver, subject=subject, contents=contents)
    print("email sent")
    time.sleep(60) # check every 60 seconds; 3600 seconds = 1 hour

#we can use alternatively PythonAnywhere to execute script every day https://www.pythonanywhere.com
