from django.contrib import admin
from content.models import Content


@admin.register(Content)
class PostAdmin(admin.ModelAdmin):
    """Model Post for admin-user."""
    fields = ("author", "title", 'videofile', "text", "pub_date")
    search_fields = ("text",)
    readonly_fields = ("pub_date", )
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"
