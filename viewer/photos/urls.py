# viewer/photos/urls.py

from django.urls import path
from photos.views import dashboard, photo_list, photo_columns, detail

app_name = "photos"

urlpatterns = [
    path("", dashboard, name="dashboard"), # <--- Dashboard View
    path("list/", photo_list, name="list"),
    path("columns/", photo_columns, name="columns"),
    path("<int:pk>/", detail, name="detail"), # <--- Detail View
]