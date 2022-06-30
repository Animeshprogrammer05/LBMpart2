from django.shortcuts import render

from .models import *

def Booklistview(request):
    book_list=Book.objects.all()
    context={'book_list':book_list}
    return render(request,'catlog/book_dtail.html',context)

