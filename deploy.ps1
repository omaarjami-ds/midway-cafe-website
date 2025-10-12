# 🚀 Script de déploiement Midway Café
Write-Host "🚀 DÉPLOIEMENT MIDWAY CAFÉ" -ForegroundColor Green
Write-Host "==========================" -ForegroundColor Green
Write-Host ""

# Vérification des fichiers
Write-Host "📋 Vérification des fichiers..." -ForegroundColor Yellow
$requiredFiles = @("requirements.txt", "Procfile", "runtime.txt", ".gitignore")

foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "✅ $file présent" -ForegroundColor Green
    } else {
        Write-Host "❌ $file manquant" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "🔧 Préparation du déploiement..." -ForegroundColor Yellow
Write-Host ""

# Instructions
Write-Host "📝 INSTRUCTIONS DE DÉPLOIEMENT :" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Créez un repository GitHub :" -ForegroundColor White
Write-Host "   - Allez sur https://github.com" -ForegroundColor Gray
Write-Host "   - Créez un nouveau repository : midway-cafe-website" -ForegroundColor Gray
Write-Host "   - Copiez l'URL de votre repository" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Connectez votre projet :" -ForegroundColor White
Write-Host "   git remote add origin VOTRE_URL_GITHUB" -ForegroundColor Gray
Write-Host "   git branch -M main" -ForegroundColor Gray
Write-Host "   git push -u origin main" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Déployez sur Railway :" -ForegroundColor White
Write-Host "   - Allez sur https://railway.app" -ForegroundColor Gray
Write-Host "   - Connectez-vous avec GitHub" -ForegroundColor Gray
Write-Host "   - Créez un nouveau projet depuis votre repository" -ForegroundColor Gray
Write-Host "   - Ajoutez les variables d'environnement" -ForegroundColor Gray
Write-Host ""
Write-Host "4. Votre site sera en ligne !" -ForegroundColor White
Write-Host ""
Write-Host "📱 Variables d'environnement pour Railway :" -ForegroundColor Cyan
Write-Host "DEBUG=False" -ForegroundColor Yellow
Write-Host "SECRET_KEY=NUrwUxyrzKzjN7BhpgQE7f9zb0PMZW2-Va2HNsrKcHFSVLVu1_e8iYKV1S1CfQKmPyw" -ForegroundColor Yellow
Write-Host "ALLOWED_HOSTS=*.railway.app,midway-cafe-production.up.railway.app" -ForegroundColor Yellow
Write-Host ""
Write-Host "🎉 Votre site Midway Café sera bientôt en ligne !" -ForegroundColor Green
Write-Host ""
Read-Host "Appuyez sur Entrée pour continuer"
