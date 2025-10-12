from django.conf import settings
from django.http import HttpResponse, Http404
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_http_methods
import os
import mimetypes

@require_http_methods(["GET"])
@cache_control(max_age=3600)
def serve_static_image(request, path):
    """
    Vue pour servir les images statiques en production
    """
    # Construire le chemin complet vers l'image
    full_path = os.path.join(settings.BASE_DIR, 'menu', 'static', 'menu', path)
    
    # Vérifier que le fichier existe
    if not os.path.exists(full_path):
        raise Http404("Image not found")
    
    # Déterminer le type MIME
    content_type, _ = mimetypes.guess_type(full_path)
    if content_type is None:
        content_type = 'application/octet-stream'
    
    # Lire et retourner le fichier
    with open(full_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type=content_type)
        response['Content-Length'] = os.path.getsize(full_path)
        return response
