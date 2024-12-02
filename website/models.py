from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=200)
    slug = models.SlugField(verbose_name=_("Slug"), allow_unicode=True, max_length=200)
    author = models.ForeignKey(User,verbose_name=_("Author"), on_delete=models.SET_NULL, null=True)
    content = models.TextField(_("Content"))
    publish = models.BooleanField(verbose_name=_("Publish"), default=False)
    created = models.DateTimeField(verbose_name=_("Created"), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("Updated"), auto_now=True)
    status = models.IntegerField(verbose_name=_("Status"))
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ("-publish",)
        