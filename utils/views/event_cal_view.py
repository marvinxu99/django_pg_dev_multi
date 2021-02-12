import calendar
from django.shortcuts import render
from datetime import datetime, timedelta, date
from calendar import HTMLCalendar
from django.views.generic import ListView
from django.urls import reverse_lazy, reverse
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from utils.models import Event
from utils.forms import EventForm


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, firstday=calendar.SUNDAY):
        self.year = year
        self.month = month
        super(Calendar, self).__init__(firstday)   # set the first day of the week

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)

        d = ''
        for event in events_per_day:
            d += f'<li> {event.get_html_url} </li>'

        if day != 0:
            csscls = ''
            if date.today() == date(self.year, self.month, day):
                csscls = 'today'
            return f"<td class='{csscls}'><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal


class CalendarView(ListView):
    model = Event
    template_name = 'utils/event_calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        # d = get_date(self.request.GET.get('day', None))
        d = self.get_date(self.request.GET.get('month', None))
        context['prev_month'] = self.prev_month(d)
        context['next_month'] = self.next_month(d)

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)

        return context

    def get_date(self, req_day):
        if req_day:
            year, month = (int(x) for x in req_day.split('-'))
            return date(year, month, day=1)
        return datetime.today()

    def prev_month(self, d):
        first = d.replace(day=1)
        prev_month = first - timedelta(days=1)
        month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
        return month

    def next_month(self, d):
        days_in_month = calendar.monthrange(d.year, d.month)[1]
        last = d.replace(day=days_in_month)
        next_month = last + timedelta(days=1)
        month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
        return month

@login_required
def event(request, event_id=None):
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
        template_tile = 'Edit Event'
    else:
        instance = Event()
        instance.start_time = datetime.now()
        instance.end_time = datetime.now()
        template_tile = 'New Event'

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('utils:calendar'))

    return render(request, 'utils/cal_event.html', {'form': form, 'template_tile': template_tile})
