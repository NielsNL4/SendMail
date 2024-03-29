import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path


def sendMail():

    weekNum =   input("Weeknummer: ")
    teacher  =   input('Leraar: ')

    email           = 'your@email.com' #your email
    password        = 'password'       #your password, if u have 2 step authentication on u have to create one in your google settings
    send_to_email   = 'receiver@email.com' #the receiver of your mail
    subject         = 'Logboek Week {}'.format(weekNum)
    message         = 'Beste {},\n\nHierbij mijn logboek van week {}.\n\nMet vriendelijke groet,\n\nYour Name'.format(teacher,weekNum)
    file_location   = 'D:\\School\\Logboeken\\Stage\\Your_Name_{}_logboek.pdf'.format(weekNum) #the location of your log with the exact file name as here or u have to change it

    if(teacher == 'name' or teacher == 'name'):
        send_to_email = 'name@mail.com'
    elif(teacher == '' or teacher == ''):
        send_to_email = ''
    elif(teacher == '' or teacher == ''):
        send_to_email = ''
    elif(teacher == '' or teacher == ''):
        send_to_email = ''
    elif(teacher == '' or teacher == ''):
        send_to_email = ''
    elif(teacher == '' or teacher == ''):
        send_to_email = ''
    elif(teacher == '' or teacher == ''):
        send_to_email = input('enter E-mail: ')

    msg             = MIMEMultipart()
    msg['From']     = email
    msg['To']       = send_to_email
    msg['Subject']  = subject

    msg.attach(MIMEText(message, 'plain'))

    # Setup the attachment
    filename    = os.path.basename(file_location)
    attachment  = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # Attach the attachment to the MIMEMultipart object
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()

sendMail()
