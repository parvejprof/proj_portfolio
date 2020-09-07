from django.shortcuts import render
import os
from subprocess import call

# Create your views here.

from .forms import CalculateForm

total=10
total01=10

def calc_index(request):
    global total
    global total01
    
    
    
    form = CalculateForm()
    if request.method == 'POST':
        form = CalculateForm(request.POST)
        if form.is_valid():
              
                 number01=form.cleaned_data["number01"],
                 number02=form.cleaned_data["number02"],
              
                
                 total = number01 + number02
                 total01 = int(total[0]) + int(total[1])          

        res = os.listdir
        success = call('date')             

        form = CalculateForm()
        return render(request, "calc_index.html", {"form": form,"total": total01, "res": res, "success": success},)
    else:
        res = os.listdir
        return render(request, "calc_index.html", {"form": form,"res": res},)

 

    # form = CalculateForm()
    # context = {
        
    #     "form": form,
    #     "total": total01,
    # }

   # return render(request, "calc_index.html", total01)
