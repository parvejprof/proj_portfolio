from django.shortcuts import render
import os
from subprocess import call
import subprocess

from django.http import HttpResponseRedirect
from .models import Import
from .forms import ImportForm 


# Create your views here.

from .forms import ControlpanelForm


def control_panel_index(request):
   
  
    form = ControlpanelForm()
    if request.method == 'POST':
        form = ControlpanelForm(request.POST)
        if form.is_valid():
              
                 
               #  user_name=form.cleaned_data["user_name"],
                 domain_name=form.cleaned_data["domain_name"],
                             
    
                # user_name = str(user_name[0])
                 domain_name = str(domain_name[0])  

                # username = user_addition(user_name)
                 directory = dir_function(domain_name)
                 httpconffile = conffile_function(domain_name)
                 

        form = ControlpanelForm()
        return render(request, "control_panel_index.html", {"form": form, "output2": domain_name, },)

    else:
        return render(request, "control_panel_index.html", {"form": form,},)



def dir_function(user_name):
     output1 = "/var/www/" + user_name 
     return subprocess.call(['./scripts/dir_creations.py', '-p', output1])

def user_addition(output):
      return subprocess.call(['./scripts/user_creations.py','-p', output])

def conffile_function(domain_name):
     return subprocess.call(['./scripts/file_creations.py', '-p', domain_name])





   
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect



from .forms import DocumentForm
from .models import Document


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
    
        form = DocumentForm(request.POST, request.FILES)
        
        
        if form.is_valid():
           # newdoc = Document(docfile = request.FILES['docfile'])
           # newdoc.save()
            handle_uploaded_file(request.FILES["upload_file"]) 
            description = form.cleaned_data["description"],
            #form.save()

             
            
            description = (description[0])
           
            return render(request, 'model_form_upload_success.html', {'description': description})
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {'form': form})




def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)




from .forms import GeeksForm 
  
def handle_uploaded_file(f):   
    with open('media/'+f.name, 'wb+') as destination:   
        for chunk in f.chunks(): 
            destination.write(chunk)
    return (f)  
# Create your views here. 


def import_website(request): 
    context = {} 
    if request.POST: 
        form = GeeksForm(request.POST, request.FILES) 
        if form.is_valid(): 
            file_name = handle_uploaded_file(request.FILES["geeks_field"])
            description = form.cleaned_data["name"],

            description = (description[0])
            print(description)
            file_name = str(file_name)
            print(file_name)
            import_site(description, file_name)
            return render(request, 'model_form_upload_success.html', {'description': description})
    else: 
        form = GeeksForm() 
    context['form'] = form 
    return render(request, "home.html", context) 
    


def import_site(site_name, hello):
     #site = "/var/www/" + site_name 
     #print(filepath)
     return subprocess.call(['./scripts/test_import_website_setup.py', '-p', site_name, '-t', hello])
