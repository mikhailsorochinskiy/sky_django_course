from django.contrib import admin
from .models import BlogReview
# Register your models here.
@admin.register(BlogReview)
class BlogReview(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'see_counter')
    search_fields = ('title',)