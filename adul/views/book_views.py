from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages

from adul.models import BookList, BookStore

# Create your views here.

def select(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        
        search = request.GET.get('search', '')
    
        
        booklist = BookList.objects.filter(title__icontains = search)
        p = Paginator(booklist, 10)

        info = p.page(page)

        start_page = (int(page) - 1) // 10 * 10 + 1
        end_page = start_page + 9
        if end_page > p.num_pages:
            end_page = p.num_pages



        context = {
        'booklist' : info,
        'page_range' : range(start_page, end_page + 1),
        'search' : search
        }
        return render(request, 'book_t/select.html', context)
    
def insert(request):
    if request.method == 'POST':
        bcode = BookList.objects.order_by('-bcode').first().bcode + 1
        title = request.POST.get('title')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        pubs = BookStore.objects.filter(name__icontains = publisher)        
        
        if publisher == '':
            publisher_id = 0
        elif not pubs:
            bscode = BookStore.objects.order_by('-bscode').first().bscode + 1
            BookStore.objects.create(bscode=bscode,
                                     name=publisher)
            publisher_id = bscode
        elif len(pubs) >= 2:
            # 2개 이상일때 선택하는 코드
            publisher_id = pubs[0].bscode
        else:

            publisher_id = pubs[0].bscode

        year_of_publication = request.POST.get('year_of_publication')
        price = request.POST.get('price')
        if price == '':
            price = 0
        

        BookList.objects.create(bcode=bcode,
                                title=title,
                                author=author,
                                publisher_id=publisher_id,
                                year_of_publication=year_of_publication,
                                price=price)

        
        return redirect('/')
        # return render(request, 'book_list/main.html')
    else:
        return render(request, 'book_t/insert.html')
        
def update(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        booklist = BookList.objects.all()
        p = Paginator(booklist, 10)

        info = p.page(page)

        start_page = (int(page) - 1) // 10 * 10 + 1
        end_page = start_page + 9
        if end_page > p.num_pages:
            end_page = p.num_pages



        context = {
        'booklist' : info,
        'page_range' : range(start_page, end_page + 1)
        }
        return render(request, 'book_t/update.html', context)
    elif request.method == 'POST':
        bcode = request.POST.get('bcode')
        title = request.POST.get('title')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        pubs = BookStore.objects.filter(name__icontains = publisher)
        if not pubs:
            bscode = BookStore.objects.order_by('-bscode').first().bscode + 1
            BookStore.objects.create(bscode=bscode,
                                     name=publisher)
            publisher_id = bscode
        elif len(pubs) >= 2:
            # 2개 이상일때 선택하는 코드
            publisher_id = pubs[0].bscode
        else:

            publisher_id = pubs[0].bscode

        year_of_publication = request.POST.get('year_of_publication')
        price = request.POST.get('price')

        update_data = BookList.objects.get(bcode = bcode)
        if title != '':
            update_data.title = title
        if author != '':
            update_data.author = author
        if publisher != '':
            update_data.publisher_id = publisher_id
        if year_of_publication != '':
            update_data.year_of_publication = year_of_publication
        if price != '':
            update_data.price = price

        update_data.save()

        return redirect('/')

def delete(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        booklist = BookList.objects.all()
        p = Paginator(booklist, 10)

        info = p.page(page)

        start_page = (int(page) - 1) // 10 * 10 + 1
        end_page = start_page + 9
        if end_page > p.num_pages:
            end_page = p.num_pages



        context = {
        'booklist' : info,
        'page_range' : range(start_page, end_page + 1)
        }
        return render(request, 'book_t/delete.html', context)
    elif request.method == 'POST':
        bcode = request.POST.get('bcode')
        BookList.objects.get(bcode = bcode).delete()
        
        return redirect('/')