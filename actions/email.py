import email, smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from st2common.runners.base_action import Action

class SendEmail(Action):
    def run(self,email_to, subject, body):
      fromaddr = "stackstorm.alert@gmail.com"
      toaddr = email_to
      msg = MIMEMultipart()
      msg['From'] = fromaddr
      msg['To'] = toaddr
      msg['Subject'] = "Python email"
      bd = body
      msg.attach(MIMEText(bd, 'plain'))
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()
      server.ehlo()
      server.login(fromaddr, "harsh6100")
      text = msg.as_string()
      server.sendmail(fromaddr, toaddr, text)
