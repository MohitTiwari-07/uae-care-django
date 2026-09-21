import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create admin user from environment variables"

    def handle(self, *args, **options):

        User = get_user_model()

        username = os.getenv("DJANGO_ADMIN_USERNAME")
        email = os.getenv("DJANGO_ADMIN_EMAIL")
        password = os.getenv("DJANGO_ADMIN_PASSWORD")

        if not username or not email or not password:
            self.stdout.write(
                self.style.WARNING(
                    "Admin environment variables are not configured."
                )
            )
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.SUCCESS("Admin user already exists.")
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )

        self.stdout.write(
            self.style.SUCCESS("Admin user created successfully.")
        )