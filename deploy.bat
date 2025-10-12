@echo off
echo 🚀 DÉPLOIEMENT MIDWAY CAFÉ
echo ==========================
echo.

echo 📋 Vérification des fichiers...
if not exist "requirements.txt" (
    echo ❌ Erreur: requirements.txt manquant
    pause
    exit /b 1
)

if not exist "Procfile" (
    echo ❌ Erreur: Procfile manquant
    pause
    exit /b 1
)

echo ✅ Fichiers de déploiement présents
echo.

echo 🔧 Préparation du déploiement...
echo.

echo 📝 Instructions de déploiement :
echo.
echo 1. Créez un repository GitHub :
echo    - Allez sur https://github.com
echo    - Créez un nouveau repository : midway-cafe-website
echo    - Copiez l'URL de votre repository
echo.
echo 2. Connectez votre projet :
echo    git remote add origin VOTRE_URL_GITHUB
echo    git branch -M main
echo    git push -u origin main
echo.
echo 3. Déployez sur Railway :
echo    - Allez sur https://railway.app
echo    - Connectez-vous avec GitHub
echo    - Créez un nouveau projet depuis votre repository
echo    - Ajoutez les variables d'environnement (voir DEPLOYMENT_INFO.txt)
echo.
echo 4. Votre site sera en ligne !
echo.
echo 📱 Variables d'environnement pour Railway :
echo DEBUG=False
echo SECRET_KEY=NUrwUxyrzKzjN7BhpgQE7f9zb0PMZW2-Va2HNsrKcHFSVLVu1_e8iYKV1S1CfQKmPyw
echo ALLOWED_HOSTS=*.railway.app,midway-cafe-production.up.railway.app
echo.
echo 🎉 Votre site Midway Café sera bientôt en ligne !
echo.
pause
