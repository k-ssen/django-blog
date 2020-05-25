from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'image'] #여기에는 원하는 값을 쓸 수 있음> 써주지 않는 값은 views에서 처리하면 된다.
        