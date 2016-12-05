from django import template
from django.db.models import Count

register = template.Library()

from ..models import Post

# Simple Template tag to display total number of posts in the blog
@register.simple_tag
def total_posts():
	return Post.published.count()

# Inclusion Tag to display the Latest Post in the blog page
@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=5):
	latest_posts = Post.published.order_by('-publish')[:count]
	return {'latest_posts': latest_posts}

# Assignment Tag to display most commented Post
@register.assignment_tag
def get_most_commented_posts(count=5):
	return Post.published.annotate(
		total_comments=Count('comments')).order_by('-total_comments')[:count]