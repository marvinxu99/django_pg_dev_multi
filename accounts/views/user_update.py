from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'accounts/my_account.html'
    #success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        # return self.request.META.get('HTTP_REFERER')
        return reverse_lazy('home')
