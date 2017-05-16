from django.db import models
from utils import csv_rows

# Create your models here.


class Company(models.Model):
    company_id = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    @classmethod
    def populate(cls):
        for row in csv_rows('Companies.csv'):
            Company.objects.get_or_create(
                company_id = row[2],
                name = row[0],
                state = row[1]
            )


class Document(models.Model):
    file_name = models.CharField(max_length=200)
    pdf_doc = models.FileField(upload_to='pdf', null=True, blank=True)
    url = models.CharField(max_length=300)
    company = models.ForeignKey('Company',null=True)
    calculated_company_name = models.CharField(max_length=200)
    calculated_state = models.CharField(max_length=200)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)