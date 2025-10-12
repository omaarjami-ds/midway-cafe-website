from django.urls import path
from . import views
from . import static_views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('menu/gallery_partial/', views.menu_gallery_partial, name='menu_gallery_partial'),
    path('reservation/', views.reservation, name='reservation'),
    path('contact/', views.contact, name='contact'),
    path('galerie/', views.galerie, name='galerie'),
    # Endpoint pour servir les images statiques
    path('static-images/<str:path>', static_views.serve_static_image, name='serve_static_image'),
]
