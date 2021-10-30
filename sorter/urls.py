from django.urls import path
from . import views

urlpatterns = [
    path('sort/',views.SortedArray),
    path('getsort/',views.GetUnsortedList),
]