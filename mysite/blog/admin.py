from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
	# List of fields to be displyed in PostAdmin
	list_display = ('title', 'author', 'publish', 'created', 'updated', 'status')
	# Display title field as a link
	list_display_links = ('title',)
	# Adds List filter on the right site bar of the Post List page
	list_filter = ('status', 'created', 'publish', 'author')
	# Makes the status field editable on the Post List page
	list_editable = ('status',)
	# Adds a search list field on top of the Post List page
	search_fields = ('title', 'body')
	# Prepopulates slug field as you type the Post title
	prepopulated_fields = {'slug': ('title',)}
	# Makes the author field a searchable field in Post (replaces + add)
	raw_id_fields = ('author',)
	# Adds Bar to navigate quickly through a date hierarchy
	date_hierarchy = 'publish'
	# Adds list ordering by status and publish fields
	ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'post', 'created', 'active',)
	list_filter = ('active', 'created', 'updated',)
	search_fields = ('name', 'email', 'body',)


# Register your models here.
admin.site.register(Post, PostAdmin)