from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Category, MenuItem
from django import forms
from django.contrib import messages
from twilio.rest import Client
from django.template.loader import render_to_string
from django.http import JsonResponse
import os

def home(request):
    """Vue d'accueil du site Midway Café."""
    context = {"now": timezone.now()}
    return render(request, 'menu/home.html', context)

def menu(request):
    """Vue de la carte du Midway Café."""
    import os
    from django.conf import settings
    categories = Category.objects.all()
    menu_items = MenuItem.objects.all()
    # Récupérer dynamiquement les images extraites du PDF
    images_dir = os.path.join(settings.BASE_DIR, 'menu', 'static', 'menu', 'pdf_images')
    all_images = []
    if os.path.exists(images_dir):
        all_images = [
            f"menu/pdf_images/{img}"
            for img in os.listdir(images_dir)
            if img.lower().endswith(('.jpg', '.jpeg', '.png'))
        ]
        all_images.sort()
    # Images pour Petit Déj
    petit_dej_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0002.jpg',
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0003.jpg',
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0004.jpg',
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0005.jpg',
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0006.jpg',
    ]
    cafe_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0007.jpg',
    ]
    the_boisson_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0008.jpg',
    ]
    jus_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0009.jpg',
    ]
    jwajem_mojito_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0010.jpg',
    ]
    crepe_gaufre_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0011.jpg',
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0012.jpg',
    ]
    fruit_omelette_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0013.jpg',
    ]
    viennoiserie_glace_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0014.jpg',
    ]
    chicha_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0015.jpg',
    ]
    cat = request.GET.get('cat')
    if cat == 'petitdej':
        image_files = [img for img in petit_dej_images if img in all_images]
    elif cat == 'cafe':
        image_files = [img for img in cafe_images if img in all_images]
    elif cat == 'theboisson':
        image_files = [img for img in the_boisson_images if img in all_images]
    elif cat == 'jus':
        image_files = [img for img in jus_images if img in all_images]
    elif cat == 'jwajemmojito':
        image_files = [img for img in jwajem_mojito_images if img in all_images]
    elif cat == 'crepegaufre':
        image_files = [img for img in crepe_gaufre_images if img in all_images]
    elif cat == 'fruitomelette':
        image_files = [img for img in fruit_omelette_images if img in all_images]
    elif cat == 'viennoiserieglace':
        image_files = [img for img in viennoiserie_glace_images if img in all_images]
    elif cat == 'chicha':
        image_files = [img for img in chicha_images if img in all_images]
    else:
        image_files = all_images
    context = {
        'categories': categories,
        'menu_items': menu_items,
        'now': timezone.now(),
        'image_files': image_files,
    }
    return render(request, 'menu/menu.html', context)

class ContactForm(forms.Form):
    nom = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))

def contact(request):
    """Page de contact simplifiée."""
    messages.success(request, "Merci pour votre visite ! Pour nous contacter, utilisez les informations ci-dessous.")
    context = {"now": timezone.now()}
    return render(request, "menu/contact.html", context)

class ReservationForm(forms.Form):
    nom = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    telephone = forms.CharField(label="Numéro de téléphone", max_length=20, widget=forms.TextInput(attrs={"class": "form-control", "type": "tel", "placeholder": "ex: 22 123 456"}))
    date = forms.DateField(label="Date", widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}))
    heure = forms.TimeField(label="Heure", widget=forms.TimeInput(attrs={"type": "time", "class": "form-control"}))
    personnes = forms.IntegerField(label="Nombre de personnes", min_value=1, max_value=20, widget=forms.NumberInput(attrs={"class": "form-control"}))
    message = forms.CharField(label="Message (optionnel)", required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}))

