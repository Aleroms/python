import smtplib

my_email = "dejaentendu2013@gmail.com"
pw="pejorgyjhxactsoo"
msg = "Hello World!"
connection = smtplib.SMTP("outlook.office365.com", port=587)
# transfer layer security: secures connection
connection.starttls()
connection.login(user=my_email, password=pw)
connection.sendmail(from_addr=my_email, to_addrs="ccastu.green@outlook.com", msg=msg)
connection.close()
