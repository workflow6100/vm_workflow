import smtplib
from st2common.runners.base_action import Action
class SendEmail(Action):
    def run(self,email_to):
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("stackstorm.alert@gmail.com", "harsh6100") 
        message = 'VM successfully Created'
        s.sendmail("stackstorm.alert@gmail.com", email_to, message) 
        s.quit() 
