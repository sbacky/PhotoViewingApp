# viewer/photos/views.py

import logging

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.utils import timezone
from django.core.paginator import Paginator, Page
from django.views.decorators.http import require_POST

from photos.models import Photo

# Get instance of logger using namespace
logger = logging.getLogger(__name__)


def dashboard(request: HttpRequest) -> HttpResponse:
    photos = Photo.objects.all().filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    paginator = Paginator(photos, 12)
    page = paginator.page(1)

    return render(
        request,
        "photos/dashboard.html",
        {
            "page": page,
        }
    )


@require_POST
def page(request: HttpRequest, page_num: int) -> HttpResponse:
    photos = Photo.objects.all().filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    paginator = Paginator(photos, 12)
    current_page = paginator.page(page_num)

    hide_button = False

    if current_page.has_next():
        next_page = paginator.page(current_page.next_page_number())
        if not next_page.has_next():
            hide_button = True
        return render(
            request,
            "photos/photo_list.html",
            {
                "page": next_page,
                "hide_button": hide_button,
            }
        )
    else:
        hide_button = True
        return render(
            request,
            "photos/photo_list.html",
            {
                "hide_button": hide_button
            }
        )


def detail(request: HttpResponse, pk: int) -> HttpResponse:
    photo = Photo.objects.get(id=pk)
    return render(
        request,
        "photos/detail.html",
        {
            "photo": photo
        }
    )
