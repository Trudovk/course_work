from django.core.management.base import BaseCommand
from ...models import Item

class Command(BaseCommand):
    help = 'Counts the number of Item objects'

    def handle(self, *args, **options):
        count = Item.objects.count()
        self.stdout.write(f'There are {count} Item objects in the database.')