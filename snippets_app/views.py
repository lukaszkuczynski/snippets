from django.shortcuts import render

# Create your views here.

from .models import Snippet

def index(request):
    snippets = Snippet.objects.all()
    return render(request, 'index.html', context={"snippets": snippets})