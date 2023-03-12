from django.contrib import admin
from photos.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    model = Photo

    list_display = ("name", "pub_date")
    list_filter = ("name", "pub_date")

    fieldsets = (
        (None, {
            "fields": (
                "name",
                "image",
                "description",
                "taken_date"
            ),
        }),
    )
    
    search_fields = ("name", "pub_date")

admin.site.register(Photo, PhotoAdmin)