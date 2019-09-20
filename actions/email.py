import email, smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from st2common.runners.base_action import Action

class SendEmail(Action):
    def run(self,email_to, subject, body):
      sender_email = "stackstorm.alert@gmail.com"
      password = "harsh6100"
        
      message = MIMEMultipart()
      message["From"] = sender_email
      message["To"] = email_to
      message["Subject"] = subject
      
      message.attach(MIMEText(message, "plain"))      
     
      
      context = ssl.create_default_context()
      with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
          server.login(sender_email, password)
          server.sendmail(sender_email, email_to, message)
