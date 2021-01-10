import time
import webbrowser as web
import pyautogui as pg
from urllib.parse import quote
import smtplib

class Communication():

    def __init__(self) -> None:
        pass

    def sendwhatmsg(self,phone_no, message):
        """ need to be logged in to Whatsapp on web"""
        wait_time =10
        parsedMessage = quote(message)
        web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
        time.sleep(2)
        width,height = pg.size()
        pg.click(width/2,height/2)
        time.sleep(wait_time-2)
        pg.press('enter')
        

    def sendMail(self,my_mail, my_pass, mail_to, subject, content):
        """
        Sends mail to a person using SMTP. 
        *Before using this function you have to enable less secure app in your email's privacy settings.*
        @params
        my_mail = Your email ID.
        my_pass = Your email password.
        mail_to = Reciver's email ID.
        subject = Subject of the email.
        content = Body of the email.
        """
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()

            server.starttls()
            server.login(my_mail, my_pass) # enter your email and password but you have to enable <less secure app> in your email privacy setting
            server.sendmail(my_mail, mail_to, f"{subject}\n\n{content}") # enter your email, reciver email, subject and content to send
            server.quit()
        
        except Exception as e:
            print(e)

    def sendSMS(self, to_number, message):
        #SMS needs to use a pay account to be send.
        print(f"SMS send to {to_number} with the message: {message}")
