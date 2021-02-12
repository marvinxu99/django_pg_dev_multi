from django.contrib import admin
from .models import Issue, Comment, SavedIssue, Tag

# Register your models here.


class CommentAdminInline(admin.StackedInline):
    model = Comment


class CommentAdmin(admin.ModelAdmin):
    inlines = (CommentAdminInline, )


admin.site.register(Issue, CommentAdmin)
admin.site.register(SavedIssue)
admin.site.register(Tag)
