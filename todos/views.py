from django.shortcuts import render
from django.http import Http404

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET'])
def apiOverview(request):
    # '''
    # Set safe=False to allow other data types rather than dictionary
    # In order to allow non-dict objects to be serialized set the safe parameter to False 
    # '''
    api_urls = {
        'List': '/api/todos/',
        'Detail View': '/api/todos/<int:pk>/',
        'Create': '/api/todos/',
        'Update': '/api/todos/<int:pk>/',
        'Delete': '/api/todos/<int:pk>/',
    }
    
    return Response(api_urls)


class TodoListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    
    def get(self,request,*args,**kwargs): 
        return self.list(self,request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs): 
        return self.create(request,*args,**kwargs)
    
    
class TodoDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
