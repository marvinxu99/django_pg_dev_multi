'''
python manage.py csv_import

'''

from django.core.management.base import BaseCommand

from polls.models import PersonImport


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path (or a Python file object)
        insert_count = PersonImport.objects.from_csv('person_import.csv')
        print ("{} records inserted".format(insert_count))
