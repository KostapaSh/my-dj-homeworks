from pprint import pprint

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, reverse


def getrecipe(servings, my_dish) -> dict():


    DATA = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
        # можете добавить свои рецепты ;)
    }


    context = {
        'recipe':{}
    }

    if servings != None:
        for ket, val in DATA[my_dish].items():
            context['recipe'][ket] = val*int(servings)
    else:
        for ket, val in DATA[my_dish].items():
            context['recipe'][ket] = val

    return context

def home_view(request):

    template_name = 'calculator/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Рецепт омлета': 'omlet/',
        'Рецепт пасты': 'pasta/',
        'Рецепт бутерброда': 'buter/',
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def dish_view (request, dish):

    #vv_dish = request.path_info.replace('/', '')
    servings = request.GET.get('servings')

    return render(request, 'calculator/index.html', getrecipe(servings,dish))



# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
