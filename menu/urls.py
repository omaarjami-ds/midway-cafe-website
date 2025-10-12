from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('menu/gallery_partial/', views.menu_gallery_partial, name='menu_gallery_partial'),
    path('reservation/', views.reservation, name='reservation'),
    path('contact/', views.contact, name='contact'),
    path('galerie/', views.galerie, name='galerie'),
]
