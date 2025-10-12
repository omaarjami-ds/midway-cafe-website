#!/bin/bash
# Script de build simple pour Render

echo "🚀 Démarrage du build..."

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate --noinput

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

echo "✅ Build terminé!"
