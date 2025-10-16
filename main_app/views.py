from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import List
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms

# Define the home view function
def about(request):
    return render(request, 'about.html')

@login_required
def list(request):
    list = List.objects.filter(user=request.user).order_by('-id')
    return render(request, 'index.html', {'lists': list})

@login_required
def detail(request, item_id):
    item = List.objects.get(id=item_id)
    return render(request, 'detail.html', {'item': item})

class TaskCreate(LoginRequiredMixin, CreateView):
    model = List
    fields = ['task', 'date', 'description', 'is_complete']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date'].widget = forms.DateTimeInput(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TasktUpdate(LoginRequiredMixin, UpdateView):
    model = List
    fields = ['task', 'date', 'description', 'is_complete']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date'].widget = forms.DateTimeInput(attrs={'type': 'date'})
        return form

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = List
    success_url = '/'

class Home(LoginView):
    template_name = 'home.html'
    
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)