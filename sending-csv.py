import yagmail
import os
import pandas

sender = '@gmail.com'

subject = """
subject
"""

yag = yagmail.SMTP(user=sender, password="Gmail App Password")

df = pandas.read_csv('contacts.csv') #name, email
#sends email to all in the contacts.csv

for index, row in df.iterrows(): #for each row, row -> dictionary, row[name], row[email]
  contents = f"""
Hi {row['name']} the content of the email
Hi
"""
  yag.send(to=row['email'], subject=subject, contents=contents)
  print("email sent")
