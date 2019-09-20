import smtplib
from st2common.runners.base_action import Action
class SendEmail(Action):
    def run(self,email_to, subject, body):
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("stackstorm.alert@gmail.com", "harsh6100") 
        message = "Message_you_need_to_send"
        s.sendmail("stackstorm.alert@gmail.com", "harsh6100@gmail.com", message) 
        s.quit() 
