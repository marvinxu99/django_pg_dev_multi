from django.urls import path
from . import views


app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.author_detail_view, name='author-detail'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),

    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<uuid:pk>/renew-staff/', views.renew_book_staff, name='renew-book-staff'),
    path('book/<uuid:pk>/renew-user/', views.renew_book_user, name='renew-book-user'),
    path('book/<uuid:pk>/test-checkout/', views.test_checkout, name='test-checkout'),
    path('book/<uuid:pk>/change-book-status-staff/', views.change_book_status_staff, name='change-book-status-staff'),

    path('contact/', views.contact_email, name='contact'),
    path('contact_email_sent/', views.contact_email_sent, name='contact_email_sent'),

    path('mybooks/', views.BorrowedBooksByUserListView.as_view(), name='my-borrowed'),
    path('allbooks/', views.BorrowedBooksByStaffListView.as_view(), name='all-borrowed'),

]
