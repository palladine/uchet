from django.core.management.base import BaseCommand, CommandError
from app.models import User, Unit, Monitor, Printer, Scanner, IBP, Scale, Phone, Router, ARM
from barcode import generate

class Command(BaseCommand):
    def handle(self, *args, **options):
        ...

