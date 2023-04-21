from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('image','title','category','body')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Title'}),
            'category': forms.TextInput(attrs={'placeholder':'Category'}),
            'body': forms.Textarea(attrs={'placeholder':'Write Your caption here..'}),
        }
        