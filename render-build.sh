#!/bin/bash
# Script de déploiement simple pour Render

echo "🚀 Démarrage du déploiement..."

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate --noinput

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

echo "✅ Déploiement terminé!"
