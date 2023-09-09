from django.contrib import admin

# Register your models here.
from.models import Comments

class CommentsAdmin(admin.ModelAdmin):
    list_display=("name","comments","ratings","date","customer")
    
admin.site.register(Comments,CommentsAdmin)
