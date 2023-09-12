
# Register your models here.
from django.contrib import admin
from comment.models import ReviewComments


class ReviewCommentsAdmin(admin.ModelAdmin):
    list_display = ("equipment_name", "comments", "ratings", "Time_stamp", "customer")


admin.site.register(ReviewComments, ReviewCommentsAdmin)
