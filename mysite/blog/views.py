from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post
from .forms import EmailPostForm

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
	context = {
		'post': post,
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

	if request.method == "POST":
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
	else:
		form = EmailPostForm()
	context = {
		'post': post,
		'form': form,
	}
	return render(request, 'blog/share.html', context)