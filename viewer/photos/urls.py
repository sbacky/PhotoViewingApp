# viewer/photos/urls.py

from django.urls import path
from photos.views import dashboard, detail

app_name = "photos"

urlpatterns = [
    path("", dashboard, name="dashboard"), # <--- Dashboard View
    path("<int:pk>/", detail, name="detail"), # <--- Detail View
]