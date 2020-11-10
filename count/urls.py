
from . import view
from django.urls import path

urlpatterns = [
    path('',view.homepage, name = 'home'),
    path('eggs',view.eggs),
    path('count',view.count, name = 'count'),
    path('abouts',view.about, name = 'about'),
]
