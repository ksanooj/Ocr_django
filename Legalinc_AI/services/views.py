from django.shortcuts import render
from django.views.generic import View
from services.models import Document
from django.core.files.storage import FileSystemStorage

# Create your views here.
from Legalinc_AI.settings import  MEDIA_ROOT


class HomeView(View):
    @staticmethod
    def get(request):
        files = Document.objects.all()
        data = dict()
        data['files']=files
        data['pdf_url']=MEDIA_ROOT+'/pdf'
        return render(request, 'index.html',data)


    @staticmethod
    def post(request):
        if request.method == 'POST' and request.FILES['myfile']:
            file = Document()
            file.name = str(request.FILES['myfile'].name)
            file.pdf_doc = request.FILES['myfile']
            files = Document.objects.all()
            data = dict()
            data['files'] = files
            file.save()
            return render(request, 'index.html', data)

