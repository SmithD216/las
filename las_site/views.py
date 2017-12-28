from django.shortcuts import render

def index(request):
    """The home page for las."""
    return render(request, 'las_site/index.html')