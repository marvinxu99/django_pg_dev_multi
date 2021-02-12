# Start the id from 10000

# method 1: TESTED and WORKED
# (1) python manage.py makemigrations APPNAME --empty

# (2) Inside the created migration file, add the following:
#
# operations = [
#     migrations.RunSQL('ALTER SEQUENCE APPNAME_USER_id_seq RESTART WITH 10000;')
# ]


# method 2: NOT TESTED
# from django.db.models import .signals
# from django.db import connection, transaction

# cursor = connection.cursor()
# cursor = cursor.execute(""" ALTER SEQUENCE user_id RESTART WITH 10000; """)
# transaction.commit_unless_managed()

# signals.post_syncdb.connect(auto_increment_start, sender=app_models)
