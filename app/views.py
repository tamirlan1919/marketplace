from django.shortcuts import render,get_object_or_404
from app.models import Category,Product,Review,Question
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
from django.contrib import messages
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
    questions = Question.objects.all()
    return render(request,'sub_tovar.html',{'tovar':tovar,'tovars':tovars,'reviews':reviews,
                                            'len':len(reviews), 'quest':questions,
                                            'len_quest':len(questions)})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('home')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})