from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('portfoliodetails', views.portfoliodetails, name='portfoliodetails'),
    path('servicedetails', views.servicedetails, name='servicedetails'),
    path('starterpage', views.starterpage, name='starterpage'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),  # Add this line
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)