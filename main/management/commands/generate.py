import random
from django.core.management.base import BaseCommand, CommandError
from main.models import Cafe
from faker import Faker


class Command(BaseCommand):
    help = 'Create fake cafe'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Кількість закладів для додавання')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            fake = Faker()
            try:
                adr = fake.address()
                ttl = fake.sentences(1)[0]
                txt = ' '.join(fake.sentences(3))
                pub = fake.year()
                pri = random.radiant(50, 200)
                Cafe.objects.create(
                    title=ttl,
                    address=adr,
                    text=txt,
                    price=pri,
                    published=pub,
                )
                print(f'Added {ttl}')
            except:
                raise CommandError('Error of creating')
            else:
                print(f'{i+1} закладів додалось')
