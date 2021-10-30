from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SorterForm
# Create your views here.



def SortArray(request):
    return render(request,'sorter.html',{})


def SortList(unsortedList):
    uL = unsortedList.split(',')
    for i in range(0, len(uL)):
        uL[i] = int(uL[i])
    uL.sort()
    return uL
    

   

def GetUnsortedList(request):
    
    form = SorterForm(request.POST or None)
    if form.is_valid():
        uL = SortList(form.cleaned_data.get('unsortedList'))
        obj = {
            'sortedList':uL
        }
        form.save()
        return render(request,'sorter.html',obj)
 
    
    context = {
        'form': form,
        }
    return render(request,'getform.html',context)
   



