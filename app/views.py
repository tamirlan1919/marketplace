from django.shortcuts import render,get_object_or_404
from app.models import Category,Product,Review,Question
from .forms import UserLoginForm,SignupForm
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate 
from .forms import SignupForm 
from django.contrib.sites.shortcuts import get_current_site 
from django.utils.encoding import force_bytes, force_str 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.template.loader import render_to_string 
from .token import account_activation_token 
from django.contrib.auth.models import User 
from django.core.mail import send_mail
from .models import UserProfile
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
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            user_profile = UserProfile.objects.create()
            user_profile.user = user
            user_profile.save()

            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()

            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()

    return render(request, 'register.html', {'form': form})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can log in to your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def user_logout(request):
    logout(request)
    return redirect('home')

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