from django.contrib import admin
from .models import Biog
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Biog)
class BiogAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """

    summernote_fields = ("content",)
