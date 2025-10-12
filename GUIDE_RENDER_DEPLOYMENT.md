# 🚀 GUIDE DE DÉPLOIEMENT RENDER - MIDWAY CAFÉ

## ✅ CONFIGURATION PRÊTE POUR RENDER

Votre projet est maintenant configuré pour être déployé sur Render.com !

---

## 📋 ÉTAPES DE DÉPLOIEMENT

### **1️⃣ Créer un compte Render**
- Allez sur [render.com](https://render.com)
- Cliquez "Get Started for Free"
- Connectez-vous avec votre compte GitHub

### **2️⃣ Créer un nouveau service Web**
1. Cliquez "New +" dans le dashboard
2. Sélectionnez "Web Service"
3. Connectez votre repository GitHub : `omaarjami-ds/midway-cafe-website`
4. Configurez le service :
   - **Name** : `midway-cafe`
   - **Environment** : `Python 3`
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `gunicorn midway_project.wsgi:application`

### **3️⃣ Variables d'environnement**
Dans la section "Environment Variables", ajoutez :

```
DEBUG=False
SECRET_KEY=NUrwUxyrzKzjN7BhpgQE7f9zb0PMZW2-Va2HNsrKcHFSVLVu1_e8iYKV1S1CfQKmPyw
ALLOWED_HOSTS=midway-cafe.onrender.com,*.onrender.com
```

### **4️⃣ Déployer**
1. Cliquez "Create Web Service"
2. Render va automatiquement :
   - Cloner votre code
   - Installer les dépendances
   - Démarrer votre application
3. Attendez 3-5 minutes pour le déploiement

---

## 🔧 CONFIGURATION TECHNIQUE

### **Fichiers configurés :**
- ✅ `Procfile` : Commande de démarrage Gunicorn
- ✅ `runtime.txt` : Version Python 3.11.9
- ✅ `requirements.txt` : Toutes les dépendances
- ✅ `settings.py` : Configuration pour production

### **Fonctionnalités incluses :**
- ✅ Gestion des fichiers statiques avec WhiteNoise
- ✅ Configuration de base de données PostgreSQL
- ✅ Variables d'environnement sécurisées
- ✅ Configuration HTTPS automatique

---

## 🌐 RÉSULTAT FINAL

Après le déploiement, votre site sera accessible sur :
**https://midway-cafe.onrender.com**

### **Fonctionnalités disponibles :**
- ✅ Page d'accueil avec carousel
- ✅ Menu interactif avec filtres
- ✅ Galerie d'images
- ✅ Formulaire de réservation
- ✅ Page de contact
- ✅ Design responsive (mobile, tablette, PC)
- ✅ HTTPS sécurisé

---

## 🆘 DÉPANNAGE

### **Si le déploiement échoue :**
1. Vérifiez les logs dans Render Dashboard
2. Assurez-vous que toutes les variables d'environnement sont définies
3. Vérifiez que le repository GitHub est public

### **Si le site ne fonctionne pas :**
1. Vérifiez que `DEBUG=False` en production
2. Assurez-vous que `ALLOWED_HOSTS` contient votre domaine Render
3. Vérifiez les logs d'erreur dans Render

---

## 🎉 FÉLICITATIONS !

Votre site Midway Café sera bientôt en ligne et accessible partout dans le monde ! 🌍☕

**Prochaines étapes recommandées :**
1. Tester le site déployé
2. Configurer un nom de domaine personnalisé
3. Ajouter Google Analytics
4. Optimiser le SEO

---

## 📞 SUPPORT

Si vous rencontrez des problèmes, vérifiez :
- Les logs dans Render Dashboard
- La configuration des variables d'environnement
- La connectivité GitHub

**Votre site sera prêt en quelques minutes ! 🚀**
