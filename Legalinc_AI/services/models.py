from django.db import models
from djangotoolbox.fields import ListField

# Create your models here.


class File(models.Model):
    name = models.CharField(max_length=200)
    pdf_doc = models.FileField(upload_to='pdf', null=True, blank=True)
    company_names = ListField(models.CharField())
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)