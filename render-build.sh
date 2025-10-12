#!/bin/bash
# Script de déploiement robuste pour Render

echo "🚀 Démarrage du déploiement..."

# Installer les dépendances
echo "📦 Installation des dépendances..."
pip install -r requirements.txt

# Appliquer les migrations
echo "🗄️ Application des migrations..."
python manage.py migrate --noinput

# Collecter les fichiers statiques avec plus de verbosité
echo "📁 Collecte des fichiers statiques..."
python manage.py collectstatic --noinput --verbosity=2

# Vérifier que les fichiers statiques sont bien collectés
echo "🔍 Vérification des fichiers statiques..."
ls -la staticfiles/
ls -la staticfiles/menu/

echo "✅ Déploiement terminé!"
