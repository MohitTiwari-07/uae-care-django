from django.core.management.base import BaseCommand
from django.core.management import call_command
from core.models import Service


class Command(BaseCommand):
    help = "Import initial core data"

    def handle(self, *args, **options):

        # Data already exists, so don't import again
        if Service.objects.exists():
            self.stdout.write(
                self.style.WARNING("Core data already exists. Skipping import.")
            )
            return

        call_command("loaddata", "core_data.json")

        self.stdout.write(
            self.style.SUCCESS("Core data imported successfully.")
        )