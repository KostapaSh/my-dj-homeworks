from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_phone = request.GET.get('sort')

    sort_map = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }

    if sort_phone:
        phone_list = Phone.objects.all().order_by(sort_map[sort_phone])
    else:
        phone_list = Phone.objects.all()

    context = {'phones': phone_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_slug = Phone.objects.filter(slug=slug)[0]
    context = {'phone': phone_slug}
    return render(request, template, context)
