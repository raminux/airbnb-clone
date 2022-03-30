import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from reviews import models as review_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates many reviews."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many reviews do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "accuracy": lambda review: random.randint(0, 5),
                "communication": lambda review: random.randint(0, 5),
                "clealiness": lambda review: random.randint(0, 5),
                "location": lambda review: random.randint(0, 5),
                "check_in": lambda review: random.randint(0, 5),
                "value": lambda review: random.randint(0, 5),
                "user": lambda review: random.choice(users),
                "room": lambda review: random.choice(rooms),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
