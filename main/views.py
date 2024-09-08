from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'price' : '$300',
        'name': 'Del Piero 1997-98 Juventus Home Jersey',
        'description': 'This is the 1997-98 Juventus home jersey worn by Alessandro Del Piero. The jersey is made by Kappa. The jersey is in excellent condition and has the original Serie A patch on the right sleeve.',
    }

    return render(request, "main.html", context)