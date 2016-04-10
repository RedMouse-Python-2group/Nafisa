from django.contrib import admin

# Register your models here.

from .models import CategoryName, Post



class PostModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "author", "created_date",'category']
	class Meta:
		model = Post



admin.site.register(Post, PostModelAdmin)
admin.site.register(CategoryName)
