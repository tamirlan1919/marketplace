from django.contrib import admin
from app.models import User,UserProfile,Order,OrderItem,Category,Review,Product,ProductAttribute,Attribute
# Register your models here.


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Attribute)
admin.site.register(Product)
admin.site.register(ProductAttribute)