#!/bin/bash
# Script de test pour vérifier les images sur Render

echo "🔍 Test des images sur Render..."

# Test de l'image principale
echo "📸 Test de l'image café.jpg..."
curl -I https://midway-cafe-website.onrender.com/static/menu/café.jpg

echo ""
echo "📸 Test de l'image accueil.jpg..."
curl -I https://midway-cafe-website.onrender.com/static/menu/accueil.jpg

echo ""
echo "📸 Test de l'image patisserie.png..."
curl -I https://midway-cafe-website.onrender.com/static/menu/patisserie.png

echo ""
echo "✅ Tests terminés!"
