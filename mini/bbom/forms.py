from django import forms
from .models import Post, Comment, Univ, Summary
from django.contrib.auth.models import User

#게시글 형성 Form
class PostForms(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'menu', 'univ', 'summary']
        widgets = {
            'title' : forms.TextInput(attrs = {'placeholder':'입력해주세요'}),
        }
        labels = {
            'title' : '',
            'content' : '',
            'category' : '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['summary'].queryset = Summary.objects.none()

        if 'univ' in self.data:
            try:
                univ_id = int(self.data.get('univ'))
                self.fields['summary'].queryset = Summary.objects.filter(univ_id=univ_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['summary'].queryset = self.instance.univ.summary_set.order_by('name')

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