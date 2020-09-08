from django.shortcuts import render
import os
from subprocess import call
import subprocess

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
                 user_name=form.cleaned_data["user_name"],
                             
                
                 total = number01 + number02
                 total01 = int(total[0]) + int(total[1]) 
                 output = str(user_name[0])  

                 output2 = user_addition(output)
                 output = script_function(output)
                 

        res = os.listdir
        os.seteuid(0)
        os.system("touch /tmp/1.txt")
        success = call('date')             

        form = CalculateForm()
        return render(request, "calc_index.html", {"form": form,"total": total01, "res": res, "success": success, "output2": output2},)
        #return render(request, "calc_index.html", {"form": form,"total": total01, "output2": output2},)
    else:
        res = os.listdir
        return render(request, "calc_index.html", {"form": form,"res": res},)
        #return render(request, "calc_index.html", {"form": form,},)

 

    # form = CalculateForm()
    # context = {
        
    #     "form": form,
    #     "total": total01,
    # }

   # return render(request, "calc_index.html", total01)

def script_function(user_name):
     output1 = "/tmp/" + user_name 
     return subprocess.call(['./scripts/dir_creations.py', '-p', output1])

def user_addition(user_name):
      output2 = user_name + "001"
      #return output2
      return subprocess.call(['./scripts/user_creations.py','-p', output2])