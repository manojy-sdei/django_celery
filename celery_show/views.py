from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .task import *
# from .helper import *
from django.core.files.storage import FileSystemStorage
import os
from docx2pdf import convert

from celery.result import AsyncResult
# Create your views here.



def index(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        file_name = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(file_name)
        data = convert_doc_to_pdf.delay(myfile.name)
        return HttpResponseRedirect(data.task_id)
        

    return render(request, "home.html")


def check_status(request, task_id):
    res = AsyncResult(task_id)
    print(res.ready()) # to know the status of task `{if ture tasks completed if false task incomplete }`
    context = {'task_status':res.ready()}
    return render(request,'progress.html', context)


#celery -A celery_example worker -l info -P eventlet