from django import forms
from .models import article

class ArticleForm(forms.ModelForm):
    class Meta:
        model=article
        fields = {'title', 'content', 'article_image'}
        fields_order = ['title', 'content', 'article_image']
        fields_keyOrder = ['title', 'content', 'article_image']
 