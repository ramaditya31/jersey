from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306165502',
        'name': 'Rama',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)