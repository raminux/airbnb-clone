from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city": city})
