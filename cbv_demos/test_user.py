from django.contrib.auth import models as auth_models, get_user_model

UserModel = get_user_model()
UserModel.objects.create_user(
    username='doncho',
    password='asdqwe123',
)
