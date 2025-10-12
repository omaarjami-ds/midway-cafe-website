# 🎯 Guide Visuel de Déploiement - Midway Café

## 📱 **ÉTAPE 1 : Créer un compte GitHub**

### 🔗 **Allez sur GitHub.com**
1. Ouvrez votre navigateur
2. Allez sur [https://github.com](https://github.com)
3. Cliquez sur **"Sign up"** (S'inscrire)

### 📝 **Créez votre compte**
- **Username** : Choisissez un nom d'utilisateur (ex: `omaar-jami`)
- **Email** : Votre adresse email
- **Password** : Un mot de passe sécurisé
- Cliquez **"Create account"**

### 🆕 **Créez un nouveau repository**
1. Cliquez sur le bouton **"New"** (vert) ou **"+"** en haut à droite
2. **Repository name** : `midway-cafe-website`
3. **Description** : `Site web responsive du Midway Café`
4. Cochez **"Public"**
5. **NE COCHEZ PAS** "Add a README file"
6. Cliquez **"Create repository"**

---

## 🚀 **ÉTAPE 2 : Connecter votre projet à GitHub**

### 📋 **Copiez l'URL de votre repository**
Après avoir créé le repository, GitHub vous montrera une page avec des instructions. Copiez l'URL qui ressemble à :
```
https://github.com/VOTRE_USERNAME/midway-cafe-website.git
```

### 💻 **Dans votre terminal (PowerShell)**
Ouvrez PowerShell dans le dossier `midway_cafe` et exécutez :

```powershell
# Remplacez VOTRE_USERNAME par votre nom d'utilisateur GitHub
git remote add origin https://github.com/VOTRE_USERNAME/midway-cafe-website.git
git branch -M main
git push -u origin main
```

**Exemple concret :**
```powershell
git remote add origin https://github.com/omaar-jami/midway-cafe-website.git
git branch -M main
git push -u origin main
```

---

## 🌐 **ÉTAPE 3 : Déployer sur Railway**

### 🔗 **Allez sur Railway.app**
1. Ouvrez [https://railway.app](https://railway.app)
2. Cliquez sur **"Login"**
3. Sélectionnez **"Login with GitHub"**
4. Autorisez Railway à accéder à votre compte GitHub

### 🆕 **Créez un nouveau projet**
1. Cliquez sur **"New Project"**
2. Sélectionnez **"Deploy from GitHub repo"**
3. Choisissez votre repository **"midway-cafe-website"**
4. Railway va automatiquement détecter que c'est un projet Django

### ⚙️ **Configurez les variables d'environnement**
1. Dans votre projet Railway, cliquez sur **"Variables"**
2. Ajoutez ces 3 variables une par une :

**Variable 1 :**
- **Name** : `DEBUG`
- **Value** : `False`

**Variable 2 :**
- **Name** : `SECRET_KEY`
- **Value** : `NUrwUxyrzKzjN7BhpgQE7f9zb0PMZW2-Va2HNsrKcHFSVLVu1_e8iYKV1S1CfQKmPyw`

**Variable 3 :**
- **Name** : `ALLOWED_HOSTS`
- **Value** : `*.railway.app,midway-cafe-production.up.railway.app`

### 🚀 **Déployez !**
1. Cliquez sur **"Deploy"**
2. Attendez 2-3 minutes
3. Railway va construire et déployer votre site

---

## 🎉 **ÉTAPE 4 : Votre site est en ligne !**

### 🌍 **Accédez à votre site**
Railway vous donnera une URL comme :
```
https://midway-cafe-production.up.railway.app
```

### ✅ **Testez votre site**
1. Ouvrez l'URL dans votre navigateur
2. Testez sur votre téléphone
3. Vérifiez que tout fonctionne :
   - ✅ Navigation
   - ✅ Images
   - ✅ Responsive design
   - ✅ Formulaire de réservation

---

## 🆘 **En cas de problème**

### ❌ **Erreur lors du push vers GitHub**
```powershell
# Vérifiez que vous êtes dans le bon dossier
cd C:\Users\omaar\midway_cafe

# Vérifiez le statut git
git status

# Ajoutez tous les fichiers
git add .

# Commitez
git commit -m "Deploy to production"

# Poussez vers GitHub
git push -u origin main
```

### ❌ **Erreur sur Railway**
1. Vérifiez que toutes les variables d'environnement sont correctes
2. Regardez les logs de déploiement dans Railway
3. Assurez-vous que votre repository GitHub est public

### ❌ **Site ne s'affiche pas**
1. Attendez 5-10 minutes (premier déploiement peut être lent)
2. Vérifiez l'URL dans Railway
3. Testez sur un autre navigateur

---

## 🎯 **Résultat Final**

Votre site **Midway Café** sera :
- ✅ **En ligne** et accessible partout
- ✅ **Responsive** sur tous les appareils
- ✅ **Sécurisé** avec HTTPS
- ✅ **Gratuit** avec Railway
- ✅ **Professionnel** et rapide

## 📞 **Besoin d'aide ?**

Si vous avez des questions ou des problèmes :
1. Relisez ce guide étape par étape
2. Vérifiez que vous suivez exactement les instructions
3. Contactez-moi si vous êtes bloqué !

**Votre site Midway Café sera bientôt en ligne ! 🎉☕🌍**
