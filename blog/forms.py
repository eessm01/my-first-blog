from django import forms

# models 
from .models import Post


class PostForm(forms.ModelForm):
  
  class Meta:
    model = Post
    fields = ('title', 'text',)
    