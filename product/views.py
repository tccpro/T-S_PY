from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product,Category
from django.core.paginator import Paginator
from utils.utils import get_order_count
SORTING = {
    'arzon':'price',
    'qimmat':'-price',
    'eski':'id',
    'yangi':'-id'
}
def home(request):
    products = Product.objects.all()[:6]
    return render(
        request=request,
        template_name='index.html',
        context={
            'products':products,
        }
    )


def product_detail(request,id):

    product = Product.objects.get(id=id)
    return render(
        request=request,
        template_name='product/product_detail.html',
        context={
            'product':product,
        }
    )


def store(request):
    cat = request.GET.get('category',0)
    page:str = request.GET.get('page',1)
    per_page:str = request.GET.get('per-page',6)
    sorting:str = request.GET.get('sorting','yangi')
    min_price:str = request.GET.get('min-price',0)
    max_price:str = request.GET.get('max-price',999999999999)
    if cat:
        products = Product.objects.filter(category=cat)
    else:
        products = Product.objects.all()
    products = products.filter(price__gte=min_price,price__lte=max_price).order_by(SORTING[sorting])
    categories = Category.objects.all()
    length = len(products)
    paginator = Paginator(
        object_list=products,
        per_page=per_page,
    )
    page = int(page)
    page = page if page<=paginator.num_pages else paginator.num_pages
    paginator_page_list = paginator.get_page(page)

    badge_count = get_order_count(request)
    return render(
        request=request,
        template_name='product/store.html',
        context={
            'products':paginator_page_list,
            'length':length,
            'categories':categories,
            'paginator':paginator,
            'current_page':int(page),
            'cat_id':int(cat),
            'sorting':sorting,
            'badge_count':badge_count,
        }
    )


def search(request):
    search_text = request.GET.get('search',None)
    product_list = Product.objects.filter(name__contains=search_text)
    categories = Category.objects.all()
    length = len(product_list)
    return render(
        request=request,
        template_name='product/store.html',
        context={
            'products':product_list,
            'length':length,
            'categories':categories,
        }
    )


