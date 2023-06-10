from django.shortcuts import render,get_object_or_404
from app.models import Category,Product,Review,Question
from .forms import UserLoginForm,SignupForm
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate 
from .forms import SignupForm,UserProfileForm
from django.contrib.sites.shortcuts import get_current_site 
from django.utils.encoding import force_bytes, force_str 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.template.loader import render_to_string 
from .token import account_activation_token 
from django.contrib.auth.models import User 
from django.core.mail import send_mail
from .models import UserProfile
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage 
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



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            User = get_user_model()
            try:
                existing_user = User.objects.get(email=email)
                return HttpResponse('This email was in database')
            except User.DoesNotExist:
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = account_activation_token.make_token(user)
                activation_link = f"http://{current_site.domain}/activate/{uid}/{token}/"

                mail_subject = 'Activation link has been sent to your email id'
                message = f"Hello {user.username},\n\nClick the following link to activate your account:\n\n{activation_link}"

                send_mail(mail_subject, message, 'tchinchaev@bk.ru', [user.email])

                return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})

def activate(request, uidb64, token): 
    User = get_user_model() 
    try: 
        uid = force_str(urlsafe_base64_decode(uidb64)) 
        user = User.objects.get(pk=uid) 
    except(TypeError, ValueError, OverflowError, User.DoesNotExist): 
        user = None 
    if user is not None and account_activation_token.check_token(user, token): 
        user.is_active = True 
        user.save() 
        
        user_profile = get_object_or_404(UserProfile, user=user)
        user_profile.user = User.objects.get(username=user_profile.user.username)
        user_profile.save()

        return HttpResponse('Thank you for your email confirmation. Now you can login your account.') 
    else: 
        return HttpResponse('Activation link is invalid!') 

def user_logout(request):
    logout(request)
    return redirect('/')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})

@login_required
def profile_user(request):
    user = request.user
    user_profile = user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            # Получение текущего пользователя
            user = request.user

            # Сохранение данных профиля пользователя
            profile = user.userprofile
            profile.name = form.cleaned_data.get('name')
            profile.second_name = form.cleaned_data.get('second_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.date_br = form.cleaned_data.get('date_br')
            profile.gender = form.cleaned_data.get('gender')
            profile.phone_number = form.cleaned_data.get('phone_number')
            profile.address_city = form.cleaned_data.get('address_city')
            profile.address_street = form.cleaned_data.get('address_street')
            profile.address_house = form.cleaned_data.get('address_house')
            profile.address_podezd = form.cleaned_data.get('address_podezd')
            profile.address_kv = form.cleaned_data.get('address_kv')
            profile.comment = form.cleaned_data.get('comment')
            profile.notification_settings = form.cleaned_data.get('notification_settings')
            profile.user_picture = form.cleaned_data.get('user_picture')
            profile.save()

            return redirect('/')  # Перенаправление на страницу профиля
    else:
        form = UserProfileForm()
    
    return render(request, 'profile_info.html',{'user_profile': user_profile,'form': form})


@login_required
def cart(request):
    return render(request,'cart.html')


@login_required
def likes(request):
    return render(request,'likes.html')

@login_required
def order(request):
    return render(request,'orders.html')