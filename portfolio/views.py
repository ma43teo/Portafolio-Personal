from django.shortcuts import render
from .models import Project

# Create your views here.



def portfolio(request):
    projects = Project.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        projects = projects.filter(title__icontains=search_query)

    context = {
        'projects': projects
    }
    return render(request, 'portfolio/portfolio.html', context)