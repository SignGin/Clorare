from django.core.management.base import BaseCommand
from django_seed import Seed
from clothes.models import Clothes


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=1,
            type=int,
            help="how many clothes data?"
        )

    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()

        try:
            seeder.add_entity(
                Clothes,
                total,
                {}
            )
            seeder.execute()
            print(f"Successfully added {total} clothes data!!")
        except:
            print("Failed to add clothes data")
