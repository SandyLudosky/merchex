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


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands, 'nav': navigation})


def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings, 'nav': navigation})


def about(request):
    return render(request, 'listings/about.html', {'title': 'About Us', 'nav': navigation})


def help(request):
    return render(request, 'listings/help.html', {'title': 'Help', 'nav': navigation})
