from django.shortcuts import render, redirect
from .forms import regForm
import secrets
from django.core.mail import send_mail
from django.contrib.auth.models import User


def reg(request):
    if request.method == 'POST':
        form = regForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('verify')
    else:
        form = regForm()
    return render(request, 'main/reg.html', {'form': form})


def welcome(request):
    return render(request, 'main/welcome.html')

def verify(request):
    return render(request, 'main/verify.html')

def generate_verification_token():
    return secrets.token_urlsafe(32)

def send_verification_email(user_email, verification_token):
    verification_url = f'http://127.0.0.1:8000/verify/{verification_token}'
    subject = 'Email Verification'
    message = f'Please click the link below to verify your email: {verification_url}'
    sender_email = ''
    send_mail(subject, message, sender_email, [user_email])

def verify_email(request, verification_token):
    try:
        user = User.objects.get(verification_token=verification_token)
    except User.DoesNotExist:
        return render(request, 'invalid_verification.html')

    user.is_verified = True
    user.save()

    return redirect('welcome')
