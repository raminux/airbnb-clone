from math import ceil
from django.utils import timezone
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, View
from . import models, forms


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


class SearchView(View):

    """Search Room Definition"""

    def get(self, request):

        country = request.GET.get("country")

        if country:
            form = forms.SearchForm(request.GET)

            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                beds = form.cleaned_data.get("beds")
                bedrooms = form.cleaned_data.get("bedrooms")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city"] = city

                # filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                qs_rooms = models.Room.objects.filter(**filter_args)

                for amenity in amenities:
                    qs_rooms = qs_rooms.filter(amenities=amenity)

                for facility in facilities:
                    qs_rooms = qs_rooms.filter(facilities=facility)

                print(request.get_full_path())
                qs_rooms = qs_rooms.order_by("created")

                page_size = 10
                page = request.GET.get("page")
                page = int(page or 1)
                paginator = Paginator(qs_rooms, page_size, orphans=5)
                rooms = paginator.get_page(page)

                href = request.get_full_path()
                if "page" in href:
                    print(href)
                    index = [i for i, ltr in enumerate(href) if ltr == "&"]
                    index = index[-1]
                    print(index)
                    href = href[0:index]

                return render(
                    request,
                    "rooms/search.html",
                    {
                        "form": form,
                        "rooms": rooms,
                        "href": href,
                    },
                )
        else:
            form = forms.SearchForm()

        return render(
            request,
            "rooms/search.html",
            {
                "form": form,
            },
        )
