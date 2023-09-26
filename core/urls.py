from django.urls import path
from .views import *
urlpatterns = [
   path('', home, name="Home"),
   path('ai-images/<str:query>', gallery, name="gallery"),
]
    