from django.shortcuts import render
from katalog.models import CatalogItem
data_katalog_item = CatalogItem.objects.all()
context = {
    'list_item': data_katalog_item,
    'name': 'Julian Justin Orvino'
}
def show_katalog(request):
    return render(request, "katalog.html", context)

