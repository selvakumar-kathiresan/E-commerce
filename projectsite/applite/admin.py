from django.contrib import admin
from applite.models import *

class CatagoryAdmin(admin.ModelAdmin):
	list_display=['name','image','description']

admin.site.register(Catagory,CatagoryAdmin)
admin.site.register(Product)