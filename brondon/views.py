from django.shortcuts import render

# Create your views here.
# Create your views here.
from .models import Home, About, Profile, Category, Skills, Projects

def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Projects
    projects = Projects.objects.all()
    

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'projects': projects
    }


    return render(request, 'index.html', context)
