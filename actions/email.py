import smtplib
from st2common.runners.base_action import Action
class SendEmail(Action):
    def run(self):
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("stackstorm.alert@gmail.com", "harsh6100") 
        message = 'aasfdasf'
        s.sendmail("stackstorm.alert@gmail.com", 'harsh6100@gmail.com', message) 
        s.quit() 
