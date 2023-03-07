import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Remo '
email['to'] = 'murungiremulus73@gmail.com'
email['subject'] = 'You are great!!'
email.set_content(html.substitute(name='TinTin'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummy@gmail.com', 'Password')
    smtp.send_message(email)
    print('all good Sir!')


