"""firstSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from books.views import index
from books.views import asl_detailed
from books.views import other_works
from books.views import about
from books.views import blog
from books.views import gallery
from books.views import events
from books.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
	path('index.html', index),
	path('', index),
	path('asl_detailed.html', asl_detailed),
	path('other_works.html', other_works),
	path('about.html', about),
	path('blog.html', blog),
	path('gallery.html', gallery),
	path('event.html', events),
	path('contact.html', contact),
]
