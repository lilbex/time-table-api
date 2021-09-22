from decouple import config
from django.core.mail import send_mail



class Util:
    @staticmethod
    def send_email(data):
        email_subject=data['email_subject']
        message=data['email_body']
        email_from = 'lilbex.com@gmail'
        email_to=data['to_email']
        html_format=data['email_body']
        try:
            send_mail(email_subject, message, email_from, email_to,
            fail_silently=False, html_message=html_format)
            return True
        except Exception as err:
            print(str(err))
            return False
