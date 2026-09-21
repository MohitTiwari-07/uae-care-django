from django.core.management.base import BaseCommand
from django.core.management import call_command
from core.models import Service


class Command(BaseCommand):
    help = "Import initial core data"

    def handle(self, *args, **options):

        self.stdout.write("IMPORT COMMAND STARTED")

        self.stdout.write(
            f"Services currently in database: {Service.objects.count()}"
        )

        if Service.objects.exists():
            self.stdout.write(
                self.style.WARNING("Core data already exists. Skipping import.")
            )
            return

        self.stdout.write("Loading core_data.json...")

        call_command("loaddata", "core_data.json", verbosity=2)

        self.stdout.write(
            self.style.SUCCESS("Core data imported successfully.")
        )