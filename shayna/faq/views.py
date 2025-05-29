from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import FAQ



def faq_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq/faq_section.html', {'faqs': faqs})