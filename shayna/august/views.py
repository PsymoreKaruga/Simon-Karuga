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
    return render(request, 'august/starterpage.html')

def resume(request):
    template = loader.get_template('august/resume.html')
    return HttpResponse(template.render({}, request))
    #return render(request, 'august/resume.html')

def about(request):
    template = loader.get_template('august/about.html')
    return HttpResponse(template.render({}, request))
    #return render(request, 'august/about.html')
    

# The following contact_view and success_view functions are commented out.
# This means they will not be loaded or available in the Django app.
# Use the uncommented versions below if you want these views to be active.

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             phone = form.cleaned_data.get('phone', '')
#             message = form.cleaned_data['message']
#
#             full_message = f"From: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}"
#
#             send_mail(
#                 subject,
#                 full_message,
#                 email,
#                 ['simonkaruga945@gmail.com'],  # Replace with your receiving email address
#                 fail_silently=False,
#             )
#             return redirect('success')  # Redirect to a success page or any other page
#     else:
#         form = ContactForm()
#     #return render(request, 'contact.html', {'form': form})
#     return render(request, 'august/contact.html', {'form': form})
#
# def success_view(request):
#     return render(request, 'august/success.html')



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
                ['simonkaruga945@gmail.com'],  # Replace with your receiving email
                fail_silently=False,

            )
            return redirect('success')  # Redirect to success page
        else:
            # If form is invalid, render with errors
            return render(request, 'august/contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'august/contact.html', {'form': form})

def success_view(request):
    return render(request, 'august/success.html')



# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from .forms import ContactForm

# def index_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             phone = form.cleaned_data.get('phone', '')
#             message = form.cleaned_data['message']
#
#             full_message = f"From: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}"
#
#             send_mail(
#                 subject,
#                 full_message,
#                 email,
#                 ['simonkaruga945@gmail.com'],  # Replace with your receiving email
#                 fail_silently=False,
#             )
#             return redirect('success')  # Redirect to success page
#         else:
#             # Render index with form errors if invalid
#             return render(request, 'index.html', {'form': form})
#     else:
#         # Initialize empty form for GET request
#         form = ContactForm()
#         return render(request, 'august/index.html', {'form': form})
#
# def success_view(request):
#     return render(request, 'august/success.html')
