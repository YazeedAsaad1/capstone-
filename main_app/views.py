from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import List

# Define the home view function
def about(request):
    return render(request, 'about.html')

def list(request):
    list = List.objects.all()
    return render(request, 'index.html', {'lists': list})

def detail(request, item_id):
    item = List.objects.get(id=item_id)
    return render(request, 'detail.html', {'item': item})

class TaskCreate(CreateView):
    model = List
    fields = '__all__'
    success_url = '/'