from django.db import models
from djangotoolbox.fields import ListField

# Create your models here.

class Company(models.Model):
    company_id = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

class Document(models.Model):
    file_name = models.CharField(max_length=200)
    pdf_doc = models.FileField(upload_to='pdf', null=True, blank=True)
    company_id = models.ForeignKey('Company')
    calculated_company_name = models.CharField(max_length=200)
    calculated_state = models.CharField(max_length=200)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)