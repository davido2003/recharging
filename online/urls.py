from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('buslist/', views.buslist, name='buslist'),
    path('bus/', views.bus, name='bus'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('feedback/', views.feedback, name='feedback'),
    path('icons/', views.icons, name='icons'),
    path('movies/', views.movies, name='movies'),
    path('pay/', views.pay, name='pay'),
    path('plans/', views.plans, name='plans'),
    path('selectshow/', views.selectshow, name='selectshow'),
    path('shortcodes/', views.shortcodes, name='shortcodes'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('support/', views.support, name='support'),
    path('terms/', views.terms, name='terms'),
    path('train/', views.train, name='train'),
    path('trainslist/', views.trainslist, name='trainslist'),
    
]