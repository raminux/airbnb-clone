from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "bedrooms",
        "beds",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )
    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    search_fields = (
        "city",
        "host__username",
    )
    ordering = ("name", "price", "bedrooms")
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )
    fieldsets = (
        (
            "Basic Information",
            {
                "fields": ("name", "description", "country", "address", "price"),
            },
        ),
        (
            "Times",
            {
                "fields": ("check_in", "check_out", "instant_book"),
            },
        ),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More about the space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass
