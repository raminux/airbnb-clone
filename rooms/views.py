from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_countries import countries
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering_by = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


class RoomDetail(DetailView):

    """Room Detail Definition"""

    model = models.Room
    pk_url_kwarg = "pk"
    template_name = "rooms/room_detail.html"


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    selected_country = request.GET.get("country", "IR")
    selected_room_type = int(request.GET.get("room_type", 0))
    selected_amenities = request.GET.getlist("amenities")
    selected_facilities = request.GET.getlist("facilities")
    selected_instant = bool(request.GET.get("instant", False))
    selected_super_host = bool(request.GET.get("super_host", False))

    price = int(request.GET.get("price", 0))
    beds = int(request.GET.get("beds", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    baths = int(request.GET.get("baths", 0))

    form = {
        "city": city,
        "selected_country": selected_country,
        "selected_room_type": selected_room_type,
        "price": price,
        "beds": beds,
        "guests": guests,
        "bedrooms": bedrooms,
        "baths": baths,
        "selected_amenities": selected_amenities,
        "selected_facilities": selected_facilities,
        "selected_instant": selected_instant,
        "selected_super_host": selected_super_host,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = selected_country

    if selected_room_type != 0:
        filter_args["room_type__pk"] = selected_room_type

    if price != 0:
        filter_args["price__lte"] = price

    if beds != 0:
        filter_args["beds__gte"] = beds

    if guests != 0:
        filter_args["guests__gte"] = guests

    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if baths != 0:
        filter_args["baths__gte"] = baths

    if selected_instant is True:
        filter_args["instant_book"] = True

    if selected_super_host is True:
        filter_args["host__superhost"] = True

    rooms = models.Room.objects.filter(**filter_args)

    if len(selected_amenities) > 0:
        for s_amenity in selected_amenities:
            rooms = rooms.filter(amenities__pk=int(s_amenity))

    if len(selected_facilities) > 0:
        for s_facility in selected_facilities:
            rooms = rooms.filter(facilities__pk=int(s_facility))

    print(filter_args)

    return render(
        request,
        "rooms/search.html",
        {
            **form,
            **choices,
            "rooms": rooms,
        },
    )
