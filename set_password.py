from django.contrib.auth import get_user_model

User = get_user_model()
try:
    user = User.objects.get(username='admin')
    user.set_password('password')
    user.save()
    print("Password for 'admin' has been set successfully.")
except User.DoesNotExist:
    print("User 'admin' does not exist.")
