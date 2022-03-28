from django.core.management.base import BaseCommand
from rooms import models as rooms_models


class Command(BaseCommand):

    help = "This command creates facilities"

    def handle(self, *args, **kwargs):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            rooms_models.Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))
