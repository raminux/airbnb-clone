import random
from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from django_seed import Seed
from users import models as user_models
from reservations import models as reservation_models
from rooms import models as room_models

NAME = "reservations"


class Command(BaseCommand):

    help = f"This command creates many {NAME}."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help=f"How many {NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "status": lambda _: random.choice(
                    [
                        reservation_models.Reservation.STATUS_CANCELED,
                        reservation_models.Reservation.STATUS_CONFIRMED,
                        reservation_models.Reservation.STATUS_PENDING,
                    ]
                ),
                "guest": lambda _: random.choice(users),
                "room": lambda _: random.choice(rooms),
                "check_in": lambda _: datetime.now(),
                "check_out": lambda _: datetime.now()
                + timedelta(days=random.randint(3, 20)),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
