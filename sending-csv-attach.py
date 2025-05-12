import yagmail
import os
import pandas

sender = '@gmail.com'

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

df = pandas.read_csv('contacts.csv') #name, email
#sends email to all in the contacts.csv

for index, row in df.iterrows(): #for each row, row -> dictionary, row[name], row[email]
  receiver_email = row['email']
  subject = "subject!!!!!"
  contents = [f"""
  Hi {row['name']} pay {row['amount']}
  Hi
  """,
  row['filepath'], #filepath -> to the file which has to be attached
  ]
  yag.send(to=row['email'], subject=subject, contents=contents)
  print("email sent")
