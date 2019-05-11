from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User



#게시글 형성 Form
class PostForms(forms.modelForm):
    title = forms.CharField(widget = forms.Textarea(attrs = {'placeholder': '글을 입력하세요'}), label = '')
    content = forms.CharField (label = '')
    img = forms.FileField(label = '')
    timeSet = forms.TimeField(label = '')
    class Meta:
         model = Post
         field = ['title', 'content', 'img', 'timeSet', ]

#댓글 형성 Form
class CommentForms(forms.modelForm):
    comment = forms.CharField (widget = forms.TextInput (attrs = {'placeholder': '댓글을 입력하세요.'}), label = '')
    class Meta:
        model = Comment
        field = ['content',]


#유저 정보를 저장하기 위한 Form
class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)