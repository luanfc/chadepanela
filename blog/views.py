from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Create your views here.
def item_list(request):
    itens = Item.objects.order_by('ordem')
    template_name = 'blog/item_list.html'
    return render(request, template_name, {'itens': itens})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'blog/item_detail.html', {'item': item})


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        item = form.save(commit=False)
        item.ativo = 1
        item.save()
        return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'blog/item_edit.html', {'form': form})
