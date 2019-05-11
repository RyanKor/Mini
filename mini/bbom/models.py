from django.db import models
from django.utils import timezone

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length = 200, help_text = "제목을 입력하세요.")
    content = models.TextField()
    img = models.FileField(null = None)
    timeSet = models.TimeField(default = timezone.now)
    author = models.CharField(max_length=50, default = "")
    
    def __str__ (self):
        return self.title

class Comment(models.Model):
    #On_delete는 이 댓글이 속한 포스트가 삭제 되었을 때 어떻게 할 것인가에 대한 행동 지시
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name = 'comments')
    content = models.TextField()
    # photo = models.FileField(null = True)
    def __str__(self):
        return self.content

         
