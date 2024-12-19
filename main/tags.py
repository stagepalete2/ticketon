from taggit.models import TagBase, GenericTaggedItemBase
from taggit.managers import TaggableManager
from django.db import models

class MetaTags(TagBase):

    class Meta:
        verbose_name = "Мета теги"
        verbose_name_plural = "Мета теги"

    # ... methods (if any) here


class MetaTagsAll(GenericTaggedItemBase):
    tag = models.ForeignKey(
        MetaTags,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )
