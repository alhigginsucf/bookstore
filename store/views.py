from django.shortcuts import render

from .models import Book

 

def store(request):

   count = Book.objects.all().count()

   context = {

       'count': count,

   }

   request.session['location'] = "unknown"  # Session variable

   if request.user.is_authenticated:        # Is the user authenticated?

       request.session['location'] = "Earth"

   return render(request, "store.html", context)