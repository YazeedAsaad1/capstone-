from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('about/', views.about, name='about'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('create/', views.TaskCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.TasktUpdate.as_view(), name='task-update'),
    path('<int:pk>/delete/', views.TaskDelete.as_view(), name='task-delete'),
]
