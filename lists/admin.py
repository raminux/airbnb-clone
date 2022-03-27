from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """ "List Admin Definition"""

    list_display = ("name", "user", "count_rooms")
    search_fields = ("name",)
    # filter horizontal is useful when adding data to the table. It
    # shows a nice GUI to filter data and then select them.
    filter_horizontal = ("rooms",)
