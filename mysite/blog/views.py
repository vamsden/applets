from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views.generic import ListView
from .models import Comment, Post
from .forms import EmailPostForm, CommentForm

# Create your views here.
"""def post_list(request):
	object_list = Post.published.all()
	paginator = Paginator(object_list, 3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
		'page': page,
		'posts': posts,
	}
	return render(request, 'blog/list.html', context)"""

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post,
								   status='published',
								   publish__year=year,
								   publish__month=month,
								   publish__day=day)
	# List of active comments for the current post
	comments = post.comments.filter(active=True)

	if request.method == "POST":
		# Comment Posted
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			# Assigns the current post to the comment
			new_comment.post = post
			# Save the comment
			new_comment.save()
	else:
		comment_form = CommentForm()
	context = {
		'post': post,
		'comments': comments,
		'comment_form': comment_form,
	}
	return render(request, 'blog/detail.html', context)


# Post List View in class based form
class PostListView(ListView):
	queryset = Post.published.all() # model = Post
	context_object_name = 'posts' # default: object_list
	paginate_by = 3
	template_name = 'blog/list.html'


# Share Post View
def post_share(request, post_id):
	post = get_object_or_404(Post, id=post_id, status="published")
	sent = False
	receiver = ""

	if request.method == "POST":
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			receiver = cd['to']
			post_url = request.build_absolute_uri(post.get_absolute_url())
			subject = '{} ({}) recommends you reading "{}"'.format(
				cd['name'], cd['email'], post.title)
			message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(
				post.title, post_url, cd['name'], cd['comments'])
			send_mail(subject, message, 'admin@myblog.com', [cd['to']])
			sent = True
	else:
		form = EmailPostForm()
	context = {
		'post': post,
		'form': form,
		'sent': sent,
		'receiver': receiver,
	}
	return render(request, 'blog/share.html', context)