def reservation(request):
    """Page de réservation avec formulaire et confirmation."""
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Récupère les données du formulaire
            nom = form.cleaned_data['nom']
            telephone = form.cleaned_data['telephone']
            date = form.cleaned_data['date']
            heure = form.cleaned_data['heure']
            personnes = form.cleaned_data['personnes']
            message = form.cleaned_data['message']

            # Prépare le message WhatsApp
            whatsapp_message = (
                f"Nouvelle réservation Midway Café :\n"
                f"Nom : {nom}\n"
                f"Téléphone : {telephone}\n"
                f"Date : {date}\n"
                f"Heure : {heure}\n"
                f"Nombre de personnes : {personnes}\n"
                f"Message : {message}"
            )

            # Twilio credentials (from environment variables)
            account_sid = os.getenv('TWILIO_ACCOUNT_SID', '')
            auth_token = os.getenv('TWILIO_AUTH_TOKEN', '')
            
            if account_sid and auth_token:
                client = Client(account_sid, auth_token)
                from_whatsapp = os.getenv('TWILIO_FROM_WHATSAPP', 'whatsapp:+14155238886')
                to_whatsapp = os.getenv('TWILIO_TO_WHATSAPP', 'whatsapp:+21656012373')
            else:
                client = None

            try:
                if client:
                    client.messages.create(
                        body=whatsapp_message,
                        from_=from_whatsapp,
                        to=to_whatsapp
                    )
            except Exception as e:
                print(f"Erreur lors de l'envoi WhatsApp : {e}")

            messages.success(request, "Votre réservation a bien été prise en compte ! Nous vous attendons avec plaisir.")
            return redirect('reservation')  # Redirige vers la page de réservation
    else:
        form = ReservationForm()
    context = {"form": form, "now": timezone.now()}
    return render(request, "menu/reservation.html", context)

def galerie(request):
    """Page galerie photos ambiance et produits."""
    images = [
        {"url": "/static/menu/café.jpg", "alt": "Ambiance café"},
        {"url": "/static/menu/patisserie.png", "alt": "Pâtisserie maison"},
        {"url": "/static/menu/behy3.jpg", "alt": "Notre barista"},
        {"url": "/static/menu/gaufres.jpg", "alt": "Gaufres maison"},
        {"url": "/static/menu/cakes.jpg", "alt": "Cakes gourmands"},
        {"url": "/static/menu/behy1.jpg", "alt": "Espace détente"},
        {"url": "/static/menu/behy.jpg", "alt": "Coin cosy"},
        {"url": "/static/menu/conviviale.jpg", "alt": "Ambiance conviviale"},
    ]
    context = {"images": images, "now": timezone.now()}
    return render(request, "menu/galerie.html", context)

def menu_gallery_partial(request):
    cat = request.GET.get('cat')
    import os
    from django.conf import settings
    images_dir = os.path.join(settings.BASE_DIR, 'menu', 'static', 'menu', 'pdf_images')
    all_images = []
    if os.path.exists(images_dir):
        all_images = [
            f"menu/pdf_images/{img}"
            for img in os.listdir(images_dir)
            if img.lower().endswith(('.jpg', '.jpeg', '.png'))
        ]
        all_images.sort()
    petit_dej_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0002.jpg',
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0003.jpg',
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0004.jpg',
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0005.jpg',
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0006.jpg',
    ]
    cafe_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0007.jpg',
    ]
    the_boisson_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0008.jpg',
    ]
    jus_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0009.jpg',
    ]
    jwajem_mojito_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0010.jpg',
    ]
    crepe_gaufre_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0011.jpg',
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0012.jpg',
    ]
    fruit_omelette_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0013.jpg',
    ]
    viennoiserie_glace_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0014.jpg',
    ]
    chicha_images = [
        'menu/pdf_images/Brown Vintage Cafe Menu_page-0015.jpg',
    ]
    if cat == 'petitdej':
        image_files = [img for img in petit_dej_images if img in all_images]
    elif cat == 'cafe':
        image_files = [img for img in cafe_images if img in all_images]
    elif cat == 'theboisson':
        image_files = [img for img in the_boisson_images if img in all_images]
    elif cat == 'jus':
        image_files = [img for img in jus_images if img in all_images]
    elif cat == 'jwajemmojito':
        image_files = [img for img in jwajem_mojito_images if img in all_images]
    elif cat == 'crepegaufre':
        image_files = [img for img in crepe_gaufre_images if img in all_images]
    elif cat == 'fruitomelette':
        image_files = [img for img in fruit_omelette_images if img in all_images]
    elif cat == 'viennoiserieglace':
        image_files = [img for img in viennoiserie_glace_images if img in all_images]
    elif cat == 'chicha':
        image_files = [img for img in chicha_images if img in all_images]
    else:
        image_files = all_images
    html = render_to_string('menu/partials/gallery.html', {'image_files': image_files}, request=request)
    return JsonResponse({'html': html})