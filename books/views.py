from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request, "index.html")
def asl_detailed(request):
     return render(request, "asl_detailed.html")
def other_works(request):
     return render(request, "other_works.html")
def about(request):
     return render(request, "about.html")
def gallery(request):
     return render(request, "gallery.html")
def blog(request):
     return render(request, "blog.html")
def events(request):
     return render(request, "event.html")
def contact(request):
     return render(request, "contact.html")
