from django.shortcuts import render
from .models import Jersey

# Create your views here.
def show_main(request):
    jersey = Jersey.objects.all()
    
    return render(request, "main.html", {"jersey": jersey,})