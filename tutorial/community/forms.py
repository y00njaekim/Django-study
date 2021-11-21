from django.forms import ModelForm
from community import models


class Form(ModelForm):
    class Meta:
        model = models.Article
        fields = ['name', 'title', 'contents', 'url', 'email']