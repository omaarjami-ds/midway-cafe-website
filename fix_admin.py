from django.contrib.auth import get_user_model

User = get_user_model()
try:
    user = User.objects.get(username='admin')
    user.set_password('password')
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print("Password and staff status for 'admin' have been set successfully.")
except User.DoesNotExist:
    User.objects.create_superuser('admin', 'admin@example.com', 'password')
    print("Superuser 'admin' created successfully.")
