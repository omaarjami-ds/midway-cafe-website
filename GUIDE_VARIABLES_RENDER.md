# 📱 COMMENT AJOUTER LES VARIABLES D'ENVIRONNEMENT SUR RENDER

## 🎯 LOCALISATION DES VARIABLES D'ENVIRONNEMENT

### **Étapes détaillées :**

#### **1. Connectez-vous à Render**
- Allez sur [render.com](https://render.com)
- Connectez-vous avec votre compte

#### **2. Accédez à votre service**
- Cliquez sur votre service "midway-cafe-website" dans le dashboard
- Vous verrez la page de votre service

#### **3. Trouvez la section "Environment"**
- Dans le menu de gauche, cliquez sur **"Environment"**
- Ou cherchez l'onglet **"Environment"** en haut de la page

#### **4. Ajoutez les variables**
Vous verrez une section avec des champs :
- **Key** (nom de la variable)
- **Value** (valeur de la variable)

---

## 🔧 VARIABLES À AJOUTER

### **Ajoutez ces 4 variables une par une :**

#### **Variable 1 :**
- **Key :** `TWILIO_ACCOUNT_SID`
- **Value :** `your-twilio-account-sid` (remplacez par votre vrai SID)

#### **Variable 2 :**
- **Key :** `TWILIO_AUTH_TOKEN`
- **Value :** `your-twilio-auth-token` (remplacez par votre vrai token)

#### **Variable 3 :**
- **Key :** `TWILIO_FROM_WHATSAPP`
- **Value :** `whatsapp:+14155238886`

#### **Variable 4 :**
- **Key :** `TWILIO_TO_WHATSAPP`
- **Value :** `whatsapp:+21656012373`

---

## 📸 VISUALISATION

### **Ce que vous verrez sur Render :**

```
Environment Variables
┌─────────────────────────┬─────────────────────────────────────┐
│ Key                     │ Value                               │
├─────────────────────────┼─────────────────────────────────────┤
│ DEBUG                   │ False                               │
│ SECRET_KEY              │ NUrwUxyrzKzjN7BhpgQE7f9zb0PMZW2... │
│ ALLOWED_HOSTS           │ midway-cafe-website.onrender.com    │
│ TWILIO_ACCOUNT_SID      │ [À AJOUTER]                        │
│ TWILIO_AUTH_TOKEN       │ [À AJOUTER]                        │
│ TWILIO_FROM_WHATSAPP    │ [À AJOUTER]                        │
│ TWILIO_TO_WHATSAPP      │ [À AJOUTER]                        │
└─────────────────────────┴─────────────────────────────────────┘
```

---

## 🚀 ÉTAPES PRÉCISES

### **1. Cliquez sur "Add Environment Variable"**
- Bouton bleu ou vert sur la page Environment

### **2. Remplissez chaque variable**
- Tapez le nom dans "Key"
- Tapez la valeur dans "Value"
- Cliquez sur "Save" ou "Add"

### **3. Répétez pour les 4 variables**
- Faites cela 4 fois (une fois par variable)

### **4. Redéployez votre service**
- Cliquez sur "Manual Deploy" ou attendez le déploiement automatique

---

## 🔍 VÉRIFICATION

### **Après avoir ajouté les variables :**
1. Vérifiez qu'elles apparaissent dans la liste
2. Redéployez votre service
3. Testez une réservation
4. Vérifiez que le message WhatsApp arrive

---

## 🎉 RÉSULTAT

Une fois les variables ajoutées, vos notifications WhatsApp seront automatiquement activées ! 🚀📱
