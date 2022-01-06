from celery import shared_task
from .models import UserAccount, OTP
# -------utilities-------
from random import randint
from Project_TwoWaits.settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from django.template.loader import render_to_string


# ------OTP-------
otp_expire_duration = 2

# -------CHANGE TO CLASS BASED--------
# ------ For Sending OTP to passed E-Mail -------
@shared_task
def send_otp(email):
    # generating 4-digit OTP
    otp = randint(1000,9999)
    # getting account
    user = UserAccount.objects.get(email=email)
    try:
        OTP.objects.create(otp_account_id=user, otp=otp)

    except:
        new_otp = OTP.objects.get(otp_account_id=user)
        new_otp.otp = otp
        new_otp.created = timezone.now()
        new_otp.save()
        
    from_email, to = EMAIL_HOST_USER, email
    subject = "OTP for TwoWaits Sign-Up"
    text_content = f'Your One Time Password for signing up on V-Shop is {otp}.\nValid for only 2 minutes.\nDO NOT SHARE IT WITH ANYBODY.'
    user = email.split('@')[0]
    context = ({'user':user,'otp':otp, 'otp_expire_duration':otp_expire_duration})
    html_content = render_to_string('otp_email.html',context=context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return "email sent"
