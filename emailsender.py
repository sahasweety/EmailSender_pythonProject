"""import smtplib

to = input("Enter the email of recipient:\n")
content = input("Enter the content for mail:\n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email@gmail.com', 'your-app-password')  # Use App Password here
    server.sendmail('your-email@gmail.com', to, content)
    server.close()

sendEmail(to, content)"""