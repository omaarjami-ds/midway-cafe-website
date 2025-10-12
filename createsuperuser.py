from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'omaarjami@gmail.com', 'admin123')
    print("Superutilisateur créé avec succès!")
    print("Nom d'utilisateur: admin")
    print("Email: omaarjami@gmail.com")
    print("Mot de passe: admin123")
    print("\nVous pouvez maintenant accéder à l'admin à l'adresse:")
    print("http://localhost:8000/admin/")
else:
    print("Le superutilisateur 'admin' existe déjà.")
