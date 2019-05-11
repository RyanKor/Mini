from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])

class Post(models.Model):
    CHOICES = (
    ('man', 'man'),
    ('woman', 'woman'),
    )

    title = models.CharField(max_length = 200, help_text = "제목을 입력하세요.")
    content = models.TextField()
    img = models.FileField(null = True)
    author = models.CharField(max_length=50, default = "")
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='product')
    gender = models.CharField(max_length=30, choices=CHOICES)
    univ = (
        ('KU', '고려대학교'),
        ('Yonsei', '연세대학교'),
        ('SeongShin', '성신여대'),
    )

    KUspot = (
        ('KU', '고려대 CU'),
        ('KU', '고려대 GS25'),
        ('KU', '고려대 미니스톱'),
    )
    Yspot = (
        ('Yonsei', '연세 CU'),
        ('Yonsei', '연세 GS25'),
        ('Yonsei', '연세 미니스톱'),
    )
    Sspot = (
        ('SeongShin', '성신 CU'),
        ('SeongShin', '성신 GS25'),
        ('SeongShin', '성신 미니스톱'),
    )
    school = models.CharField(max_length=30, choices=univ)
    kp = models.CharField(max_length = 30, choices = KUspot)
    yp = models.CharField(max_length = 30, choices = Yspot)
    sp = models.CharField(max_length = 30, choices = Sspot)
    def __str__ (self):
        return self.title

class Comment(models.Model):
    #On_delete는 이 댓글이 속한 포스트가 삭제 되었을 때 어떻게 할 것인가에 대한 행동 지시
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name = 'comments')
    content = models.TextField()
    # photo = models.FileField(null = True)
    def __str__(self):
        return self.content