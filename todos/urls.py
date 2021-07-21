from django.urls import path
from .views import  TodoListView,TodoDetailView



from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

path('todos',TodoListView.as_view(),name="todo-list"),  
path('todos/<int:pk>',TodoDetailView.as_view(),name="todo-detail"),  

]

urlpatterns = format_suffix_patterns(urlpatterns)
