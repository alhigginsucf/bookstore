from django.shortcuts import render

from .models import Book

 

# Create your views here.

def store(request):

   count = Book.objects.all().count()

   context = {

       'count': count,

   }

   return render(request, "store.html", context)