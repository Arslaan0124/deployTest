from django.shortcuts import render
from django.http import HttpResponse
from .forms import SorterForm
# Create your views here.
def SortedArray(request):
    return render(request,'sorter.html',{})
def Sortlist(unsortedList):
    
    u=unsortedList.split(',')
    for i in range(0,len(u)):
        u[i]=int(u[i])
    u.sort()
    print(u)
    return u

def GetUnsortedList(request):
    form = SorterForm(request.POST or None)
    if form.is_valid():
        arr = Sortlist(form.cleaned_data.get("unsortedList"))
        obj = {
            "unsortedList" : arr
        }
        form.save()
        return render(request,'sorter.html',obj)
        
    
    contex = {
        'form' : form,
    }
    return render(request,'getform.html',contex)
