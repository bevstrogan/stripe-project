from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class CreateSuperUserCommand(BaseCommand): #кастомная комманда для создания админа
    def handle(self, *args, **options):
        User = get_user_model()
        username = 'admin'
        email = 'admin@example.com'
        password = 'qwerty123123'

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING('Пользователь уже существует.'))
        else:
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS('Пользователь создан'))