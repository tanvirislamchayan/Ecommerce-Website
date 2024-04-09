from django.conf import settings
from django.core.mail import send_mail




def send_email_activation_mail(email, email_token):
    subject = 'Verify accunt of Django website'
    email_from = settings.EMAIL_HOST_USER
    message = f'Hi, Please click on the link to activate your email on Django website.  http://localhost:8000/account/activate/{email_token}'

    send_mail(subject, message, email_from, [email])