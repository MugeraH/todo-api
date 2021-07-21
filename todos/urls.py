from django.urls import path
from .views import  apiOverview,TodoListView,TodoDetailView



from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
 path('',apiOverview,name='api'),
path('api/todos',TodoListView.as_view(),name="todo-list"),  
path('api/todos/<int:pk>',TodoDetailView.as_view(),name="todo-detail"),  

]

urlpatterns = format_suffix_patterns(urlpatterns)
