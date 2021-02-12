'''
Writing custom django-admin commands
https://docs.djangoproject.com/en/1.11/howto/custom-management-commands/
The closepoll.py module has only one requirement – it must define a class
Command that extends BaseCommand or one of its subclasses.

> python manage.py <poll_id> --delete
'''
from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll

class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('poll_id', nargs='+', type=int)

        # Named (optional) arguments
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        for poll_id in options['poll_id']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            print("before...")
            print(options['delete'])
            if options['delete']:
                print("delete")
                poll.delete()
                poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully deleted poll "%s"' % poll_id))
