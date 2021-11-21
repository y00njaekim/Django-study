from django.shortcuts import render
from community import forms
from community import models


# Create your views here.
def write(request):
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.Form()

    return render(request, 'community/write.html', {'form': form})


def list(request):
    articleList = models.Article.objects.all()
    return render(request, 'community/list.html', {'articleList': articleList})


def view(request, num="1"):
    article = models.Article.objects.get(id=num)
    return render(request, 'community/view.html', {'article': article})
