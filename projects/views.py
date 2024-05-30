from django.shortcuts import render
from projects.models import Project
# Create your views here.
def project_index(request, pk):
    projects = Project.objects.get(pk=pk)
    context = {
            "projects": projects
     }
    return render(request, "projects/project_index.html", context)

