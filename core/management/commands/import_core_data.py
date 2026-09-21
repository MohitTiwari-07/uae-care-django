import json
from pathlib import Path

from django.core.management.base import BaseCommand
from django.core.serializers import deserialize
from core.models import Service


class Command(BaseCommand):
    help = "Import initial core data"

    def handle(self, *args, **options):

        self.stdout.write("IMPORT COMMAND STARTED")

        service_count = Service.objects.count()
        self.stdout.write(
            f"Services currently in database: {service_count}"
        )

        if Service.objects.exists():
            self.stdout.write(
                self.style.WARNING(
                    "Core data already exists. Skipping import."
                )
            )
            return

        fixture_path = Path("core_data.json")

        self.stdout.write(
            f"Reading fixture: {fixture_path.resolve()}"
        )

        with open(fixture_path, "r", encoding="utf-8-sig") as file:
            data = json.load(file)

        self.stdout.write(
            f"Found {len(data)} objects in fixture."
        )

        for obj in deserialize("json", json.dumps(data)):
            obj.save()

        self.stdout.write(
            self.style.SUCCESS(
                "Core data imported successfully."
            )
        )