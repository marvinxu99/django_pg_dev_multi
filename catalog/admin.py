from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language


class BookInline(admin.StackedInline):
    model = Book
    fieldsets = (
        (None, {
            'fields': ('title', )
        }),
        ('more information', {
            'classes': ('collapse',),
            'fields': ('summary', 'genre', ('isbn', 'language'), )
        }),
    )

    extra = 0


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline, ]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


admin.site.register(Language)
admin.site.register(Genre)
