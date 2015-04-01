from django.contrib import admin
from cart.models import ShoppingCart

class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user','time',)

admin.site.register(ShoppingCart,ShoppingCartAdmin)