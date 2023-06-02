from django.shortcuts import render
from app.models import Category,Product
# Create your views here.


def index(request):
    sub = Category.objects.values('podname').distinct()
    pod = Category.objects.values('name','podname','podname_name').distinct()
    data = Category.objects.values('name').distinct()
    data_id = Category.objects.values('id','name',).distinct()
    print(data)
    return render(request, 'index.html',{'cat':data,'pod': pod,'subb':sub})




def products_by_category_view(request, cat_id:int):
    category = Category.objects.get(id=cat_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products.html', {'products': products})