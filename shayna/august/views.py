from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from .forms import ContactForm


# Create your views here.


def index(request):
   template = loader.get_template('august/index.html')
   return HttpResponse(template.render({}, request))


    #return render(request , 'index.html')

def portfoliodetails(request):
    template = loader.get_template('august/portfoliodetails.html')
    return HttpResponse(template.render({}, request))
    return render(request , 'portfoliodetails.html')


def servicedetails(request):
    template = loader.get_template('august/servicedetails.html')
    return HttpResponse(template.render({}, request))
    return render(request , 'servicedetails.html')


def starterpage(request):
    template = loader.get_template('august/starterpage.html')   
    return HttpResponse(template.render({}, request))


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            phone = form.cleaned_data.get('phone', '')
            message = form.cleaned_data['message']

            full_message = f"From: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}"

            send_mail(
                subject,
                full_message,
                email,
                ['simonkaruga945@gmail.com'],  # Replace with your receiving email address
                fail_silently=False,
            )
            return redirect('success')  # Redirect to a success page or any other page
    else:
        form = ContactForm()
    #return render(request, 'contact.html', {'form': form})
    return render(request, 'august/contact.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')



