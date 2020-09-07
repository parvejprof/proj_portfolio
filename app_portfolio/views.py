from django.shortcuts import render
from app_portfolio.models import Portfolio

# Create your views here.

def project_index(request):
    projects = Portfolio.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Portfolio.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
