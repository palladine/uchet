from django.core.management.base import BaseCommand, CommandError
from app.models import User, Unit, Monitor, Printer, Scanner, IBP, Scale, Phone, Router, ARM
from barcode import generate

class Command(BaseCommand):
    def handle(self, *args, **options):
        # 'code39', 'code128', 'ean', 'ean13', 'ean8', 'gs1', 'gtin', 'isbn', 'isbn10', 'isbn13', 'issn', 'jan', 'pzn', 'upc', 'upca'
        name = generate('ean13', '5901234123457', output='barcode_svg')
        print(name)