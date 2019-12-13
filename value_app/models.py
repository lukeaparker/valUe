from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class Value(models.Model):
    """ Represents a single wiki page. """
    slug = models.CharField(max_length=settings.VALUE_TAG_MAX_LENGTH, blank=True, editable=False,
                            help_text="Unique URL path to access this page. Generated by the system.")
    tag = models.TextField(unique=True,
        help_text="Enter a value tag")
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this page was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True,
                                    help_text="The date and time this page was updated. Automatically generated when the model updates.")

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/my-new-value-page). """
        path_components = {'slug': self.slug}
        return reverse('nonprof_detail', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.tag, allow_unicode=True)

        # Call save on the superclass.
        return super(Value, self).save(*args, **kwargs)