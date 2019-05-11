from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

#게시글 형성 Form
class PostForms(forms.ModelForm):
    class Meta:
         model = Post
         fields = ('title', 'content', 'school', 'category', 'menu', 'img', )
         widget = {
             forms.TextInput(attrs = {'placeholder':'글을 입력하세요'}),
         }
         labels = {
             'content' : '',
             'img': '',
             'category' : '',
         }

#댓글 형성 Form
class CommentForms(forms.ModelForm):
    comment = forms.CharField (widget = forms.TextInput (attrs = {'placeholder': '댓글을 입력하세요.'}), label = '')
    class Meta:
        model = Comment
        fields = ['content',]

#유저 정보를 저장하기 위한 Form
class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)