from django.contrib import admin
from app.models import UserProfile,Order,OrderItem,Category,Review,Product,Attribute
from app.models import ProductImage,Question,SellerProfile,Cart
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Attribute)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Question)
admin.site.register(SellerProfile)
admin.site.register(Cart)