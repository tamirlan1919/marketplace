from django.shortcuts import render,get_object_or_404
from app.models import Category,Product,Review
# Create your views here.


def index(request):
    sub = Category.objects.values('podname').distinct()
    pod = Category.objects.values('name','podname').distinct()
    data = Category.objects.values('name').distinct()
    category = Category.objects.all()
    data_id = Category.objects.values('id','name',).distinct()
    tovars = Product.objects.all()
    print(data)
    return render(request, 'index.html',{'cat':data,'pod': pod,'subb':sub,'tovars':tovars,'categ':category})




def products_by_category_view(request, cat_id:int):
    category = Category.objects.get(id=cat_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products.html', {'products': products})



def show_sub_tovar(request,id_clothes:int):
    tovar = get_object_or_404(Product,id = id_clothes)
    tovars = Product.objects.all()
    reviews = Review.objects.all()
    return render(request,'sub_tovar.html',{'tovar':tovar,'tovars':tovars,'reviews':reviews})
