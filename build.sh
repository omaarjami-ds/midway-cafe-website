#!/bin/bash
# Build script pour Render.com
# Ce script corrige les problèmes courants de déploiement Django

echo "🚀 Démarrage du build pour Render..."

# Installer les dépendances
echo "📦 Installation des dépendances..."
pip install -r requirements.txt

# Appliquer les migrations
echo "🗄️ Application des migrations..."
python manage.py migrate

# Collecter les fichiers statiques
echo "📁 Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

# Vérifier la configuration
echo "✅ Vérification de la configuration..."
python manage.py check

echo "🎉 Build terminé avec succès!"
