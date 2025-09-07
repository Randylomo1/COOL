from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def splash(request):
    return render(request, 'splash.html')

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('account_login')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Contact Form Submission from {name}',
                message,
                email,
                [settings.ADMIN_EMAIL], 
            )
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def faq(request):
    return render(request, 'faq.html')

def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')
