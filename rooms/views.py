from django.views.generic import ListView, View
from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
from . import forms

class HomeView(ListView):
    """ HomeView Definition """
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/room_detail.html", context={
            'room': room,
        })
    except models.Room.DoesNotExist:
        raise Http404()

class SearchView(View):

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
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price  # less than and equals

                if guests is not None:
                    filter_args["guests__gte"] = guests  # greater than and equals

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                qs = models.Room.objects.filter(**filter_args).order_by("-created")

                for amenity in amenities:
                    qs = qs.filter(amenities__pk=amenity.pk)

                for facility in facilities:
                    qs = qs.filter(facilities__pk=facility.pk)

                paginator = Paginator(qs, 2)

                page = request.GET.get("page", 1)

                rooms = paginator.get_page(page)

                query_string = request.environ.get("QUERY_STRING")

                return render(request, "rooms/search.html", {
                    "form": form,
                    "rooms": rooms,
                    "query_string": query_string,
                })

        else:
            form = forms.SearchForm()

        return render(request, "rooms/search.html", {
            "form": form,
        })


