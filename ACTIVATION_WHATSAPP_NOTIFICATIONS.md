# 📱 ACTIVATION NOTIFICATIONS WHATSAPP

## ✅ SITUATION ACTUELLE

**Bonne nouvelle !** Les notifications WhatsApp sont déjà configurées dans votre projet.

### **Code déjà présent :**

#### **1. Dans `menu/views.py`**
```python
# Prépare le message WhatsApp
whatsapp_message = (
    f"Nouvelle réservation Midway Café :\n"
    f"Nom : {nom}\n"
    f"Téléphone : {telephone}\n"
    f"Date : {date}\n"
    f"Heure : {heure}\n"
    f"Nombre de personnes : {personnes}\n"
    f"Message : {message}"
)

# Envoi via Twilio
client.messages.create(
    body=whatsapp_message,
    from_=from_whatsapp,
    to=to_whatsapp
)
```

#### **2. Liens WhatsApp dans le site**
- En-tête : `https://wa.me/21628839178`
- Footer : `https://wa.me/21628839178`
- Page Contact : `https://wa.me/21628839178`

---

## 🔧 ACTIVATION COMPLÈTE

### **1. Variables d'environnement à configurer sur Render :**

Ajoutez ces variables dans votre dashboard Render :

```
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_FROM_WHATSAPP=whatsapp:+14155238886
TWILIO_TO_WHATSAPP=whatsapp:+21656012373
```

### **2. Configuration Twilio :**

#### **Étapes pour obtenir les credentials :**
1. Créez un compte sur [Twilio](https://www.twilio.com)
2. Activez WhatsApp Business API
3. Obtenez votre `Account SID` et `Auth Token`
4. Configurez le numéro WhatsApp Business

#### **Numéros par défaut :**
- **De** : `whatsapp:+14155238886` (numéro Twilio sandbox)
- **Vers** : `whatsapp:+21656012373` (votre numéro)

---

## 🚀 DÉPLOIEMENT

### **Commandes à exécuter :**

```bash
git add .
git commit -m "Add: Configuration WhatsApp notifications"
git push origin main
```

### **Configuration sur Render :**
1. Allez dans votre dashboard Render
2. Sélectionnez votre service
3. Allez dans "Environment"
4. Ajoutez les 4 variables Twilio
5. Redéployez votre service

---

## 🎯 FONCTIONNALITÉS

### **Notifications automatiques :**
- ✅ Nouvelle réservation → Message WhatsApp
- ✅ Informations complètes du client
- ✅ Date, heure, nombre de personnes
- ✅ Message personnalisé du client

### **Liens WhatsApp directs :**
- ✅ En-tête du site
- ✅ Footer du site
- ✅ Page de contact
- ✅ Numéro : +216 28 839 178

---

## 🔍 TEST

### **Pour tester les notifications :**
1. Allez sur la page de réservation
2. Remplissez le formulaire
3. Soumettez la réservation
4. Vérifiez que le message WhatsApp arrive

### **Pour tester les liens :**
1. Cliquez sur le numéro de téléphone
2. WhatsApp doit s'ouvrir avec le numéro pré-rempli

---

## 🎉 NOTIFICATIONS WHATSAPP ACTIVÉES !

Vos notifications WhatsApp sont prêtes ! Il suffit de configurer les variables Twilio sur Render. 🚀📱
