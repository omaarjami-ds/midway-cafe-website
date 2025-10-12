# 🚀 Guide de Déploiement - Midway Café

## 📋 Prérequis
- ✅ Compte GitHub
- ✅ Compte Railway (gratuit)
- ✅ Projet préparé (✅ Fait)

## 🎯 Option 1 : Railway (GRATUIT - Recommandé)

### **Étape 1 : Créer un repository GitHub**

1. **Allez sur [github.com](https://github.com)**
2. **Cliquez sur "New repository"**
3. **Nom du repository** : `midway-cafe-website`
4. **Description** : `Site web responsive du Midway Café`
5. **Cochez "Public"**
6. **Cliquez "Create repository"**

### **Étape 2 : Connecter votre projet local à GitHub**

```bash
# Dans votre terminal (dans le dossier midway_cafe)
git remote add origin https://github.com/VOTRE_USERNAME/midway-cafe-website.git
git branch -M main
git push -u origin main
```

### **Étape 3 : Déployer sur Railway**

1. **Allez sur [railway.app](https://railway.app)**
2. **Cliquez "Login" et connectez-vous avec GitHub**
3. **Cliquez "New Project"**
4. **Sélectionnez "Deploy from GitHub repo"**
5. **Choisissez votre repository `midway-cafe-website`**
6. **Railway va automatiquement détecter que c'est un projet Django**

### **Étape 4 : Configurer les variables d'environnement**

Dans Railway, allez dans **Variables** et ajoutez :

```
DEBUG=False
SECRET_KEY=une-clé-secrète-très-longue-et-complexe
ALLOWED_HOSTS=*.railway.app,midway-cafe-production.up.railway.app
```

### **Étape 5 : Déployer**

1. **Railway va automatiquement déployer votre site**
2. **Attendez 2-3 minutes**
3. **Votre site sera disponible sur une URL comme : `https://midway-cafe-production.up.railway.app`**

---

## 🎯 Option 2 : Render (GRATUIT - Alternative)

### **Étape 1 : Créer un compte Render**

1. **Allez sur [render.com](https://render.com)**
2. **Créez un compte avec GitHub**

### **Étape 2 : Créer un nouveau service**

1. **Cliquez "New +"**
2. **Sélectionnez "Web Service"**
3. **Connectez votre repository GitHub**
4. **Configurez :**
   - **Name** : `midway-cafe`
   - **Environment** : `Python 3`
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `gunicorn midway_project.wsgi:application`

### **Étape 3 : Variables d'environnement**

```
DEBUG=False
SECRET_KEY=une-clé-secrète-très-longue-et-complexe
ALLOWED_HOSTS=midway-cafe.onrender.com
```

---

## 🎯 Option 3 : PythonAnywhere (GRATUIT - Spécialisé Python)

### **Étape 1 : Créer un compte**

1. **Allez sur [pythonanywhere.com](https://pythonanywhere.com)**
2. **Créez un compte gratuit**

### **Étape 2 : Uploader votre code**

1. **Allez dans "Files"**
2. **Uploadez votre projet**
3. **Ou clonez depuis GitHub**

### **Étape 3 : Configurer l'application web**

1. **Allez dans "Web"**
2. **Cliquez "Add a new web app"**
3. **Choisissez "Django"**
4. **Sélectionnez votre version Python**
5. **Configurez le chemin vers votre projet**

---

## 🔧 Configuration Post-Déploiement

### **1. Migrations de base de données**

```bash
python manage.py migrate
```

### **2. Créer un superutilisateur**

```bash
python manage.py createsuperuser
```

### **3. Collecter les fichiers statiques**

```bash
python manage.py collectstatic
```

---

## 🌐 Nom de Domaine Personnalisé

### **Acheter un nom de domaine**

1. **Allez sur [Namecheap](https://namecheap.com) ou [GoDaddy](https://godaddy.com)**
2. **Recherchez un nom comme :**
   - `midwaycafe.tn`
   - `cafemidway.com`
   - `midway-cafe.tn`

### **Configurer le DNS**

1. **Dans votre panneau de contrôle du domaine**
2. **Ajoutez un enregistrement CNAME :**
   - **Name** : `www`
   - **Value** : `votre-site.railway.app`

---

## 📱 Test Final

### **Vérifications importantes :**

- ✅ Site accessible sur mobile
- ✅ Navigation fonctionne
- ✅ Images s'affichent
- ✅ Formulaire de réservation fonctionne
- ✅ Vitesse de chargement acceptable

### **Outils de test :**

- **Google PageSpeed Insights** : [pagespeed.web.dev](https://pagespeed.web.dev)
- **Mobile-Friendly Test** : [search.google.com/test/mobile-friendly](https://search.google.com/test/mobile-friendly)

---

## 🆘 Support et Aide

### **Problèmes courants :**

1. **Erreur 500** : Vérifiez les variables d'environnement
2. **Images ne s'affichent pas** : Vérifiez la configuration des fichiers statiques
3. **Site lent** : Optimisez les images et utilisez un CDN

### **Ressources utiles :**

- **Documentation Railway** : [docs.railway.app](https://docs.railway.app)
- **Documentation Django** : [docs.djangoproject.com](https://docs.djangoproject.com)
- **Support** : Contactez-moi si vous avez des questions !

---

## 🎉 Félicitations !

Votre site Midway Café sera bientôt en ligne et accessible partout dans le monde ! 🌍☕

**Prochaines étapes recommandées :**
1. Déployer le site
2. Tester sur différents appareils
3. Acheter un nom de domaine
4. Optimiser le SEO
5. Ajouter Google Analytics
