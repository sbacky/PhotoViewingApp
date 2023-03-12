# viewer/photos/urls.py

from django.urls import path
from photos.views import dashboard, page, detail

app_name = "photos"

urlpatterns = [
    path("", dashboard, name="dashboard"), # <--- Dashboard View
    path("page/<int:page_num>", page, name="page"), # <--- Page View
    path("<int:pk>/", detail, name="detail"), # <--- Detail View
]