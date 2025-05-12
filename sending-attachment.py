import yagmail
import os

sender = '@gmail.com'
receiver = '@gmail.com'

subject = """
subject
"""
contents = ["""
content
Hi
""", 'text.txt'] #directory of the file which will be attachment

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD')) 
yag.send(to=receiver, subject=subject, contents=contents)
print("email sent")
