'''
python manage.py csv_export

'''

from polls.models import PersonImport
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # All this method needs is the path to your CSV.
        # (If you don't provide one, the method will return the CSV as a string.)
        PersonImport.objects.to_csv('psn_export.csv')