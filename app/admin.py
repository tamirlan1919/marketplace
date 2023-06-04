from django.contrib import admin
from app.models import User,UserProfile,Order,OrderItem,Category,Review,Product,Attribute
from app.models import ProductImage,Categoryy
# Register your models here.


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Attribute)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Categoryy)