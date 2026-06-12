from django.shortcuts import render
from django.http import Http404

from recipe.models import RecipeItem, Author

# Create your views here.
def index(request):
    data = RecipeItem.objects.all()
    author = Author.objects.all()
    return render(request, 'index.html', {'data': data, 'author':author})

def author(request, id):
    try:
        data = RecipeItem.objects.all()
        author = Author.objects.get(id=id)
        recipe = RecipeItem.objects.filter(author=author)
        return render(request, 'author.html', {'data': data, 'author':author, 'recipe':recipe})
    except Author.DoesNotExist:
        raise Http404("Author does not exist")

def recipe(request, id):
    try:
        # data = RecipeItem.objects.all()
        recipe = RecipeItem.objects.get(id=id)
        return render(request, 'recipe.html', {'recipe':recipe})
    except RecipeItem.DoesNotExist:
        raise Http404("Recipe does not exist")


