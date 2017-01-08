from django.contrib import admin
from blog.models import Blog, Comments

class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('title',)}

class CommentsAdmin(admin.ModelAdmin):
	readonly_fields = ('comment_text')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comments, CommentsAdmin)
