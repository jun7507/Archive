from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages

from adul.models import BomAssemlist, BomList, BomPartlist, BomPlatelist

# Create your views here.

def select_b(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        
        search = request.GET.get('search', '')
    
        
        bomlist = BomList.objects.filter(type__icontains = search)
        p = Paginator(bomlist, 10)

        info = p.page(page)

        start_page = (int(page) - 1) // 10 * 10 + 1
        end_page = start_page + 9
        if end_page > p.num_pages:
            end_page = p.num_pages



        context = {
        'bom_list' : info,
        'page_range' : range(start_page, end_page + 1),
        'search' : search
        }
        return render(request, 'bom_t/select_b.html', context)
    
def insert(request):
    if request.method == 'POST':
        bcode = BomList.objects.order_by('-bcode').first().bcode + 1
        bcode = request.POST.get('bcode')
        assmark = request.POST.get('assmark')
        partmark = request.POST.get('partmark')
        type = request.POST.get('type')
        h = request.POST.get('h')
        b = request.POST.get('b')
        t1 = request.POST.get('t1')
        t2 = request.POST.get('t2')
        length = request.POST.get('length')
        qty = request.POST.get('qty')
        unit = request.POST.get('weight')
        grade = request.POST.get('paint')
        area = request.POST.get('weight')
        weight = request.POST.get('paint')
        pubs = BomAssemlist.objects.filter(name__icontains = assmark)        
        
        if assmark == '':
            assmark_id = 0
        elif not pubs:
            title = BomAssemlist.objects.order_by('-title').first().title + 1
            BomAssemlist.objects.create(title=title,
                                     name=assmark)
            assmark_id = title
        elif len(pubs) >= 2:
            # 2개 이상일때 선택하는 코드
            assmark_id = pubs[0].title
        else:

            assmark_id = pubs[0].title

        year_of_publication = request.POST.get('year_of_publication')
        price = request.POST.get('price')
        if price == '':
            price = 0
        

        BomList.objects.create( bcode = bcode,
                                assmark = assmark,
                                partmark = partmark,
                                type = type,
                                h = h,
                                b = b,
                                t1 = t1,
                                t2 = t2,
                                length = length,
                                qty = qty,
                                unit =unit,
                                grade =grade,
                                area = area,
                                weight = weight,
                                )

        
        return redirect('/')
        # return render(request, 'book_list/main.html')
    else:
        return render(request, 'bom_t/insert_.html')
        
def update(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        bomassem = BomList.objects.all()
        p = Paginator(bomassem, 10)

        info = p.page(page)

        start_page = (int(page) - 1) // 10 * 10 + 1
        end_page = start_page + 9
        if end_page > p.num_pages:
            end_page = p.num_pages



        context = {
        'bom_list' : info,
        'page_range' : range(start_page, end_page + 1)
        }
        return render(request, 'bom_t/update_b.html', context)
    elif request.method == 'POST':
        bcode = request.POST.get('bcode')
        assmark = request.POST.get('assmark')
        partmark = request.POST.get('partmark')
        type = request.POST.get('type')
        h = request.POST.get('h')
        b = request.POST.get('b')
        t1 = request.POST.get('t1')
        t2 = request.POST.get('t2')
        length = request.POST.get('length')
        qty = request.POST.get('qty')
        unit = request.POST.get('weight')
        grade = request.POST.get('paint')
        area = request.POST.get('weight')
        weight = request.POST.get('paint')
        pubs = BomAssemlist.objects.filter(name__icontains = assmark)
        if not pubs:
            title = BomAssemlist.objects.order_by('-assmark').first().title + 1
            BomAssemlist.objects.create(title=title,
                                     name=assmark)
            assmark_id = assmark
        elif len(pubs) >= 2:
            # 2개 이상일때 선택하는 코드
            assmark_id = pubs[0].title
        else:

            assmark_id = pubs[0].title

        grade = request.POST.get('grade')
        length = request.POST.get('length')

        update_data = BomList.objects.get(bcode = bcode)
        if assmark != '':
            update_data.assmark_id = assmark_id
        if partmark != '':
            update_data.partmark = partmark
        if type != '':
            update_data.type = type
        if h != '':
            update_data.h = h
        if b != '':
            update_data.b = b
        if t1 != '':
            update_data.t1 = t1        
        if t2 != '':
            update_data.t2 = t2
        if length != '':
            update_data.length = length        
        if qty != '':
            update_data.qty = qty            
        if unit != '':
            update_data.unit = unit
        if grade != '':
            update_data.grade = grade
        if area != '':
            update_data.area = area           
        if weight != '':
            update_data.weight = weight         
            
        update_data.save()

        return redirect('/')

# def delete(request):
#     if request.method == 'GET':
#         page = request.GET.get('page', 1)
#         booklist = BookList.objects.all()
#         p = Paginator(booklist, 10)

#         info = p.page(page)

#         start_page = (int(page) - 1) // 10 * 10 + 1
#         end_page = start_page + 9
#         if end_page > p.num_pages:
#             end_page = p.num_pages



#         context = {
#         'booklist' : info,
#         'page_range' : range(start_page, end_page + 1)
#         }
#         return render(request, 'book_t/delete.html', context)
#     elif request.method == 'POST':
#         bcode = request.POST.get('bcode')
#         BookList.objects.get(bcode = bcode).delete()
        
#         return redirect('/')