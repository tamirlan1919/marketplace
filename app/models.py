from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectFormField
from multiselectfield import MultiSelectField

# Create your models here.

class User(AbstractUser):
    # Исправленные связи
    groups = models.ManyToManyField('auth.Group', related_name='app_users', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='app_users', blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField('User',on_delete=models.CASCADE)
    user_picture = models.ImageField('Изображения пользователя',upload_to='profile_pictures/')
    contact_info = models.CharField('Контактная информация',max_length=100)
    notification_settings = models.BooleanField('Уведомления',default=True)

class Category(models.Model):
    name = models.CharField('Категория',max_length=50)
    products = models.ManyToManyField('Product', related_name='categories')

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
    picture = models.ImageField('Изображение',upload_to='product/pictures/')
    quantity = models.PositiveIntegerField('Количество')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    attributes = models.ManyToManyField('Attribute', through='ProductAttribute')
    is_on_sale = models.BooleanField(default=False)
    images = MultiSelectField('Изображения', choices=[('image1', 'Image 1'), ('image2', 'Image 2'), ('image3', 'Image 3')], max_choices=3, blank=True)



class ProductAttribute(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='OrderItem')
    total_price = models.DecimalField('Итоговая сумма',max_digits=10, decimal_places=2)
    status = models.CharField('Статус',max_length=20)


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    text = models.TextField('Отзыв')
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)



