from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    user_picture = models.ImageField('Изображения пользователя',upload_to='profile_pictures/')
    contact_info = models.CharField('Контактная информация',max_length=100)
    notification_settings = models.BooleanField('Уведомления',default=True)

class Category(models.Model):
    name = models.CharField('Категория',max_length=100)
    podname = models.CharField('Подкатегория',max_length=100,null=True)
    podname_name = models.CharField('последний каталог',max_length=100,blank=True,null=True)
    img = models.ImageField(upload_to='priview',null=True)

    def __str__(self) -> str:
        return f'{self.name} {self.podname}'


    


class Attribute(models.Model):
    name = models.CharField('Атрибут (Размер/Цвет/Материал)',max_length=100)
    values = models.TextField('Значения',blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название товара',max_length=100)
    brand = models.CharField('Бренд',max_length=100)
    description = models.TextField('Описание')
    about_tovar = models.TextField('О товаре')
    price = models.DecimalField('Цена',max_digits=10, decimal_places=2)
    sale_price = models.DecimalField('Цена со скидкой',max_digits=10,decimal_places=2,null=True,blank=True)
    picture = models.ImageField('Изображение',upload_to='product/pictures/')
    quantity = models.PositiveIntegerField('Количество')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    is_on_sale = models.BooleanField(default=False)
    images = models.ManyToManyField('ProductImage', blank=True)
    sale = models.DecimalField('Процент скидки', max_digits=5 ,decimal_places=1,null=True,blank=True)
    image_sale = models.ImageField('Превью акций',upload_to='sales',null=True,blank=True)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE,null=True)
    reviews = models.ManyToManyField('Review', related_name='products', blank=True,null=True)
    question = models.ManyToManyField('Question',blank=True,related_name='products',null=True)

    def __str__(self) -> str:
        return f'{self.name} {self.brand} {self.price} '

class ProductImage(models.Model):
    image = models.ImageField('Изображение', upload_to='product/pictures/')



# class ProductAttribute(models.Model):
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='OrderItem')
    total_price = models.DecimalField('Итоговая сумма',max_digits=10, decimal_places=2)
    status = models.CharField('Статус',max_length=20)


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class ReviewImage(models.Model):
    image = models.ImageField('Изображение', upload_to='review/pictures/')


class Review(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    text = models.TextField('Отзыв')
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField('ReviewImage', blank=True)


class SellerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    user_picture = models.ImageField('Изображения продавца',upload_to='profile_pictures/',null=True)
    contact_info = models.CharField('Контактная информация',max_length=100,null=True)
    notification_settings = models.BooleanField('Уведомления',default=True,null=True)

class Question(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE,null=True)
    seller = models.ForeignKey('SellerProfile',on_delete=models.CASCADE,null=True)
    quest_user = models.TextField('Вопрос',null=True)
    answer = models.TextField('Ответ',null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE,related_name='products',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)



