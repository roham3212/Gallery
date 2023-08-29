from django.contrib import admin
from .models import Services



# Register your models here.




class AdminServices(admin.ModelAdmin):
    list_display = ['title', 'content', 'statues']
    list_filter = ['statues']
    search_fields = ['title', 'content']
    


admin.site.register(Services, AdminServices,)

