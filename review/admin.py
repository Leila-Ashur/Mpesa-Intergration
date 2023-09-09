from django.contrib import admin

# Register your models here.
from.models import Comments

class CommentsAdmin(admin.ModelAdmin):
    list_display=("name","comments","ratings","date")
    
admin.site.register(Comments,CommentsAdmin)
