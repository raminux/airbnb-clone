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
    selected_instant = request.GET.get("instant", False)
    selected_super_host = request.GET.get("super_host", False)

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
    return render(
        request,
        "rooms/search.html",
        {**form, **choices},
    )
