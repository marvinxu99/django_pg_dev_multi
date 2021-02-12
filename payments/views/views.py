from django.shortcuts import render
from django.views.generic.base import TemplateView


class DemoView(TemplateView):
    template_name = 'payments/demo.html'

class SuccessView(TemplateView):
    template_name = 'payments/success.html'


class CancelledView(TemplateView):
    template_name = 'payments/cancelled.html'
