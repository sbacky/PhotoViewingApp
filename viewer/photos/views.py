# viewer/photos/views.py

import logging

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.utils import timezone

from photos.models import Photo

# Get instance of logger using namespace
logger = logging.getLogger(__name__)

def dashboard(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "photos/dashboard.html"
    )

def detail(request: HttpResponse, pk: int) -> HttpResponse:
    pass
