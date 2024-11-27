from django.shortcuts import render
from . models import product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    featured_products = product.objects.order_by('priority')[:4]
    latest_products = product.objects.order_by('-id')[:4]
    context={
       'featured_products':featured_products,
       'latest_products':latest_products
    }
    return render(request,'index.html',context)

def product_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    list_product=product.objects.order_by('priority')
    product_paginator=Paginator(list_product,4)
    list_product=product_paginator.get_page(page)
    context={'product':list_product}
    return render(request,'products.html',context)

def detail_product(request,pk):
    products=product.objects.get(pk=pk)
    context={'product':products}
    return render(request,'product_details.html',context)


