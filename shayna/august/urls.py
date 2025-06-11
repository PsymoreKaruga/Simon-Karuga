from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.starterpage, name='starterpage'),
    path('index', views.index, name='index'),
    path('portfoliodetails', views.portfoliodetails, name='portfoliodetails'),
    path('servicedetails', views.servicedetails, name='servicedetails'),
    
    path('resume', views.resume, name='resume'),
    path('about', views.about, name='about'),

    path('contact/', views.contact_view, name='contact'),
    
    path('success/', views.success_view, name='success'),
    path('contact/success/', views.success_view, name='success'),
    #path('resume/', views.resume_view, name='resume'),  # Add this line
    #path('', views.index_view, name='index'),
    #path('success/', views.success_view, name='success'), # Add this line
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)