from django.contrib import admin
from products.models import Product, ProductImage, ProduCategory

# Register your models here.
#Administraremos los sgtes models

#Admin para image product en linea con product
class ProductImageInLine(admin.TabularInline):
	model = ProductImage

#Admin para product
class ProductAdmin(admin.ModelAdmin):
	#para que nuestro slug de producto se llene al mismo tiempo que
	#se escribe el nombre del producto
	prepopulated_fields = {"slug" : ("title",)}
	inlines = [
		ProductImageInLine
	]

#Registramos
admin.site.register(Product, ProductAdmin)
admin.site.register(ProduCategory)