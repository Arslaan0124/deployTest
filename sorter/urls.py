from django.urls import path
from . import views

urlpatterns = [ 
    path('sort/',views.SortArray),
    path('create/',views.GetUnsortedList)
]




