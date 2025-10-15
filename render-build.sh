#!/bin/bash
# Script de déploiement robuste pour Render

echo "🚀 Démarrage du déploiement..."

# Installer les dépendances
echo "📦 Installation des dépendances..."
pip install -r requirements.txt

# Appliquer les migrations
echo "🗄️ Application des migrations..."
python manage.py migrate --noinput

# Nettoyer les anciens fichiers statiques
echo "🧹 Nettoyage des anciens fichiers statiques..."
rm -rf staticfiles/

# Collecter les fichiers statiques avec plus de verbosité
echo "📁 Collecte des fichiers statiques..."
python manage.py collectstatic --noinput --verbosity=2 --clear

# Vérifier que les fichiers statiques sont bien collectés
echo "🔍 Vérification des fichiers statiques..."
if [ -d "staticfiles" ]; then
    echo "✅ Répertoire staticfiles créé"
    ls -la staticfiles/
    if [ -d "staticfiles/menu" ]; then
        echo "✅ Répertoire menu trouvé"
        ls -la staticfiles/menu/
        if [ -d "staticfiles/menu/menu" ]; then
            echo "✅ Images trouvées:"
            ls -la staticfiles/menu/menu/
        else
            echo "❌ Répertoire menu/menu manquant"
        fi
    else
        echo "❌ Répertoire menu manquant"
    fi
else
    echo "❌ Répertoire staticfiles manquant"
fi

# Exécuter le script de vérification
echo "🔍 Exécution du script de vérification..."
python check_static_files.py

echo "✅ Déploiement terminé!"
