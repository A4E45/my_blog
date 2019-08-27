from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
def home(request):
	posts = Post.objects.all()
	paginator = Paginator(posts, 4)
	page = request.GET.get('page')
	try:
	    posts = paginator.page(page)
	except PageNotAnInteger:
	    posts = paginator.page(1)
	except EmptyPage:
	    posts = paginator.page(paginator.num_page)
	context = {
		"posts": Post.objects.all(),
		'posts': posts,
        'page': page,
	}
	return render(request, 'blog/home.html', context)

class NewPost(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostDetail(DetailView):
	model = Post

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class UserPosts(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 4

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user)
