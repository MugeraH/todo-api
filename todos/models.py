from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description=  models.TextField(null=True)
    completed = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
       
    def save_todo(self):
        self.save()

    def delete_todo(self):
        self.delete()
        
    @classmethod
    def get_todo_by_id(cls,id):
        todo = Todo.objects.filter(pk=id)
        return todo
        
    
    def __str__(self):
        return self.title
