from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import List
from django.contrib.auth.views import LoginView

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

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class TasktUpdate(UpdateView):
    model = List
    fields = ['task', 'date', 'description', 'is_complete']

class TaskDelete(DeleteView):
    model = List
    success_url = '/'

class Home(LoginView):
    template_name = 'home.html'
    

