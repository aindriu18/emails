import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# path gives us access to index.html. We can use read_text method to read it as a string.
# We wrap in Template so it becomes a template object
html = Template(Path('index.html').read_text())

# this is our email object
email = EmailMessage()

# from here we can add to the object
email['from'] = 'Andrew English'
email['to'] = 'receive.email@gmail.com'
email['subject'] = 'testing email'

# sets the content of the email - can use text, html and images
# substitute can have multiple params - kwargs, dictionary
email.set_content(html.substitute(name='John'), 'html')

# need to use smtp server to log into our email client, then send the email from there.
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:

    # part of smtp protocol - google as to why it is ehlo
    smtp.ehlo()

    # tls is an encryption mechanism
    smtp.starttls()

    smtp.login('your.email@gmail.com', 'pilhgyeyupisnjij')

    smtp.send_message(email)

