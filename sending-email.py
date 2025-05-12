import yagmail #to send emails by gmail in Python
import os #environmental variables
import time

sender = '@gmail.com'
receiver = '@gmail.com'

subject = "this is the subject"


contents = """
this is the content of the email
content2
"""

while True:
  yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD')) #creates SMTP object, Simple Mail Transfer Protocol, only to send email
  yag.send(to=receiver, subject=subject, contents=contents)
  print("email sent")
  time.sleep(60) # so the same email is being sent every 60 seconds
