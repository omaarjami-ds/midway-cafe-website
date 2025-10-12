from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def static_image(image_path):
    """
    Template tag pour servir les images via notre endpoint personnalisé
    """
    if settings.DEBUG:
        # En développement, utiliser le système statique normal
        return f"/static/menu/{image_path}"
    else:
        # En production, utiliser notre endpoint personnalisé
        return f"/static-images/{image_path}"
