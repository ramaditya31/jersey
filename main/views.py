from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from .models import NewJersey
from .forms import JerseyForm

# Create your views here.
def show_main(request):
    jersey = NewJersey.objects.all()
    
    return render(request, "main.html", {"jersey": jersey,})

def add_jersey(request):
    form = JerseyForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_jersey.html", context)

def show_xml(request):
    data = NewJersey.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = NewJersey.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = NewJersey.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = NewJersey.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")