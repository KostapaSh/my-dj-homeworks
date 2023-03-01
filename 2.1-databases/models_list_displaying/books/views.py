from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book
from datetime import datetime


def books_title(request):
    template = 'books/books_title.html'
    context = {}
    return render(request, template, context)

def books_view(request):
    template = 'books/books_list.html'

    sort_books = Book.objects.all().order_by('pub_date')
    for ch_date in sort_books:
        ch_date.pub_date = ch_date.pub_date.strftime("%Y-%m-%d")

    context = {'books':sort_books}
    return render(request, template, context)

def book_date(request, data):
    template = 'books/books_list_date.html'

    book_page=0
    date_previous = None
    date_next = None
    list = 0

    books_list = Book.objects.all().order_by('pub_date')
    for ch_date in books_list:
        ch_date.pub_date = ch_date.pub_date.strftime("%Y-%m-%d")


    for count, value in enumerate(books_list):

        if data in value.pub_date:
            book_page = count + 1
            list += 1

    if list == 0:
        list =1

    paginator = Paginator(books_list, list)

    page = paginator.get_page(book_page)
    if page.has_previous():
        previous_page = paginator.get_page(page.previous_page_number())
        for rt in previous_page:
            date_previous = rt.pub_date
    else:
        date_previous = None

    if page.has_next():
        nex_page = paginator.get_page(page.next_page_number())
        for rt in nex_page:
            date_next = rt.pub_date
    else:
        date_next = None

    context = {'page': page,
               'date_next': date_next,
               'date_previous': date_previous,
               }
    return render(request, template, context)


def my_books_view():
    return None