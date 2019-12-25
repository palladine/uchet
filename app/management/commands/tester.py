from django.core.management.base import BaseCommand, CommandError
from app.models import User, Unit, Monitor, Printer, Scanner, IBP, Scale, Phone, Router, ARM
import barcode
import io

class Command(BaseCommand):
    def handle(self, *args, **options):
        cd = barcode.get_barcode_class('code128')
        print(cd)

        cdx = cd('1120000004')

        fp = io.BytesIO()
        cdx.write(fp)

        print(fp.getvalue().decode())
