import smtplib, ssl

port = 587  # For starttls
message = """\
Subject: Hi there

This message is sent from Python."""
smtp_server = "smtp.gmail.com"
sender_email = "snippythelobster@gmail.com"  # Enter your address
receiver_email = "friedmanjzachary@gmail.com"  # Enter receiver address
password = "beautifulsoup"


import pdb; pdb.set_trace()

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)