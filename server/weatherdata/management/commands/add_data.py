from django_seed import Seed
from weatherdata.models import Clothes
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="how many data?"
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()

        data_arr = [
            [0, 'knitwear', 'gray', 0, 2, '/clothes/cat.jpg'],
            [0, 'knitwear', 'black', 0, 2, '/clothes/cat.jpg'],

            [0, 'long-sleeved T-shirt', 'blue', 1, 2, '/clothes/cat.jpg'],

            [0, 'short-sleeved T-shirt', 'red', 2, 2, '/clothes/cat.jpg'],
            [0, 'short-sleeved T-shirt', 'white', 2, 2, '/clothes/cat.jpg'],
            [0, 'blouse', 'red', 2, 2, '/clothes/cat.jpg'],

            [0, 'check shirt', 'black', 3, 2, '/clothes/cat.jpg'],
            [0, 'stripe shirt', 'navy', 3, 2, '/clothes/cat.jpg'],
            [0, 'a sleeveless shirt', 'white', 3, 2, '/clothes/cat.jpg'],

            [1, 'jeans', 'blue', 0, 2, '/clothes/paper.jpg'],
            [1, 'jeans', 'navy', 0, 2, '/clothes/paper.jpg'],

            [1, 'jeans', 'blue', 1, 2, '/clothes/paper.jpg'],
            [1, 'jeans', 'navy', 1, 2, '/clothes/paper.jpg'],
            [1, 'pants', 'white', 1, 2, '/clothes/paper.jpg'],
            [1, 'pants', 'yellow', 1, 2, '/clothes/paper.jpg'],
            [1, 'slacks', 'black', 1, 2, '/clothes/paper.jpg'],

            [1, 'pants', 'white', 2, 2, '/clothes/paper.jpg'],
            [1, 'pants', 'yellow', 2, 2, '/clothes/paper.jpg'],
            [1, 'shorts', 'black', 2, 2, '/clothes/paper.jpg'],
            [1, 'slacks', 'black', 2, 2, '/clothes/paper.jpg'],

            [1, 'dolphin shorts', 'navy', 3, 0, '/clothes/paper.jpg'],
            [1, 'shorts', 'black', 3, 2, '/clothes/paper.jpg'],
            [1, 'skirt', 'red', 3, 0, '/clothes/paper.jpg'],
            [1, 'skirt', 'pink', 3, 0, '/clothes/paper.jpg'],

            [2, 'coat', 'black', 0, 2, '/clothes/paper.jpg'],
            [2, 'padded coat', 'black', 0, 2, '/clothes/paper.jpg'],

            [2, 'jumper', 'black', 1, 2, '/clothes/paper.jpg'],
            [2, 'jacket', 'black', 1, 2, '/clothes/paper.jpg'],

            [2, 'waistcoat', 'black', 2, 2, '/clothes/paper.jpg'],
            [2, 'cardigan', 'black', 2, 2, '/clothes/paper.jpg'],

            [2, 'none', 'none', 3, 2, '/clothes/paper.jpg'],
        ]

        for i in range(len(data_arr)):
            seeder.add_entity(Clothes, number, {
                'category': data_arr[i][0],
                'cloth_type': data_arr[i][1],
                'color': data_arr[i][2],
                'temp': data_arr[i][3],
                'sex': data_arr[i][4],
                'image': data_arr[i][5],
            })

        seeder.execute()
        print(f"Add {len(data_arr)} clothes data!!")
