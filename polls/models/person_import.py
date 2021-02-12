'''
https://django-postgres-copy.readthedocs.io/en/latest/

This model is created to demo CSV import and export

CSV file:
name,number,date
ben,1,2012-01-01
joe,2,2012-01-02
jane,3,2012-01-03

> python manage.py csv_import
> python manage.py vcs_export

'''

from django.db import models
from postgres_copy import CopyManager


class PersonImport(models.Model):
    name = models.CharField(max_length=500)
    number = models.IntegerField(null=True)
    date = models.DateField(null=True)
    objects = CopyManager()

    class meta:
        db_table = "polls_person_import"
