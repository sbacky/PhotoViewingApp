# viewer/photos/views.py

import logging

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from photos.models import Photo

# Get instance of logger using namespace
logger = logging.getLogger(__name__)


def dashboard(request: HttpRequest) -> HttpResponse:
    display = "list"
    photos = Photo.objects.all().filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    return render(
        request,
        "photos/dashboard.html",
        {
            "display": display,
            "photos": photos
        }
    )


@require_POST
def photo_list(request: HttpRequest) -> HttpResponse:
    display = "list"
    photos = Photo.objects.all().filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    return render(
        request,
        "photos/photo_display.html",
        {
            "display": display,
            "photos": photos
        }
    )


@require_POST
def photo_columns(request: HttpRequest) -> HttpResponse:
    display = "column"
    photos = Photo.objects.all().filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    return render(
        request,
        "photos/photo_display.html",
        {
            "display": display,
            "photos": photos
        }
    )


def detail(request: HttpResponse, pk: int) -> HttpResponse:
    pass
