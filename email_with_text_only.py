import smtplib
emailTo = "avdhootavhad@gmail.com"
emailfrom = "avdhootavhad2018.elect@mmcoe.edu.in"
loginId = "avdhootavhad2018.elect@mmcoe.edu.in"
msg = """You Either win or learn you never lose"""
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(loginId, "******************")
server.sendmail(emailfrom, emailTo, msg)
server.quit()
print("Email Sent, Check your gmail")
