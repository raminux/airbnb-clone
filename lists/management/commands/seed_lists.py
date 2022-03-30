import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as user_models
from lists import models as list_models
from rooms import models as room_models

NAME = "lists"


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
            list_models.List,
            number,
            {
                "user": lambda list: random.choice(users),
            },
        )
        lists = seeder.execute()
        pks = flatten(list(lists.values()))
        print(f"pks: {pks}")
        len_pks = len(pks)
        for pk in pks:
            list_object = list_models.List.objects.get(pk=pk)
            i = random.randint(0, len_pks)
            j = random.randint(0, len_pks)
            print(f"i: {i}, j: {j}")
            selected_rooms = rooms[min(i, j) : max(i, j)]
            list_object.rooms.add(*selected_rooms)

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
