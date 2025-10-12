#!/usr/bin/env python3
"""
Script de déploiement pour Render.com
Ce script prépare le projet pour le déploiement sur Render
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Exécute une commande et affiche le résultat."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Succès!")
            if result.stdout.strip():
                print(f"   Output: {result.stdout.strip()}")
        else:
            print(f"❌ {description} - Erreur!")
            print(f"   Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ {description} - Exception: {str(e)}")
        return False
    return True

def main():
    print("🚀 PRÉPARATION DU DÉPLOIEMENT RENDER")
    print("=" * 50)
    
    # Vérifier que nous sommes dans le bon répertoire
    if not os.path.exists('manage.py'):
        print("❌ Erreur: manage.py non trouvé. Assurez-vous d'être dans le répertoire du projet.")
        return False
    
    # Vérifier que l'environnement virtuel est activé
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Attention: L'environnement virtuel ne semble pas être activé.")
        print("   Activez-le avec: venv\\Scripts\\activate")
    
    # Étapes de préparation
    steps = [
        ("python manage.py check", "Vérification de la configuration Django"),
        ("python manage.py makemigrations", "Création des migrations"),
        ("python manage.py migrate", "Application des migrations"),
        ("python manage.py collectstatic --noinput", "Collecte des fichiers statiques"),
    ]
    
    success = True
    for command, description in steps:
        if not run_command(command, description):
            success = False
            break
    
    if success:
        print("\n🎉 PRÉPARATION TERMINÉE AVEC SUCCÈS!")
        print("=" * 50)
        print("✅ Votre projet est prêt pour le déploiement sur Render!")
        print("\n📋 PROCHAINES ÉTAPES:")
        print("1. Poussez votre code sur GitHub")
        print("2. Créez un compte sur render.com")
        print("3. Connectez votre repository GitHub")
        print("4. Configurez les variables d'environnement")
        print("5. Déployez!")
        print("\n📖 Consultez GUIDE_RENDER_DEPLOYMENT.md pour les détails")
    else:
        print("\n❌ PRÉPARATION ÉCHOUÉE!")
        print("Vérifiez les erreurs ci-dessus avant de continuer.")
    
    return success

if __name__ == "__main__":
    main()
