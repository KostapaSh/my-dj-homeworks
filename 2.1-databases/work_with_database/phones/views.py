from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_phone = request.GET.get('sort', None)

    if sort_phone !=None:
        if sort_phone == 'name':
            phone_list = Phone.objects.all().order_by('name')
            print(sort_phone)
            print(phone_list)
        elif sort_phone == 'min_price':
            phone_list = Phone.objects.all().order_by('price')
            print(sort_phone)
            print(phone_list)
        elif sort_phone == 'max_price':
            phone_list = Phone.objects.all().order_by('-price')
            print(sort_phone)
            print(phone_list)
    else:
        phone_list = Phone.objects.all()
    context = {'phones': phone_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_slug = Phone.objects.filter(slug=slug)[0]
    context = {'phone': phone_slug}
    return render(request, template, context)
