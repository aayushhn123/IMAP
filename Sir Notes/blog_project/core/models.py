from django.db import models
import uuid
# Create your models here.

class Blog(models.Model):
    
    title = models.CharField(max_length=2048)
    subtitle = models.CharField(max_length=2048)
    author = models.CharField(max_length=128)
    content = models.TextField()
    upload_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}"
    
class Comment(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    blog_id = models.ForeignKey(to=Blog, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
