from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class HomePage(Page):
    header = models.CharField(max_length=255, default='Header')
    subheader = models.CharField(max_length=255, default='Subheader')
    image = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    emphasis_text = models.CharField(max_length=255, default='Emphasis text')

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('subheader'),
        FieldPanel('image'),
        FieldPanel('emphasis_text'),
    ]
