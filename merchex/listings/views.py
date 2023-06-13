from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Band
from listings.models import Listing

navigation = [
    {'title': 'Home', 'path': '/hello'},
    {'title': 'About', 'path': '/about-us'},
    {'title': 'Listings', 'path': '/listings'},
    {'title': 'Help', 'path': '/help'}
]


def bands_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/bands_list.html', {'bands': bands, 'nav': navigation})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band, 'id': id, 'nav': navigation})  # nous passons l'id au modèle


def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings, 'nav': navigation})


def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request,
                  'listings/listing_detail.html',
                  {'listing': listing, 'id': id, 'nav': navigation})


def about(request):
    return render(request, 'listings/about.html', {'title': 'About Us', 'nav': navigation})


def help(request):
    return render(request, 'listings/help.html', {'title': 'Help', 'nav': navigation})
