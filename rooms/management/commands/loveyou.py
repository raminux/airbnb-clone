from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand, CommandError):
    def add_arguments(self, parser):
        parser.add_argument("--times", help="How many times do I love you?")

    def handle(self, *args, **options):
        times = options.get("times")
        for _ in range(int(times)):
            self.stdout.write(self.style.SUCCESS("I Love You!"))
            self.stdout.write(self.style.WARNING("I Love You"))
            self.stdout.write(self.style.ERROR("I Love You"))
