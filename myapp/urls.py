
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),

    path('doc/', views.doctors, name='doc'),
    path('myservice/', views.myservice, name='myservice'),
    path('appointment/', views.appointment, name='appointment'),
    path('show/', views.show, name='show'),

    path('delete/<int:id>', views.delete),

    path('contact/', views.contact, name='contact'),

    path('details/', views.detail, name='detail'),

    path('delete/<int:id>', views.delete),
]
