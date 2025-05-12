import yagmail #to send emails by gmail in Python
import os #environmental variables

sender = '@gmail.com'
receiver = '@gmail.com'

subject = "this is the subject"


contents = """
this is the content of the email
content2
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD')) #creates SMTP object, Simple Mail Transfer Protocol, only to send email
yag.send(to=receiver, subject=subject, contents=contents)
print("email sent")
