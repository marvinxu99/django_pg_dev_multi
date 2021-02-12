from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from catalog.models import BookInstance


class BorrowedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 15

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class BorrowedBooksByStaffListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to all users."""
    permission_required = ('catalog.can_mark_returned', 'catalog.can_edit')
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_staff.html'
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            bi_list = self.model.objects.filter(
                status__exact='o',
                book__title__icontains=query,
            ).order_by('due_back')
        else:
            bi_list = self.model.objects.filter(status__exact='o').order_by('due_back')
        return bi_list
